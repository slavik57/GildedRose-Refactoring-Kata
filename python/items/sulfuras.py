from .item import Item


class Sulfuras(Item):
    def __init__(self):
        super(Sulfuras, self).__init__("Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)
