import sys


def create_inventory() -> dict[str, int]:
    inventory = {}
    for pairs in sys.argv[1:]:
        try:
            pair = pairs.split(':')
            if len(pair) != 2:
                print(f" Error - invalid parameter '{pair[0]}'")
                continue
            if pair[0] in inventory:
                print(f" Redundant item '{pair[0]}' - discarding")
                continue
            inventory[pair[0]] = int(pair[1])
        except ValueError as e:
            print(f" Quantity error for '{pair[0]}': {e}")
    return inventory


def main() -> None:
    print(" === Inventory System Analysis ===")
    inventory = create_inventory()
    if len(inventory) == 0:
        print(" Empty inventory!")
        return
    print(f" Got inventory: {inventory}")
    item_list = list(inventory.keys())
    total_quant = sum(inventory.values())
    inventory_len = len(inventory)
    print(f" Item list: {item_list}")
    print(f" Total quantity of the {inventory_len} items: {total_quant}")
    for key in inventory:
        percentage = round(inventory[key] * 100 / total_quant, 1)
        print(f" Item {key} represents {percentage}%")
    greatest = item_list[0]
    for item in item_list:
        if inventory[item] > inventory[greatest]:
            greatest = item
    print(f" Item most abundant: {greatest}"
          f"with quantity {inventory[greatest]}")
    least = item_list[0]
    for item in item_list:
        if inventory[least] > inventory[item]:
            least = item
    print(f" Item least abundant: {least} with quantity {inventory[least]}")
    inventory.update({"magic_item": 1})
    print(f" Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
