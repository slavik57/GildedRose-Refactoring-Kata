from .item import Item


class AgedBrie(Item):
    def __init__(self, sell_in, quality):
        super(AgedBrie, self).__init__("Aged Brie", sell_in=sell_in, quality=quality)