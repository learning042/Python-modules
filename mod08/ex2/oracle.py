import os
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


def load_config() -> tuple[dict, list]:
    load_dotenv()
    config = {}
    missing = []
    for key in REQUIRED:
        value = os.getenv(key)
        if not value:
            missing.append(key)
            value = DEFAULT.get(key)
        config[key] = value
    return (config, missing)


def mask_key(key: str) -> str:
    return "*" * (len(key) - 4) + key[-4:]


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
        print(error)
    secrets = (config["DATABASE_URL"], config["API_KEY"], config["ZION_ENDPOINT"])
    return any(s and s in secrets for s in source)
    

def has_leaked_secret(config: dict) -> bool:
    try:
        with open(".gitignore", "r") as f:
            content = f.read()
    except OSError as error:
        print(error)
    return ".env" not in [line.strip() for line in content]


def has_override() -> bool:
    os.environ["TEST"] = "not ovewritten"
    try:
        with open(".env.tmp", "w") as f:
            f.write("TEST=overwritten\n")
    except OSError as error:
        print(error)
    load_dotenv(".env.tmp", override=True)
    result = os.environ["TEST"] == "overwritten"
    del os.environ["TEST"]
    return result

    
def display_security_checks(config: dict) -> None:
    # checar hardcoded
    # checar gitignore
    # checar overrides
    if not has_hardcoding(config):
        print("[OK] No hardcoded secrets detected")
    else:
        print("[KO] There is/are hardcoded setting(s)")
    if not os.path.isfile(".env"):
        print("[KO] .env file does not exit")
    elif has_leaked_secret(config):
        print("[KO] .env is not in .gitignore") 
    else:
        print("[OK] .env file properly configured")
    if has_override():
        print("[OK] Production overrides available")
    else:
        print("[KO] Production overrides unavailable")



def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    config, missing = load_config()
    for key in missing:
        print(f"[UNSET] {key}")
    mode = config["MATRIX_MODE"]
    if mode not in ("development", "production"):
        raise ValueError("[ERROR] Invalid matrix mode: {mode}")
    if mode == "production" and missing:
        raise ValueError("[ERROR] Production mode requires all variables set")


    print("Configuration loaded:")
    print(
            f"Mode: {mode}\n"
            f"Database: {get_database_status(config)}\n"
            "API Access: "
            f"{'Authenticated' if check_api(config['API_KEY']) else 'Unauthenticated'}\n"
    )
    print("Environment security check:")
    display_security_checks(config)


if __name__ == "__main__":
    main()
