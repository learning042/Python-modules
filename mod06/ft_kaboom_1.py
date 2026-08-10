def main() -> None:
    spell_name = "Soulmancy"
    ingredients = "Bats, frogs and bones"
    print(f" Testing record dark spell: "
          f"{dark_spell_record(spell_name, ingredients)}")


if __name__ == "__main__":
    print(" === Kaboom 1 ===")
    print(" Access to alchemy/grimoire/dark_spellbook.py directly")
    print(" Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    main()
