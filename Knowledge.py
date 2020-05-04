# from models.House import House
# from models.Trash import Trash


# class Knowledge:
#     def __init__(self, draw_items, gc):
#         self.draw_items = draw_items
#         self.gc = gc
#         self.update()

#     def add_to_dict(self, item, quantity, trash_quantity_variable):
#         if quantity in trash_quantity_variable:
#             trash_quantity_variable[quantity].append(
#                 {"col": item.col, "row": item.row})
#         else:
#             trash_quantity_variable[quantity] = [
#                 {"col": item.col, "row": item.row}]

#     def update(self):
#         self.mixed_trash_quantity_houses = {}
#         self.paper_trash_quantity_houses = {}
#         self.glass_trash_quantity_houses = {}
#         self.plastic_trash_quantity_houses = {}
#         self.trashes = {}
#         for item in self.draw_items:

#             if isinstance(self.draw_items[item], House):
#                 if not self.draw_items[item].mixed and not self.draw_items[item].paper and not self.draw_items[item].glass and not self.draw_items[item].plastic:
#                     # print(self.draw_items[item].col, self.draw_items[item].row)
#                     pass
#                 if self.draw_items[item].mixed:
#                     self.add_to_dict(self.draw_items[item], self.draw_items[item].mixed,
#                                      self.mixed_trash_quantity_houses)
#                 if self.draw_items[item].paper:
#                     self.add_to_dict(self.draw_items[item], self.draw_items[item].paper,
#                                      self.paper_trash_quantity_houses)
#                 if self.draw_items[item].glass:
#                     self.add_to_dict(self.draw_items[item], self.draw_items[item].glass,
#                                      self.glass_trash_quantity_houses)
#                 if self.draw_items[item].plastic:
#                     self.add_to_dict(self.draw_items[item], self.draw_items[item].plastic,
#                                      self.plastic_trash_quantity_houses)
#             elif isinstance(self.draw_items[item], Trash):
#                 self.trashes[self.draw_items[item].trash_type] = {
#                     "col": self.draw_items[item].col, "row": self.draw_items[item].row, "trash": self.draw_items[item].trash}

#     def show(self):
#         print({"Trash": {"mixed": self.trashes["Mixed"], "glass": self.trashes["Paper"],
#                          "paper": self.trashes["Glass"], "plastic": self.trashes["Plastic"]}},
#               {"Garbage Collector": {"mixed": self.gc.mixed, "glass": self.gc.glass,
#                                      "paper": self.gc.paper, "plastic": self.gc.plastic}}
#               )
