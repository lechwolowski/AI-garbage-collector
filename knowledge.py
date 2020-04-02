from models.House import House
# from models.Trash_Glass import Trash_Glass
from models.Trash_Paper import Trash_Paper
from models.Trash_Plastic import Trash_Plastic
from models.Trash_Mixed import Trash_Mixed


class Knowledge:
    def __init__(self, items, gc):
        self.num = items
        self.gc = gc
        self.houses = []
        for line in items:
            for item in line:
                if isinstance(item, House):
                    self.houses.append(item)
                elif isinstance(item, Trash_Mixed):
                    print(item.trash)
                    self.Trash_Mixed = item
                elif isinstance(item, Trash_Paper):
                    print(item.trash)
                    self.Trash_Paper = item
                elif isinstance(item, Trash_Glass):
                    print(item.trash)
                    self.Trash_Glass = item
                elif isinstance(item, Trash_Plastic):
                    print(item.trash)
                    self.Trash_Plastic = item

    def show(self):
        print({"Trash": {"mixed": self.Trash_Mixed.trash, "glass": self.Trash_Glass.trash,
                         "paper": self.Trash_Paper.trash, "plastic": self.Trash_Plastic.trash}},
              {"Garbage Collector": {"mixed": self.gc.mixed, "glass": self.gc.glass,
                                     "paper": self.gc.paper, "plastic": self.gc.plastic}}
              )

        print(self.houses)
        for house in self.houses:
            print(house.mixed)

        # inst = Knowledge(5)

        # numb = inst

        # inst.update(2)

        # print(inst.num, numb.num)
