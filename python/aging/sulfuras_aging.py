from aging.item_aging import ItemAging


class SulfurasAging(ItemAging):
    def __init__(self, item):
        super(SulfurasAging, self).__init__(item)

    def age_item_by_day(self):
        pass
