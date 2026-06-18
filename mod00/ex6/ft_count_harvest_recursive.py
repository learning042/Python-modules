def ft_count_harvest_recursive(d=int(input("Days until harvest: ")), h=True):
    if d == 0:
        return
    ft_count_harvest_recursive(d - 1, False)
    print(f"Day {d}")
    if h is True:
        print("Harvest time!")
