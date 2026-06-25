class Plant:
    def __init__(self, name: str,
                 height: float,
                 days: int,
                 dgrow: float = 0.8,
                 dage: int = 1
                 ) -> None:
        self._name = name.capitalize()
        if height < 0:
            print("Error, height can't be negative")
            self._height = 0.
        else:
            self._height = height
        if days < 0:
            print("Error, age can't be negative")
            self._days = 0
        else:
            self._days = days
        self._dgrow = dgrow
        self._dage = dage
        self._growth = 0.
        print("Plant Created: ", end='')
        print(f"{self._name}: {self._height:.1f}cm, {self._days} days old")

    def show(self) -> None:
        print("Current state: ", end='')
        print(f"{self._name}: {self._height:.1f}cm, {self._days} days old")

    def grow(self) -> None:
        self._height += self._dgrow
        self._growth += self._dgrow

    def age(self) -> None:
        self._days += self._dage

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height:.0f}cm")

    def set_age(self, days: int) -> None:
        if days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = days
            print(f"Age updated: {self._days} days")

    def get_height(self) -> float:
        return round(self._height, 1)


class Flower(Plant):
    def __init__(self, name: str,
                 height: float,
                 days: int,
                 color: str,
                 bloomed: bool = False,
                 dgrow: float = 0.8,
                 dage: int = 1,
                 ) -> None:
        super().__init__(name, height, days, dgrow, dage)
        self._color = color
        self._bloomed = bloomed

    def bloom(self) -> None:
        if not self._bloomed:
            print(f"(asking the {self._name.lower()} to bloom)")
            self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str,
                 height: float,
                 days: int,
                 trunk_diameter: float,
                 dgrow: float = 0.8,
                 dage: int = 1,
                 ) -> None:
        super().__init__(name, height, days, dgrow, dage)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"(asking the {self._name.lower()} to produce shade)")
        print(f"Tree {self._name} now produces a shade of"
              f" {self._height:.1f}cm long and"
              f" {self._trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str,
                 height: float,
                 days: int,
                 harvest_season: str,
                 nutritional_value: int,
                 dgrow: float = 0.8,
                 dage: int = 1,
                 ) -> None:
        super().__init__(name, height, days, dgrow, dage)
        self._harvest_season = harvest_season.capitalize()
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def grow_and_age(self, days: int = 1):
        print(f"(make {self._name.lower()} grow and age for {days} days)")
        for _ in range(days):
            self.grow()
            self.age()
            self._nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable("tomato", 5.0, 10, "april", 0, dgrow=2.1)
    tomato.show()
    tomato.grow_and_age(20)
    tomato.show()
