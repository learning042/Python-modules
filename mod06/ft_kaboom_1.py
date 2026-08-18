if __name__ == "__main__":
    print(
            "=== Kaboom 1 ===\n"
            "Access to alchemy/grimoire/dark_spellbook.py directly\n"
            "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION"
    )
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    spell_name = "Soulmancy"
    ingredients = "Bats, frogs and bones"
    print("Testing record dark spell: ", end="")
    print(dark_spell_record(spell_name, ingredients))
