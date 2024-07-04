from dataclasses import dataclass, field
	
@dataclass
class Vector:
	x : float
	y : float
	
	Up    : tuple = (0, -1)
	Down  : tuple = (0,  1)
	Left  : tuple = (-1, 0)
	Right : tuple = ( 1, 0)
	
	
@dataclass(frozen=True)
class Color:
	black : tuple = (0,0,0)
	white : tuple = (255,255,255)