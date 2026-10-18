from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStationModel(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)
    space_station = SpaceStationModel(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        is_operational=False,
        last_maintenance=datetime.now(),
    )
    print(
        "Valid station created:\n"
        f"ID: {space_station.station_id}\n"
        f"Name: {space_station.name}\n"
        f"Crew: {space_station.crew_size} people\n"
        f"Power: {space_station.power_level}%\n"
        f"Oxygen: {space_station.oxygen_level}%\n"
        f"Status: {'Operational' if space_station.is_operational else 'Not operational'}\n"
    )
    print("=" * 40)
    try:
        space_station = SpaceStationModel(
            station_id="ISS001",
            name="International Space Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            is_operational=False,
            last_maintenance=datetime.now(),
        )
        print(
            "Valid station created:\n"
            f"ID: {space_station.station_id}\n"
            f"Name: {space_station.name}\n"
            f"Crew: {space_station.crew_size} people\n"
            f"Power: {space_station.power_level}%\n"
            f"Oxygen: {space_station.oxygen_level}%\n"
            f"Status: {'Operational' if space_station.is_operational else 'Not operational'}\n"
        )	
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
