from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from typing import Self
from datetime import datetime


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name:str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def apply_mission_validation(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not any(member.rank in (Rank.commander, Rank.captain) for member in self.crew):
            raise ValueError("Mission must have at least one Commander or Captain")
        if self.duration_days > 365:
            experienced = sum(1 for member in self.crew if member.years_experience >= 5)
            if experienced < len(self.crew) / 2:
                raise ValueError("Long missions (> 365 days) need 50% experienced crew (5+ years)")
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self

    def print_mission_info(self) -> None:
        print(
            f"Mission: {self.mission_name}\n"
            f"ID: {self.mission_id}\n"
            f"Destination: {self.destination}\n"
            f"Duration: {self.duration_days} days\n"
            f"Budget: ${self.budget_millions}M\n"
            f"Crew size: {len(self.crew)}\n"
            "Crew members:" 
        )
        for member in self.crew:
            print(f"- {member.name} ({member.rank.value}) - {member.specialization}")
        print()
        


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)
    print("Valid mission created:")
    valid_crew = [
        CrewMember(
            member_id="Hello",
            name="Sarah Connor",
            rank=Rank.commander,
            age=18,
            specialization="Mission Command",
            years_experience=6,
        ),
        CrewMember(
            member_id="Hello",
            name="John Smith",
            rank=Rank.lieutenant,
            age=18,
            specialization="Navigation",
            years_experience=6,
        ),
        CrewMember(
            member_id="Hello",
            name="Alice Johnson",
            rank=Rank.officer,
            age=18,
            specialization="Engineering",
            years_experience=6,
        )
        
    ]
    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.now(),
        duration_days=900,
        crew=valid_crew,
        budget_millions=2500.0
    )
    valid_mission.print_mission_info()
    print("=" * 40)
    try:
        invalid_crew = [
            CrewMember(
                member_id="Hello",
                name="Sarah Connor",
                rank=Rank.lieutenant,
                age=18,
                specialization="Mission Command",
                years_experience=6,
            ),
            CrewMember(
                member_id="Hello",
                name="John Smith",
                rank=Rank.lieutenant,
                age=18,
                specialization="Navigation",
                years_experience=6,
            ),
            CrewMember(
                member_id="Hello",
                name="Alice Johnson",
                rank=Rank.officer,
                age=18,
                specialization="Engineering",
                years_experience=6,
            )
        ]
        invalid_mission = SpaceMission(
                mission_id="M2024_MARS",
                mission_name="Mars Colony Establishment",
                destination="Mars",
                launch_date=datetime.now(),
                duration_days=900,
                crew=invalid_crew,
                budget_millions=2500.0
        )
        invalid_mission.print_mission_info()
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
