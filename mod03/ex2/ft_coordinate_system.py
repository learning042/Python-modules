import math


def get_player_pos() -> tuple[float, float, float] | None:
    while True:
        try:
             args = input(
                            "Enter new coordinates as "
                            "floats in format 'x,y,z': "
                           )
             x, y, z = args.split(',')
        except (KeyboardInterrupt, EOFError) as e:
            print(f"Program interrupted: {e}")
            return None
        except ValueError as e:
            print(f"Invalid Syntax")
            continue
        try:
            coords = [x, y, z]
            for i in range(3):
                coords[i] = float(coords[i])
        except ValueError as e:
            print(f"Error on parameter {coords[i]}: {e}")
            return None
        return (coords[0], coords[1], coords[2])


def distance(
             coord1: tuple[float, float, float] = (0.0, 0.0, 0.0),
             coord2: tuple[float, float, float] = (0.0, 0.0, 0.0)
             ) -> float:
    dist = 0.
    for i in [0, 1, 2]:
        dist += (coord2[i] - coord1[i]) ** 2
    dist = math.sqrt(dist)
    return dist


def main() -> None:
    print("Get a first set of coordinates")
    first = get_player_pos()
    if first is None:
        return
    print(f"Get a first tuple: {first}")
    print(f"It includes: X={first[0]:.1f}, Y={first[1]:.1f}, Z={first[2]:.1f}")
    r1 = distance(first)
   print(f"Distance to center: {r1:.4f}")
    print()
    print("Get a second set of coordinates")
    second = get_player_pos()
    if second is None:
        return
    r12 = distance(first, second)
    print(f"Distance between the 2 sets of coordinates: {r12:.4f}")



if __name__ == "__main__":
    main()
