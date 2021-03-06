class ItemAging:
    def __init__(self, item):
        self.item = item

    def age_item_by_day(self):
        self._update_quality()

    def _update_quality(self):
        if self.item.quality > 0:
            self.item.quality = self.item.quality - 1
