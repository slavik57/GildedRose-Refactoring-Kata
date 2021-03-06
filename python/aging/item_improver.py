from aging.item_aging import ItemAging

MAX_ITEM_QUALITY = 50


class ItemImprover(ItemAging):
    def __init__(self, item):
        super(ItemImprover, self).__init__(item)

    def increase_item_quality(self):
        if self.item.name == "Backstage passes to a TAFKAL80ETC concert":
            self._increase_backstage_passes_quality()
        else:
            self._increase_quality_by(1)

    def _increase_backstage_passes_quality(self):
        if self.item.sell_in < 6:
            self._increase_quality_by(3)
        elif self.item.sell_in < 11:
            self._increase_quality_by(2)
        else:
            self._increase_quality_by(1)

    def _increase_quality_by(self, quality_to_add):
        self.item.quality = min(self.item.quality + quality_to_add, MAX_ITEM_QUALITY)
