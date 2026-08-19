from typing import Any
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


def NumericTest() -> None:
    test0 = 42
    test1 = "hello"
    test2 = "foo"
    test3: list[int | float] = [1, 2, 3, 4, 5]
    processor = NumericProcessor()
    print("Testing Numeric Processor...")

    print(f" Trying to validaput '{test0}': {processor.validate(test0)}")
    print(f" Trying to validaput '{test1}': {processor.validate(test1)}")
    print(f" Test invalid ingestion of string '{test2}' "
          "without prior validation:")
    try:
        processor.ingest(test2)
    except ValueError as error:
        print(f" Got exception: {error}")
    print(f" Processing data: {test3}")
    processor.ingest(test3)
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = processor.output()
        print(f" Numeric value {rank}: {value}")


def TextTest() -> None:
    test0 = 42
    test1 = ["Hello", "Nexus", "World"]
    processor = TextProcessor()
    print("Testing Text Processor...")
    print(f" Trying to validate input {test0}: "
          f"{processor.validate(test0)}")
    print(f" Processing data: {test1}")
    print(" Extracting 1 value...")
    processor.ingest(test1)
    rank, value = processor.output()
    print(f" Text value {rank}: {value}")


def LogTest() -> None:
    test0 = "hello"
    test1 = [
                {"log_level": "NOTICE", "log_message": "Connection to server"},
                {"log_level": "ERROR", "log_message": "Unauthorized acess!!"}
            ]
    processor = LogProcessor()
    print("Testing Log Processor...")
    print(f" Trying to validate input {test0}: "
          f"{processor.validate(test0)}")
    print(f" Processing data: {test1}")
    print(" Extracting 2 values...")
    processor.ingest(test1)
    for i in range(2):
        rank, value = processor.output()
        print(f" Log entry {rank}: {value}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    NumericTest()
    print()
    TextTest()
    print()
    LogTest()


if __name__ == "__main__":
    main()
