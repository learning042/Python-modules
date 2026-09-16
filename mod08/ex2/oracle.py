import os
from dotenv import load_dotenv


REQUIRED_CONFIG = (
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT"
)


DEFAULT_CONFIGS = {
    "MATRIX_MODE": "development",
    "LOG_LEVEL": "DEBUG",
    "ZION_ENDPOINT": "https://zion.com/end_point"
}


PRODUCT_KEYS = (
    "morpheus42",
    "neo42",
    "trinity42",
    "42school"
)


def get_config(key: str) -> str | None:
    load_dotenv()
    return os.getenv(key, DEFAULT_CONFIGS.get(key))
    

def build_config() -> dict[str, str | None]:
    config = {}
    for key in REQUIRED_CONFIG:
        config[key] = get_config(key)
    return config


def return_missing_keys(config: dict[str, str | None]) -> tuple[str, ...]:
    return (key for key in config if config[key] is None)


def is_valid_api_key_format(api_key: str) -> bool:
    if not api_key:
        return False
    elif len(key) < 8:
        return False
    return True


def mask_key(api_key: str) -> str:
    if not api_key:
        return "[NOT SET]"
    if not is_valid_api_key_format(api_key):
        raise ValueError("Invalid key") 
    return "*" * (len(api_key) - 4) + api_key[:-4]


def display_status(config: dict[str, str | None]) -> None:
    ...


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    config = build_config()
    print(config)


if __name__ == "__main__":
    main()
