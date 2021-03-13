from .item import Item


class Conjured(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Conjured", sell_in, quality)