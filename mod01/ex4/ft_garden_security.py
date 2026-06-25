class Plant:
    def __init__(self, name: str, height: float,
                 days: int, dgrow: float = 0.8, dage: int = 1) -> None:
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

    def get_age(self) -> int:
        return self._days


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("rose", 15.0, 10)
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-1)
    rose.set_age(-1)
    print()
    rose.show()
