import os
import sys
from dotenv import load_dotenv


REQUIRED = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
]


DEFAULT = {
        "MATRIX_MODE": "development",
        "LOG_LEVEL": "DEBUG"
}


SHELL_WINS = True


def load_config() -> tuple[dict[str, str | None], list[str]]:
    load_dotenv(override=not SHELL_WINS)
    config = {}
    missing = []
    for key in REQUIRED:
        value = os.getenv(key)
        if not value:
            missing.append(key)
            value = DEFAULT.get(key)
        config[key] = value
    return (config, missing)


def check_api(key: str | None) -> bool:
    if not key or len(key) < 8:
        return False
    return True


def get_database_status(config: dict) -> str:
    url = config["DATABASE_URL"]
    if not url:
        return "Not set"
    elif config["MATRIX_MODE"] == "development":
        return "Connected to local instance"
    return "Connected to online instance"


def has_hardcoding(config: dict) -> bool:
    try:
        with open(__file__, "r") as f:
            source = f.read()
    except OSError as error:
        print(error, file=sys.stderr)
        sys.exit(1)
    secrets = (
            config["DATABASE_URL"],
            config["API_KEY"],
            config["ZION_ENDPOINT"]
    )
    return any(s and s in source for s in secrets)


def has_leaked_secret(config: dict) -> bool:
    try:
        with open(".gitignore", "r") as f:
            content = f.read()
    except OSError as error:
        print(error, file=sys.stderr)
        sys.exit(1)
    return ".env" not in content


def display_security_checks(config: dict) -> None:
    if not has_hardcoding(config):
        print("[OK] No hardcoded secrets detected")
    else:
        print("[KO] There is/are hardcoded setting(s)")
    if not os.path.isfile(".env"):
        print("[KO] .env file does not exist")
    elif has_leaked_secret(config):
        print("[KO] .env is not in .gitignore")
    else:
        print("[OK] .env file properly configured")
    if SHELL_WINS:
        print(f"[OK] {config['MATRIX_MODE']} overrides available")
    else:
        print(f"[KO] {config['MATRIX_MODE']} overrides unavailable")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    config, missing = load_config()
    for key in missing:
        print(f"[UNSET] {key}")
    mode = config["MATRIX_MODE"]
    if mode not in ("development", "production"):
        print(f"[ERROR] Invalid matrix mode: {mode}", file=sys.stderr)
        sys.exit(1)
    if mode == "production" and missing:
        print(
                "[ERROR] Production mode requires all variables set",
                file=sys.stderr
        )
        sys.exit(1)
    api_status = (
            "Authenticated"
            if check_api(config["API_KEY"])
            else "Unauthenticated"
    )
    print(
        "Configuration loaded:\n"
        f"Mode: {mode}\n"
        f"Database: {get_database_status(config)}\n"
        f"API Access: {api_status}\n"
        f"Log Level: {config['LOG_LEVEL']}\n"
        f"Zion Network: {'Online' if config['ZION_ENDPOINT'] else 'Offline'}\n"
    )
    print("Environment security check:")
    display_security_checks(config)
    print("\nThe Oracle sees all configurations")


if __name__ == "__main__":
    main()
