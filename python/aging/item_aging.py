class ItemAging:
    def __init__(self, item):
        self.item = item

    def age_item_by_day(self):
        self._update_quality()
        self._update_sell_in()

    def _update_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1

    def _update_quality(self):
        self._reduce_quality_by(1)

    def _reduce_quality_by(self, amount):
        self.item.quality = max(0, self.item.quality - amount)

    def update_after_sell_in_date(self):
        self._reduce_quality_by(1)
