from dataclasses import dataclass, field
from typing import Any

@dataclass
class City:
    population: int
    name: str = field(compare=False)
    subject: str = field(compare=False)
    district: str = field(compare=False)
    latitude: float = field(compare=False)
    longitude: float = field(compare=False)
    is_used: bool = field(default=False, compare=False)

    def __post_init__(self) -> None:
        self.validate_name()
        self.validate_population()

    def validate_name(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError(f"Неверное значение поля name: {self.name}")
        
    def validate_population(self) -> None:
        if not isinstance(self.population, int) or self.population <= 0:
            raise ValueError(f"Неверное значение поля population: {self.population}")