import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            user = input("Enter new coordinates as " +
                         "floats in format 'x,y,z': ")
            x, y, z = user.split(",")
        except (EOFError, KeyboardInterrupt) as error:
            print(error)
            continue
        except ValueError:
            print("Invalid Syntax")
            continue

        try:
            coords = []
            for value in [x.strip(), y.strip(), z.strip()]:
                coords.append(float(value))
            return (coords[0], coords[1], coords[2])
        except ValueError as error:
            print(f"Error on parameter '{value}': {error}")


def print_coords(coords: tuple[float, float, float]) -> None:
    print(f"Got a first tuple: {coords}")
    print(f"It includes: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")


"""
Implementation with N dimensions:

def ft_range(number: int) -> list[int]:
    i = 0
    iterable = []
    while i < number:
        iterable.append(i)
        i += 1
    return iterable

def count_args(*args: float) -> int:
    count = 0
    for arg in args:
        count += 1
    return count

def distance(*coordinates: float) -> float:
    dimension = count_args(*coordinates)
    if dimension % 2 == 0:
        dimension //= 2
    else:
        raise ValueError("The number of coordinates must be even!")
    coords1 = [*coordinates[dimension:]]
    coords2 = [*coordinates[:dimension]]
    iterations = ft_range(dimension)
    sum_of_squares = 0.
    for i in iterations:
        sum_of_squares += (coords1[i] - coords2[i]) ** 2
    return round(math.sqrt(sum_of_squares), 4)

    first = get_player_pos()
    print(f"Distance to center: {distance(*first, 0, 0, 0)}\n")
    second = get_player_pos()
    print("Distance between two sets of coordinates: " +
          f"{distance(*first, *second)}")
"""


def distance(
        coord1: tuple[float, float, float],
        coord2: tuple[float, float, float] = (0, 0, 0)
        ) -> float:
    return round(math.sqrt(
            (coord1[0] - coord2[0]) ** 2 +
            (coord1[1] - coord2[1]) ** 2 +
            (coord1[2] - coord2[2]) ** 2
    ), 4)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first = get_player_pos()
    print_coords(first)
    print(f"Distance to center: {distance(first)}\n")
    print("Get a second set of coordinates")
    second = get_player_pos()
    print("Distance between the 2 sets of coordinates: ",
          distance(first, second))


if __name__ == "__main__":
    main()
