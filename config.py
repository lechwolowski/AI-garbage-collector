from platform import system
CELL_SIZE = 64
WINDOW_HEIGHT = 10 * CELL_SIZE
WINDOW_WIDTH = 16 * CELL_SIZE
MAP_HEIGHT = 10
MAP_WIDTH = 16
if system() == "Windows":
    FONT = "arial.ttf"
elif system() == "Darwin":
    FONT = "FiraCode-Bold.otf"

BLACK = (0, 0, 0)
BLUE = (0, 77, 147)
GREEN = (11, 131, 44)
YELLOW = (224, 125, 16)

HOUSE_IMAGE = "house.jpg"
TRASH_GLASS_IMAGE = "trash-glass.png"
TRASH_MIXED_IMAGE = "trash-mixed.png"
TRASH_PAPER_IMAGE = "trash-paper.png"
TRASH_PLASTIC_IMAGE = "trash-plastic.png"
GARBAGE_COLLECTOR_IMAGE = "garbage-collector.png"

MAP = {
    0: {0: "Glass", 1: "Road", 2: "Road", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "House",
        8: "Road", 9: "House", 10: "House", 11: "Road", 12: "Road", 13: "Road", 14: "Road", 15: "Paper"},
    1: {0: "Grass", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "House",
        8: "Road", 9: "House", 10: "House", 11: "Road", 12: "House", 13: "House", 14: "Road", 15: "Grass"},
    2: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "Road", 5: "Road", 6: "Road", 7: "House",
        8: "Road", 9: "House", 10: "House", 11: "Road", 12: "House", 13: "House", 14: "Road", 15: "House"},
    3: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "Road",
        8: "Road", 9: "Road", 10: "Road", 11: "Road", 12: "Road", 13: "Road", 14: "Road", 15: "House"},
    4: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "Grass",
        8: "Grass", 9: "Grass", 10: "Grass", 11: "Road", 12: "Grass", 13: "Grass", 14: "Road", 15: "House"},
    5: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "Grass",
        8: "Grass", 9: "Grass", 10: "Grass", 11: "Road", 12: "Grass", 13: "Grass", 14: "Road", 15: "House"},
    6: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "Road",
        8: "Road", 9: "Road", 10: "Road", 11: "Road", 12: "Road", 13: "Road", 14: "Road", 15: "House"},
    7: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "Road", 5: "Road", 6: "Road", 7: "House",
        8: "Road", 9: "House", 10: "House", 11: "Road", 12: "House", 13: "House", 14: "Road", 15: "House"},
    8: {0: "Grass", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "House",
        8: "Road", 9: "House", 10: "House", 11: "Road", 12: "House", 13: "House", 14: "Road", 15: "Grass"},
    9: {0: "Mixed", 1: "Road", 2: "Road", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "House",
        8: "Road", 9: "House", 10: "House", 11: "Road", 12: "Road", 13: "Road", 14: "Road", 15: "Plastic"},
}
