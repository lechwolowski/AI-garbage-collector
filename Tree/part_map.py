from config import MAP_HEIGHT, MAP_WIDTH, MAP
from models.__house__ import House
from models.__trash__ import Trash


def map2int(MAP, __y__, __x__):
    item = MAP[__y__][__x__]
    if item == "Road":
        return 1
    if item == "Grass":
        return 2
    if item == "House":
        return 3

    return 4  # trash


def part_map(MAP, draw_items, y, x, prev):

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

    map_part.append(prev)

    for coord in coords:
        if(0 <= coord[1] < MAP_HEIGHT and 0 <= coord[0] < MAP_WIDTH):
            map_part.append(map2int(MAP, coord[1], coord[0]))
        else:
            map_part.append(2)

    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
            objectt = draw_items[(x, y)]
            if type(objectt) == House:
                if objectt.plastic == 0:
                    map_part.append(0)
                else:
                    map_part.append(1)

                if objectt.mixed == 0:
                    map_part.append(0)
                else:
                    map_part.append(1)

                if objectt.glass == 0:
                    map_part.append(0)
                else:
                    map_part.append(1)

                if objectt.paper == 0:
                    map_part.append(0)
                else:
                    map_part.append(1)

    return map_part


def save_to_file(plik, lista):
    strList = []
    for row in lista:
        lista = [str(item) for item in row]
        strList.append(lista)
    plik = open('Xlearn.txt', 'a')
    for row in strList:
        list1 = [(item+" ") for item in row]
        plik.writelines(list1)
        plik.write('\n')

    plik.close()


def save_to_file_1(plik, lista):
    strList = []
    for i in lista:
        strList.append(str(i))
    plik = open('Ylearn.txt', 'a')
    list1 = [(item+" ") for item in strList]
    plik.writelines(list1)
    plik.write('\n')
    plik.close()


def read_table(table, file_name, param):
    f = open(file_name)
    if param == 0:
        for linia in f:
            table += [linia.split()]
        for x in range(len(table)):
            w = table[x]
            for y in range(len(w)):
                w[y] = int(w[y])

    elif param == 1:
        for linia in f:
            table += linia.split()
        for x in range(len(table)):
            table[x] = int(table[x])

    f.close

# y-row


def check_house_trash(x, y, draw_items):
    if y > 0 and y < 6:
        if (type(draw_items[(x-1, y)]) == House or type(draw_items[(x+1, y)]) == House or type(draw_items[(x, y-1)]) == House or type(draw_items[(x, y+1)]) == House or type(draw_items[(x-1, y)]) == Trash or type(draw_items[(x+1, y)]) == Trash or type(draw_items[(x, y-1)]) == Trash or type(draw_items[(x, y+1)]) == Trash):
            return True
        else:
            return False
    elif y == 0:
        if (type(draw_items[(x-1, y)]) == House or type(draw_items[(x+1, y)]) == House or type(draw_items[(x, y+1)]) == House or type(draw_items[(x-1, y)]) == Trash or type(draw_items[(x+1, y)]) == Trash or type(draw_items[(x, y+1)]) == Trash):
            return True
        else:
            return False
    elif y == 6:
        if (type(draw_items[(x-1, y)]) == House or type(draw_items[(x+1, y)]) == House or type(draw_items[(x, y-1)]) == House or type(draw_items[(x-1, y)]) == Trash or type(draw_items[(x+1, y)]) == Trash or type(draw_items[(x, y-1)]) == Trash):
            return True
        else:
            return False


def empty_houses(draw_items):
    sum = 0
    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
            objectt = draw_items[(x, y)]
            if type(objectt) == House:
                sum = sum+objectt.plastic+objectt.mixed+objectt.glass+objectt.paper
    return sum
