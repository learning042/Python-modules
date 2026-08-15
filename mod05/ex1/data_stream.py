from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self, name: str):
        self.buffer: list[tuple[int, str]] = []
        self.count = 0
        self._name = name

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

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
                logEntry += f": {item[key]}"
            self.buffer.append((self.count, logEntry))
            self.count += 1


class DataStream:
    def __init__(self) -> None:
        self._processors = []

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


def main() -> None:
    print(" === Code Nexus - Data Stream ===")
    print()
    print(" Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    print()
    print(" Registering Numeric Processor")
    print()
    numProc = NumericProcessor()
    stream.register_processor(numProc)
    print()
    batch = ["Hello World",
             [3.14, -1, 2.71],
             [{"log_level": "Warning", "log_message": "Telnet access! "
             "Use ssh instead"}, {"log_level": "INFO", "log_message":
                                 "User wil is connected"}],
             42,
             ["Hi", "five"]
             ]
    print(f" Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    print()
    print(f" Registering other data processors")
    textProc = TextProcessor()
    logProc = LogProcessor()
    stream.register_processor(textProc)
    stream.register_processor(logProc)
    stream.process_stream(batch)
    print(" Send the same batch again")
    stream.print_processors_stats()
    print()
    print(" Consume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numProc.output()
    for _ in range(2):
        textProc.output()
    logProc.output()
    stream.print_processors_stats()
    

if __name__ == "__main__":
    main()
