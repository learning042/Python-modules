from importlib import import_module

def validate_ingredients(ingredients: str) -> str:
    module = import_module("alchemy.grimoire.light_spellbook")
    allowed = module.light_spell_allowed_ingredients()
    lower = ingredients.lower()
    if any(ingredient in lower for ingredient in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
