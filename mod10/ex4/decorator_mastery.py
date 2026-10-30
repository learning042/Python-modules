from collections.abc import Callable
from typing import Any
import time
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    for i in range(50000):
        continue
    return "Fireball cast!"

print(fireball())


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power: int, *args: Any, **kwargs) -> Any:
            if power < min_power:
                return "Insufficient power for this spell"
            return func(power, *args, **kwargs)
        return wrapper
    return decorator


@power_validator(10)
def spell(power: int, name: str) -> str:
    return f"Casting {power} power spell {name}!"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            print(f"Spell casting failed after {max_attempts} attempts")
            print("Waaaaaaagh spelled !")
            return
        return wrapper
    return decorator
            
@retry_spell(5)
def prob_spell() -> None:
    raise ValueError("error")

print(spell(9, "fire"))
prob_spell()
