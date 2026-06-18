def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit != "packets" and unit != "grams" and unit != "area":
        print("Unknown unit type")
        return
    print(f"{seed_type.capitalize()} seeds: ", end='')
    if unit == "packets":
        print(f"{quantity} packets available")
    elif unit == "area":
        print(f"covers {quantity} square meters")
    else:
        print(f"{quantity} grams total")
