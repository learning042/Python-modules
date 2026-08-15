from typing import Any, Protocol
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self, name: str):
        self.buffer: list[tuple[int, str]] = []
        self.count = 0
        self._name = name

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self.buffer:
            raise Exception("No data available for extraction.")
        return self.buffer.pop(0) 

    def get_name(self) -> str:
        return self._name


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for element in data:
                if not isinstance(element, (int, float)) or isinstance(element, bool):
                    return False
            return True
        elif isinstance(data, bool):
            return False
        elif isinstance(data, (int, float)): 
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self.buffer.append((self.count, str(item)))
            self.count += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for element in data:
                if not isinstance(element, str):
                    return False
            return True
        elif isinstance(data, str):
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self.buffer.append((self.count, item))
            self.count += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Log Processor")

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for element in data:
                if not isinstance(element, dict):
                    return False
                for key in element.keys():
                    value = element[key]
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True
        elif isinstance(data, dict):
            for key in data.keys():
                    value = data[key]
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True
        return False

    def ingest(self, data: dict[str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            logEntry = ""
            for key in item.keys():
                logEntry += f"{item[key]}: "
            logEntry = logEntry[:-2]
            self.buffer.append((self.count, logEntry))
            self.count += 1


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        try:
            if isinstance(proc, DataProcessor):
                self._processors.append(proc)
            else:
                raise ValueError("Invalid Processor")
        except ValueError as e:
            print(e)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for data in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(data):
                    proc.ingest(data)
                    handled = True
                    break
            if not handled:
                print(f" DataStream error - Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        print(" === DataStream statistics ===")
        if not self._processors:
            print(" No processor found, no data")
            return
        for proc in self._processors:
            print(f" {proc.get_name()}: "
                  f"total {proc.count} items processed, "
                  f"remaining {len(proc.buffer)} on processor"
                  )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors: 
            data = []
            for _ in range(nb):
                try:
                    data.append(proc.output())
                except Exception:
                    break
            plugin.process_output(data)


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...

class ExportCSV:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print(",".join(value for rank, value in data))

class ExportJSON:
    def process_output(self, data: list[tuple[int, str]]) -> None:
    	print(" {" + ", ".join(f'item_{rank}: "{value}"' for rank, value in data) + "}")


def main() -> None:
    print(" === Code Nexus - Data Pipeline ===")
    print()
    print(" Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    print()
    print(" Registering Processors")
    print()
    batch = ["Hello World",
             [3.14, -1, 2.71],
             [{"log_level": "WARNING", "log_message": "Telnet access! "
             "Use ssh instead"}, {"log_level": "INFO", "log_message":
                                 "User wil is connected"}],
             42,
             ["Hi", "five"]
             ]
    print(f" Send first batch of data on stream: {batch}")
    print()
    numProc = NumericProcessor()
    textProc = TextProcessor()
    logProc = LogProcessor()
    stream.register_processor(numProc)
    stream.register_processor(textProc)
    stream.register_processor(logProc)
    stream.process_stream(batch)
    stream.print_processors_stats()
    print()
    stream.output_pipeline(3, ExportCSV())
    print()
    stream.print_processors_stats()
    second_batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [{"log_level": "ERROR", "log_message": "500 server crash"},
    	{"log_level": "NOTICE", "log_message": "Certificate expires in 10 days"}],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ] 
    print()
    print(f"Send another batch of data: {second_batch}")
    stream.process_stream(second_batch)
    print()
    stream.print_processors_stats()
    print()
    print(" Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, ExportJSON())
    print()
    stream.print_processors_stats()
    

if __name__ == "__main__":
    main()
