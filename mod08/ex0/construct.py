import sys
import os
import site


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def get_sitepkg_path(env_name: str) -> str | None:
    for path in site.getsitepackages():
        if env_name in path and "lib64" not in path:
            return path
    return None


def print_not_in_venv_msg() -> None:
    curr_python = sys.executable
    print(
        "MATRIX STATUS: You're still plugged in\n"
        f"Current Python: {curr_python}\n"
        "Virtual Environment: None detected\n\n"
        "Warning: You're in the global environment!\n"
        "The machines can see everything you install.\n\n"
        "To enter the construct, run:\n"
        "python -m venv matrix_venv\n"
        "source matrix_env/bin/activate # On Unix\n"
        "matrix_env/Scripts/activate # On Windows\n\n"
        "Then run this program again."
    )


def print_in_venv_msg() -> None:
    env_name = os.path.basename(sys.prefix)
    curr_python = sys.executable
    pkg_path = get_sitepkg_path(env_name)
    print(
        "MATRIX STATUS: Welcome to the construct\n"
        f"Current Python: {curr_python}\n"
        f"Virtual Environment: {env_name}\n"
        "SUCCESS: You're in an isolated environment!\n"
        "Safe to install packages without affecting\n"
        "the global system.\n\n"
        "Package installation path:\n"
        f"{pkg_path}"
    )


def main() -> None:
    print_in_venv_msg() if is_in_venv() else print_not_in_venv_msg()


if __name__ == "__main__":
    main()
