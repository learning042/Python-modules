from collections.abc import Callable

def heal(target: str, power: int) -> str:
    return f"Heals restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball burns {target} for {power} damage"

def condition(target: str, power: int) -> bool:
    return power > 10


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: spell(target, power) if condition(target, power) else "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: 


combined = spell_combiner(fireball, heal)
result = combined("Dragon", 10)
print(result[0], result[1])

mega_fireball = power_amplifier(fireball, 3)
result = mega_fireball("Dragon", 10)
print(result)


using_spell = conditional_caster(condition, fireball)
spell = using_spell("Dragon", 11)
print(spell)



