class Plant:
    def __init__(self, name: str, height: float,
                 days: int, dgrow: float = 0.8, dage: int = 1) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days = days
        self.dgrow = dgrow
        self.dage = dage
        self.growth = 0.
        print("Created: ", end='')
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def grow(self):
        self.height += self.dgrow
        self.growth += self.dgrow

    def age(self):
        self.days += self.dage


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("rose", 25.0, 30)
    oak = Plant("oak", 200.0, 365)
    cactus = Plant("cactus", 5.0, 90)
    sunflower = Plant("sunflower", 80.0, 45)
    fern = Plant("fern", 15.0, 120)
