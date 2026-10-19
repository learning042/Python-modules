def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))

def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda mage: mage["power"])["power"],
        "min_power": min(mages, key=lambda mage: mage["power"])["power"],
        "avg_power": round(
            sum(map(lambda mage: mage["power"], mages)) / len(mages), 2
            )
    }

artifact = [
    {"name": "knife", "power": 40, "type": "metal"},
    {"name": "staff", "power": 4000, "type": "fire"}
]

spells = ["fire", "water", "rock", "air"]


art = artifact_sorter(artifact)
art2 = power_filter(artifact, 1000)
spells2 = spell_transformer(spells)
mages = mage_stats(artifact)
print(art)
print(art2)
print(spells2)
print(mages)


