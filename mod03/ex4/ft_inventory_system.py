import sys


def get_inventory(args: list[str]) -> dict[str, int]:
    inventory = {}
    for arg in args:
        item = arg.split(":")
        if len(item) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        key, value = item
        key = key.strip()
        value = value.strip()
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
        else:
            try:
                inventory[key] = int(value)
            except ValueError as error:
                print(f"Quantity error for '{key}': {error}")
    return inventory


def print_percentages(inventory: dict[str, int], total: int) -> None:
    for item in inventory.keys():
        percentage = 100 * inventory[item] / total
        print(f"Item {item} represents: {percentage:.1f}%")


def print_most_abundant(inventory: dict[str, int]) -> None:
    items = list(inventory.keys())
    most = items[0]
    for item in items:
        if inventory[item] > inventory[most]:
            most = item
    print(f"Item most abundant: {most} with quantity {inventory[most]}")


def print_least_abundant(inventory: dict[str, int]) -> None:
    items = list(inventory.keys())
    least = items[0]
    for item in items:
        if inventory[item] < inventory[least]:
            least = item
    print(f"Item least abundant: {least} with quantity {inventory[least]}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = get_inventory(sys.argv[1:])
    size = len(inventory)
    total = sum(inventory.values())
    print(
        f"Get inventory: {inventory}\n"
        f"Item list: {list(inventory.keys())}\n"
        f"Total quantity of the {size} items: {total}"
    )
    print_percentages(inventory, total)
    if not size:
        print("There isn't any items!")
    else:
        print_most_abundant(inventory)
        print_least_abundant(inventory)
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
