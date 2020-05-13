from config import MAP_HEIGHT, MAP_WIDTH, MAP
from models.__house__ import House


def map2int(MAP, __y__, __x__):
    item = MAP[__y__][__x__]
    if item == "Road":
        return 1
    if item == "Grass":
        return 2
    if item == "House":
        return 3

    return 4  # trash


def part_map(MAP, draw_items, y, x):
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

    for x in range(MAP_HEIGHT-1):
        for y in range(MAP_WIDTH-1):
            object = draw_items[(y, x)]
            if type(object) == House:
                if object.is_empty():
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

        #print("tablicaY=", table)
    f.close
