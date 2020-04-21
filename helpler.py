from config import MAP
from models.Road import Road
from models.Grass import Grass
from models.House import House
from config import MAP_HEIGHT, MAP_WIDTH
from models.Trash import Trash


def Render_Element(x, y):
    item = MAP[y][x]
    if item == "Road":
        return Road(x, y)
    elif item == "Grass":
        return Grass(x, y)
    elif item == "House":
        return House(x, y)
    else:
        return Trash(x, y, item)


def is_within_width(item): return item[0] >= 0 and item[0] < MAP_WIDTH
def is_within_height(item): return item[1] >= 0 and item[1] < MAP_HEIGHT
