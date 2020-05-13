from config import MAP_HEIGHT, MAP_WIDTH, MAP


def map2int(MAP, __y__, __x__):
    item = MAP[__y__][__x__]
    if item == "Road":
        return 1
    if item == "Grass":
        return 2
    if item == "House":
        return 3

    return 4  # trash


def part_map(MAP, y, x):
    map_part = []
    coords = [
        [x-3, y-3], [x-2, y-3], [x-1, y-3], [x+0,
                                             y-3], [x+1, y-3], [x+2, y-3], [x+3, y-3],
        [x-3, y-2], [x-2, y-2], [x-1, y-2], [x+0,
                                             y-2], [x+1, y-2], [x+2, y-2], [x+3, y-2],
        [x-3, y-1], [x-2, y-1], [x-1, y-1], [x+0,
                                             y-1], [x+1, y-1], [x+2, y-1], [x+3, y-1],
        [x-3, y+0], [x-2, y+0], [x-1, y+0], [x+0,
                                             y+0], [x+1, y+0], [x+2, y+0], [x+3, y+0],
        [x-3, y+1], [x-2, y+1], [x-1, y+1], [x+0,
                                             y+1], [x+1, y+1], [x+2, y+1], [x+3, y+1],
        [x-3, y+2], [x-2, y+2], [x-1, y+2], [x+0,
                                             y+2], [x+1, y+2], [x+2, y+2], [x+3, y+2],
        [x-3, y+3], [x-2, y+3], [x-1, y+3], [x+0,
                                             y+3], [x+1, y+3], [x+2, y+3], [x+3, y+3]
    ]

    for coord in coords:
        if(0 <= coord[1] < MAP_HEIGHT and 0 <= coord[0] < MAP_WIDTH):
            map_part.append(map2int(MAP, coord[1], coord[0]))
        else:
            map_part.append(2)
    return map_part


def save_to_file(plik, lista):
    plik = open('learn.txt', 'a')
    for element in lista:
        plik.writelines(*str(element), end="\n")

    plik.close()
