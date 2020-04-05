from models.House import House
from models.Trash import Trash


class Knowledge:
    def __init__(self, draw_items, gc):
        self.draw_items = draw_items
        self.gc = gc
        self.update()

    def add_to_dict(self, item, quantity, trash_quantity_variable):
        if quantity in trash_quantity_variable:
            trash_quantity_variable[quantity].append(
                {"col": item.col, "row": item.row})
        else:
            trash_quantity_variable[quantity] = [
                {"col": item.col, "row": item.row}]

    def update(self):
        self.mixed_trash_quantity_houses = {}
        self.paper_trash_quantity_houses = {}
        self.glass_trash_quantity_houses = {}
        self.plastic_trash_quantity_houses = {}
        self.trashes = {}
        for line in self.draw_items:
            for item in line:
                if isinstance(item, House):
                    if not item.mixed and not item.paper and not item.glass and not item.plastic:
                        # print(item.col, item.row)
                        pass
                    if item.mixed:
                        self.add_to_dict(item, item.mixed,
                                         self.mixed_trash_quantity_houses)
                    if item.paper:
                        self.add_to_dict(item, item.paper,
                                         self.paper_trash_quantity_houses)
                    if item.glass:
                        self.add_to_dict(item, item.glass,
                                         self.glass_trash_quantity_houses)
                    if item.plastic:
                        self.add_to_dict(item, item.plastic,
                                         self.plastic_trash_quantity_houses)
                elif isinstance(item, Trash):
                    self.trashes[item.trash_type] = {
                        "col": item.col, "row": item.row, "trash": item.trash}

    def show(self):
        print({"Trash": {"mixed": self.trashes["Mixed"], "glass": self.trashes["Paper"],
                         "paper": self.trashes["Glass"], "plastic": self.trashes["Plastic"]}},
              {"Garbage Collector": {"mixed": self.gc.mixed, "glass": self.gc.glass,
                                     "paper": self.gc.paper, "plastic": self.gc.plastic}}
              )
