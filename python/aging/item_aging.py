class ItemAging:
    def __init__(self, item):
        self.item = item

    def age_item_by_day(self):
        self._update_quality()
        self._update_sell_in()

    def _update_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1

    def _update_quality(self):
        if self.item.quality > 0:
            self.item.quality = self.item.quality - 1
