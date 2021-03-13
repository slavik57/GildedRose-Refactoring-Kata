from aging import MAX_ITEM_QUALITY
from .item_aging import ItemAging


class ItemImprover(ItemAging):
    def __init__(self, item):
        super(ItemImprover, self).__init__(item)

    def _update_quality_before_sell_in(self):
        self._increase_quality_by(1)

    def _update_quality_after_sell_in(self):
        self._increase_quality_by(2)

    def _increase_quality_by(self, quality_to_add):
        self.item.quality = min(self.item.quality + quality_to_add, MAX_ITEM_QUALITY)
