from config import MAP
from models.Road import Road
from models.Grass import Grass
from models.House import House


def Render_Element(x, y):
    item = MAP[y][x]
    if item == "Road":
        return Road(x, y)
    elif item == "Grass":
        return Grass(x, y)
    elif item == "House":
        return House(x, y)
    elif item == "Factory":
        pass
