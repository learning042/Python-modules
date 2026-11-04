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



def mask_key(key: str) -> str:
    if len(key) < 8:
        raise ValueError("Invalid api key")
    return "*" * (len(key) - 4) + key[-4:]


def build_config(config_file: str) -> dict[str, str | None]:
    load_dotenv(config_file)
    config = {}
    for key in REQUIRED_CONFIGS:
        config[key] = os.getenv(key, DEFAULT_CONFIGS.get(key))
    return config


def show_missing_config(config: dict[str, str | None]) -> None:
    for key in REQUIRED_CONFIGS:
        if config[key] is None:
            print(f"[UNSET-VALUE] {key}")


def print_config(config: dict[str, str | None]) -> None:
    print(f"Mode: {config['MATRIX_MODE']}")
    if config["MATRIX_MODE"] == "development":
        print("Connected to local instance", end="")
    elif config["MATRIX_MODE"] == "production":
        print("Connected to online instance", end="")
    print(" : {config['DATABASE_URL']}")
    if config["API_KEY"]:
        print(f"API Access: Authenticated {mask_key(config['API_KEY'])}")
    else:
        print(f"API Access: Unauthenticated")
    print(f"Log level: {config['LOG_LEVEL']}")
    print("Zion Network: Online")

    
def main() -> None:
    config = build_config(".env.example")
    print_config(config)


if __name__ == "__main__":
    main()
