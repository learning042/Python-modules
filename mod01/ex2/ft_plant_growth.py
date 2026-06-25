class Plant:
    def __init__(self, name: str, height: float,
                 days: int, dgrow: float = 0.8, dage: int = 1) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days = days
        self.dgrow = dgrow
        self.dage = dage
        self.growth = 0.

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def grow(self):
        self.height += self.dgrow
        self.growth += self.dgrow

    def age(self):
        self.days += self.dage


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("rose", 25.0, 30)
    rose.show()
    for i in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {i} ===")
        rose.show()

    print(f"Growth this week: {rose.growth:.1f}cm")
