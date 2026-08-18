from importlib import import_module


def validate_ingredients(ingredients: str) -> str:
    module = import_module(".light_spellbook", package=__package__)
    allowed_ingredients = module.light_spell_allowed_ingredients()
    lower = ingredients.lower()
    if any(ingredient in lower for ingredient in allowed_ingredients):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
