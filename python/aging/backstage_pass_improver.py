from aging.item_improver import ItemImprover


class BackstagePassImprover(ItemImprover):
    def __init__(self, item):
        super(BackstagePassImprover, self).__init__(item)

    def age_item_by_day(self):
        if self.item.sell_in < 6:
            self._increase_quality_by(3)
        elif self.item.sell_in < 11:
            self._increase_quality_by(2)
        else:
            self._increase_quality_by(1)