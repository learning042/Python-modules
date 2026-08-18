from typing import Any, Protocol
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._batch: list[tuple[int, str]] = []
        self._count = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self._batch:
            raise Exception("No data available!")
        return self._batch.pop(0)

    def get_batch(self) -> list[tuple[int, str]]:
        return self._batch

    def get_count(self) -> int:
        return self._count


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        samples = data if isinstance(data, list) else [data]
        for sample in samples:
            if (
                not isinstance(sample, (int, float))
                or isinstance(sample, bool)
            ):
                return False
        return True

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        samples = data if isinstance(data, list) else [data]
        for sample in samples:
            self._batch.append((self._count, str(sample)))
            self._count += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        samples = data if isinstance(data, list) else [data]
        for sample in samples:
            if not isinstance(sample, str):
                return False
        return True

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        samples = data if isinstance(data, list) else [data]
        for sample in samples:
            self._batch.append((self._count, sample))
            self._count += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        samples = data if isinstance(data, list) else [data]
        for sample in samples:
            if not isinstance(sample, dict):
                return False
            for key in sample.keys():
                if (
                    not isinstance(key, str)
                    or not isinstance(sample[key], str)
                ):
                    return False
        return True

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        samples = data if isinstance(data, list) else [data]
        for sample in samples:
            total_entry = ""
            for value in sample.values():
                total_entry += f"{value}: "
            self._batch.append((self._count, total_entry[:-2]))
            self._count += 1


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(value[1] for value in data))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON output:")
        json = {f"item_{rank}": f"{value}" for rank, value in data}
        print(json.__str__().replace("\'", "\""))


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if not isinstance(proc, DataProcessor):
            raise ValueError(
                f"Invalid DataProcessor, {proc} "
                "is '{type(proc).__name__}'"
            )
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(data):
                    proc.ingest(data)
                    handled = True
                    break
            if not handled:
                print(
                    " DataStream error - "
                    f"Can't process element in stream: {data}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processors, no data")
        for proc in self._processors:
            print(
                f"{proc.__class__.__name__[:-9]} "
                f"{proc.__class__.__name__[-9:]}: total "
                f"{proc.get_count()} items processed, "
                f"remaining {len(proc.get_batch())} on processor"
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


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")
    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO",
             "log_message": "User wil is connected"}
        ],
        42,
        ["Hi", "five"]
    ]
    batch2 = [
            21,
            ["I love AI", "LLMs are wonderful", "Stay healthy"],
            [
                {
                    "log_level": "ERROR",
                    "log_message": "500 server crash"
                },
                {
                    "log_level": "NOTICE",
                    "log_message": "Certificate expires in 10 days"
                }
            ],
            [32, 42, 64, 84, 128, 168],
            "World hello"
    ]

    datastream = DataStream()
    processors = [
            NumericProcessor(),
            TextProcessor(),
            LogProcessor()
            ]
    print()
    datastream.print_processors_stats()
    print()
    print("Registering Processors\n")
    for proc in processors:
        datastream.register_processor(proc)
    print(f"Send first batch of data on stream: {batch}")
    datastream.process_stream(batch)
    print()
    datastream.print_processors_stats()
    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    datastream.output_pipeline(3, CSVPlugin())
    print()
    datastream.print_processors_stats()
    print()
    print(f"Send another batch of data: {batch2}\n")
    datastream.process_stream(batch2)
    datastream.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    datastream.output_pipeline(5, JSONPlugin())
    print()
    datastream.print_processors_stats()


if __name__ == "__main__":
    main()
