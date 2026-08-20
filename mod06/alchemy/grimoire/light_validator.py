def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed_ingredients = light_spell_allowed_ingredients()
    lower = ingredients.lower()
    if any(ingredient in lower for ingredient in allowed_ingredients):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
