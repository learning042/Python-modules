import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            inputs = input(
                            "Enter new coordinates as "
                            "floats in format 'x,y,z': "
                           ).split(',')
            if len(inputs) != 3:
                print("Invalid syntax")
                continue
            coordinates = []
            for coord in inputs:
                coordinates += [float(coord)]
        except ValueError as e:
            print(f"Error on parameter {coord}: {e}")
            continue
        return (coordinates[0], coordinates[1], coordinates[2])


def distance(
             coord1: tuple[float, float, float] = (0.0, 0.0, 0.0),
             coord2: tuple[float, float, float] = (0.0, 0.0, 0.0)
             ) -> float:
    dist = 0.
    for i in [0, 1, 2]:
        dist += (coord2[i] - coord1[i]) ** 2
    dist = math.sqrt(dist)
    return dist


if __name__ == "__main__":
    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Get a first tuple: {first}")
    print(f"It includes: X={first[0]:.1f}, Y={first[1]:.1f}, Z={first[2]:.1f}")
    r1 = distance(first)
    print(f"Distance to center: {r1:.4f}")
    print()
    print("Get a second set of coordinates")
    second = get_player_pos()
    r12 = distance(first, second)
    print(f"Distance between the 2 sets of coordinates: {r12:.4f}")
