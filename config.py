from platform import system
CELL_SIZE = 64
MAP_HEIGHT = 7
MAP_WIDTH = 9
WINDOW_HEIGHT = MAP_HEIGHT * CELL_SIZE
WINDOW_WIDTH = MAP_WIDTH * CELL_SIZE
FONT = "./Resources/JetBrainsMono-Regular.ttf"
BLACK = (0, 0, 0)
BLUE = (0, 77, 147)
GREEN = (11, 131, 44)
YELLOW = (224, 125, 16)

TRASH_TYPES = ["mixed", "paper", "glass", "plastic"]

HOUSE_IMAGE = "house.png"
TRASH_GLASS_IMAGE = "trash-glass.png"
TRASH_MIXED_IMAGE = "trash-mixed.png"
TRASH_PAPER_IMAGE = "trash-paper.png"
TRASH_PLASTIC_IMAGE = "trash-plastic.png"
GARBAGE_COLLECTOR_IMAGE = "garbage-collector.png"

MAP = {
    0: {0: "Glass", 1: "Road", 2: "Road", 3: "Road", 4: "Grass", 5: "Road", 6: "Road", 7: "Road", 8: "Paper"},
    1: {0: "Grass", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "Road", 6: "Grass", 7: "Road", 8: "Grass"},
    2: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "Road", 5: "Road", 6: "Grass", 7: "Road", 8: "House"},
    3: {0: "Grass", 1: "Road", 2: "Road", 3: "Road", 4: "Grass", 5: "Road", 6: "Road", 7: "Road", 8: "Grass"},
    4: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "Road", 5: "Road", 6: "Grass", 7: "Road", 8: "House"},
    5: {0: "Grass", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "Road", 6: "Grass", 7: "Road", 8: "Grass"},
    6: {0: "Mixed", 1: "Road", 2: "Road", 3: "Road", 4: "Grass", 5: "Road", 6: "Road", 7: "Road", 8: "Plastic"},
}
