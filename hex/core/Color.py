from dataclasses import dataclass

@dataclass
class Color:
    r: int
    g: int
    b: int

DARK_GRAY = Color(30, 31, 34)
LIGHT_GRAY = Color(54, 55, 60)
