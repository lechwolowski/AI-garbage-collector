from models.House import House
from models.Trash import Trash


class Knowledge:
    def __init__(self, items, gc):
        self.num = items
        self.gc = gc
        self.houses = []
        self.trashes = {}
        for line in items:
            for item in line:
                if isinstance(item, House):
                    self.houses.append(item)
                elif isinstance(item, Trash):
                    print(item.trash_type)
                    self.trashes[item.trash_type] = item

    def show(self):
        print({"Trash": {"mixed": self.trashes["Mixed"].trash, "glass": self.trashes["Paper"].trash,
                         "paper": self.trashes["Glass"].trash, "plastic": self.trashes["Plastic"].trash}},
              {"Garbage Collector": {"mixed": self.gc.mixed, "glass": self.gc.glass,
                                     "paper": self.gc.paper, "plastic": self.gc.plastic}}
              )
