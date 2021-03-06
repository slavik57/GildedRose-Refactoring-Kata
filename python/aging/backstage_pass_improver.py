from aging.item_improver import ItemImprover


class BackstagePassImprover(ItemImprover):
    def __init__(self, item):
        super(BackstagePassImprover, self).__init__(item)

    def _update_quality_before_sell_in(self):
        if self.item.sell_in < 5:
            self._increase_quality_by(3)
        elif self.item.sell_in < 10:
            self._increase_quality_by(2)
        else:
            self._increase_quality_by(1)

    def _update_quality_after_sell_in(self):
        self.item.quality = 0
