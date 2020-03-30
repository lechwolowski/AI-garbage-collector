from config import MAP
from models.Road import Road
from models.Grass import Grass
from models.House import House
from models.Trash_Glass import Trash_Glass
from models.Trash_Paper import Trash_Paper
from models.Trash_Plastic import Trash_Plastic


def Render_Element(x, y):
    item = MAP[y][x]
    if item == "Road":
        return Road(x, y)
    elif item == "Grass":
        return Grass(x, y)
    elif item == "House":
        return House(x, y)
    elif item == "Glass":
        return Trash_Glass(x, y)
    elif item == "Paper":
        return Trash_Paper(x, y)
    elif item == "Plastic":
        return Trash_Plastic(x, y)
