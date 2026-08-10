import alchemy.grimoire


def main() -> None:
    print(" === Kaboom 0 ===")
    print(" Using grimoire module directly")
    spell_name = "Fantasy"
    ingredients = "Earth, wind and fire"
    print(f" Testing record light spell: "
          f"{alchemy.grimoire.light_spell_record(spell_name, ingredients)}")


if __name__ == "__main__":
    main()
