from gilded_rose import Item


class Sulfuras(Item):
    def __init__(self):
        super(Sulfuras, self).__init__("Sulfuras, Hand of Ragnaros", sell_in=10, quality=50)
    def __eq__(self, other):
        return self.quality == other.quality and self.sell_in == other.sell_in