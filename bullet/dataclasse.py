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
	white 	: tuple = (255,255,255)
	black 	: tuple = (0, 0, 0)
	sage 	: tuple = (85, 88, 67)
	maroon	: tuple = (117, 14, 33)
	orange	: tuple = (227, 101, 29)
	green	: tuple = (190, 215, 84)