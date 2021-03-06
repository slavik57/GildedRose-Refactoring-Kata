from aging.item_aging import ItemAging

MAX_ITEM_QUALITY = 50


class ItemImprover(ItemAging):
    def __init__(self, item):
        super(ItemImprover, self).__init__(item)

    def increase_item_quality(self):
        self._increase_quality_by(1)

    def _increase_quality_by(self, quality_to_add):
        self.item.quality = min(self.item.quality + quality_to_add, MAX_ITEM_QUALITY)

