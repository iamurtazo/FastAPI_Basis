from typing import Any

text: str = "value"
pert: int = 90
temp: float = 37.5

number: int | float = 12

digits: list[int | str] = [1, 2, 3, 4, 5, "six", "seven", "eight"]

table_5: tuple[int, ...] = (5, 10, 15, 20, 25)

city_temp: tuple[str, float] = ("City", 20.5)

shipment: dict[str, str | Any] = {
    "id": 12701,
    "weight": 45.349,
    "content": "wooden table",
    "status": "in transit",
}

def root(num: int | float, exp: float | None = .5) -> float:
    return pow(num, exp)
