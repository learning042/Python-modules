from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self):
        self.buffer: list[str] = []
        self.index = -1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        extracted = self.buffer.pop(0)
        self.index += 1
        return (self.index, extracted)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

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
        if isinstance(data, list):
            self.buffer.extend(str(item) for item in data)
        else:
            self.buffer.append(str(data))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

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
        if isinstance(data, list):
            self.buffer.extend(item for item in data)
        else:
            self.buffer.append(data)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

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
        if isinstance(data, list):
            for dictionary in data:
                logEntry = ""
                for key in dictionary.keys():
                    logEntry += f": {dictionary[key]}"
                self.buffer.append(logEntry)
        else:
            logEntry = ""
            for key in data.keys():
                logEntry += f": {data[key]}"
            self.buffer.append(logEntry)
        

def numericTests() -> None:
    print()
    print("Testing Numeric Processor...")
    numericTest= NumericProcessor()
    data0 = 42
    data1 = "Hello"
    data2 = "foo"
    datas: list[int | float] = [1, 2, 3, 4, 5]
    test0 = numericTest.validate(data0)
    test1 = numericTest.validate(data1)
    print(f" Trying to validate input '{data0}': {test0}") 
    print(f" Trying to validate input '{data1}': {test1}") 
    print(f" Test invalid ingestion of string '{data2}' without prior validation:")
    try:
        numericTest.ingest(data2)
    except ValueError as e:
        print(f" Got exception: {e}")
    print(" Extracting 3 values...")
    numericTest.ingest(datas)
    for _ in range(3):
        rank, value = numericTest.output()
        print(f" Numeric value {rank}: {value}")


def textTests() -> None:
    print()
    print("Testing Text Processor...") 
    data0 = 42
    datas = ["Hello", "Nexus", "World"]
    textTest = TextProcessor() 
    test0 = textTest.validate(data0)
    print(f" Trying to validate input '{data0}': {test0}")
    print(f" Processing data: {datas}")
    print(" Extracting 1 value...")
    textTest.ingest(datas)
    rank, value = textTest.output()
    print(f" Text value {rank}: {value}")


def logTests() -> None:
    print()
    print("Testing Log Processor...")
    data0 = "Hello"
    logTest = LogProcessor()
    test0 = logTest.validate(data0)
    print(f" Trying to validate input '{data0}': {test0}")
    datas = [{"log_level": "Notice", "log_message": "Connection to server"}, {"log_level": "ERROR", "log_message": "Unauthorized access!!"}]
    print(f" Processing data: {datas}")
    print(" Extracting 2 values...")
    logTest.ingest(datas)
    for _ in range(2):
        rank, value = logTest.output()
        print(f" Log entry {rank}{value}")
    #datas2 = {"hello": "oi", "world": "mundo"}
    #logTest.ingest(datas2)
    #rank, value = logTest.output()
    #print(f" Log entry {rank}: {value}")
    # datas3 = {"hello": "oi", 12: "mundo"}  
    # print(f" Test invalid ingestion of dict '{datas3}' without prior validation:")
    # try:
    #     logTest.ingest(datas3)
    #     rank, value = logTest.output()
    #     print(f" Log entry {rank}: {value}")
    # except ValueError as e:
    #     print(f" Got exception: {e}")

    
def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    numericTests()
    textTests()
    logTests()


if __name__ == "__main__":
    main()
