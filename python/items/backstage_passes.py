from gilded_rose import Item


class BackstagePasses(Item):
    def __init__(self, sell_in=16, quality=4):
        super(BackstagePasses, self).__init__(
            "Backstage passes to a TAFKAL80ETC concert", sell_in=sell_in, quality=quality)