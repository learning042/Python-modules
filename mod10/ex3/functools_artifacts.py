from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul, gt, lt
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
            "add": add,
            "multiply": mul,
            "max": lambda x, y: x if gt(x, y) else y,
            "min": lambda x, y: x if lt(x, y) else y
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: '{operation}'")
    if not spells:
        return 0
    return reduce(operations[operation], spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return (
            f"Element: {element}\n"
            f"Power: {power} attack damage\n"
            f"Target: {target}\n"
    )


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
            "fire": partial(base_enchantment, power=50, element="fire"),
            "water": partial(base_enchantment, power=50, element="water"),
            "wind": partial(base_enchantment, power=50, element="wind")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative!")
    if n == 0 or n == 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast_spell(spell: Any) -> str:
        return "unknown spell type"


    @cast_spell.register(int)
    def _0(damage_spell: int) -> str:
        return f"{damage_spell} damage"

    @cast_spell.register(str)
    def _1(enchantment: str) -> str:
        return enchantment

    @cast_spell.register(list)
    def _2(multi_cast: list) -> str:
        return f"{len(multi_cast)} spells"

    return cast_spell


try:
    print(spell_reducer([1, 2, 3], "j"))
except ValueError as error:
    print(error)




partial = partial_enchanter(base_enchantment)["wind"](target="dragon")
print(partial)

print(memoized_fibonacci(40))
print(spell_dispatcher()([1, 2, 3]))
