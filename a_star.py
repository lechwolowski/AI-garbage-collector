from models.House import House


class A_Star:
    def __init__(self, draw_items, gc):
        super().__init__()
        self.draw_items, self.gc = draw_items, gc
        self.houses = list(map(lambda item: self.draw_items[item], list(filter(lambda item: isinstance(
            self.draw_items[item], House), self.draw_items))))

    def houses_with_trash(self):
        houses = list(map(lambda item: self.draw_items[item], list(filter(lambda item: isinstance(
            self.draw_items[item], House), self.draw_items))))
        trash_types = ["mixed", "paper", "glass", "plastic"]
        # houses = filter(lambda house: (lambda trash_type: getattr(
        #     house, trash_type) > 5, trash_types), houses)
        # houses = filter(lambda house: getattr(house, "mixed") > 5, houses)
        filtered_houses = []
        for house in houses:
            empty = True
            for trash_type in trash_types:
                if getattr(house, trash_type) > 0:
                    empty = False
            print(empty, house.col, house.row)
            if not empty:
                filtered_houses.append(house)
        for house in filtered_houses:
            print("col:", house.col, "row:", house.row)
        print('\n')
        # trash quantity/distance
