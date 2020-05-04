from models.Road import Road
from models.Grass import Grass
from models.House import House
from models.Trash import Trash
from config import MAP_HEIGHT, MAP_WIDTH, MAP


def __render_element__(__x__, __y__):
    item = MAP[__y__][__x__]
    if item == "Road":
        return Road(__x__, __y__)
    if item == "Grass":
        return Grass(__x__, __y__)
    if item == "House":
        return House(__x__, __y__)

    return Trash(__x__, __y__, item)


def is_within_width(item):
    return item[0] >= 0 and item[0] < MAP_WIDTH


def is_within_height(item):
    return item[1] >= 0 and item[1] < MAP_HEIGHT
