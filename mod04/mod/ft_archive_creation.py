import sys
import typing


def safe_open(filename: str, mode: str = "r") -> typing.IO[str] | None:
    try:
        file = open(filename, mode)
    except OSError as error:
        print(f" Error opening file '{filename}': {error}")
        return None
    return file
    

def cat(file: typing.IO[str]) -> str | None: 
    try:
        buffer = file.read()
        print(" ---")
        print()
        buffer = " " + buffer.replace("\n", "\n ")
        print(" ---")
        print(buffer)
    except (OSError, UnicodeDecodeError) as error:
        print(f" Error reading file '{file.name}': {error}")
        return None
    finally:
        file.close()
        print(f" File '{file.name}' closed.")
    return buffer 


def transform_data(data: str | None) -> str | None:
    if data is None:
        return
    return data.replace("\n", "#\n") 
    

def redirect_data_to_file(filename: str, data: str | None) -> None:
    file : typing.IO[str] | None = None
    if data is None:
        return
    try:
        file = safe_open(filename, "w") 
        if file is None:
            raise OSError()
        print(f" Saving data to '{file.name}'")
        _ = file.write(data) 
        print(f" Data saved in file '{file.name}'")
    except (OSError, UnicodeEncodeError) as error:
        print(f" Error writing to file: {error}")
        return
    finally:
        if file is not None:
            file.close()
       

def main() -> None:
    argc = len(sys.argv)
    if argc != 2:
        print(f" Usage: {sys.argv[0]} <file>")
        return
    print(" === Cyber Archives Recovery & Preservation ===")
    print(f" Acessing file '{sys.argv[1]}'")
    file = safe_open(sys.argv[1])
    if file is None:
        return
    data = cat(file)
    print(" ---")
    print()
    print(" Transform data:")
    data = transform_data(data)
    print(" ---")
    print()
    print(data)
    print(" ---")
    filename = input(" Enter new file name (or empty): ")
    if filename == "":
        print(" Not saving data.")
        return
    redirect_data_to_file(filename, data)
    

if __name__ == "__main__":
    main()