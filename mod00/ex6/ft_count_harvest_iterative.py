def ft_count_harvest_iterative():
    harvest_day = int(input("Days until harvest: "))
    for day in range(1, harvest_day + 1):
        print(f"Day {day}")
    print("Harvest time!")
