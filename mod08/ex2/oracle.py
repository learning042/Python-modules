import os
from dotenv import load_dotenv


REQUIRED_CONFIGS = (
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
    return (
        "Authenticated ("
        "*" * (len(api_key) - 4) + api_key[:-4]
        ")"
        )


def display_warn_and_erros():
    ...


def display_status(config: dict[str, str | None]) -> None:
    print("ORACLE STATUS: Reading the Matrix...\n\n")
    missing_keys = return_missing_keys(config)
    if missing_keys:
        print("[WARN] Missing configuration values:")
        for key in missing_keys:
            print(f"	{key}")
        print()
        if config["MATRIX_MODE"] == "production":
            print("[ERROR] Production mode requires complete config.")
    print(
        "Configuration loaded:\n"
        ""
    )
    
    
    
    

    
    


def main() -> None:
    config = build_config()
    print(config)


if __name__ == "__main__":
    main()
