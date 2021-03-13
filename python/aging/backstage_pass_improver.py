from items.item import Item
from .ager_types import OneDayAger, ItemUpdater
from .item_improver import ItemImprover, increase_quality_by
from .item_aging import age_item, AgingStrategy


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


def age_item_by_day(item: Item) -> OneDayAger:
    return lambda: age_item(
        item=item,
        strategy=AgingStrategy(before_sell_in=_increase_quality_based_on_sell_in,
                               after_sell_in=_set_zero_quality
                               )
    )


def _increase_quality_based_on_sell_in(item: Item) -> None:
    if item.sell_in < 5:
        increase_quality = increase_quality_by(3)
    elif item.sell_in < 10:
        increase_quality = increase_quality_by(2)
    else:
        increase_quality = increase_quality_by(1)

    increase_quality(item)


def _set_zero_quality(item: Item) -> None:
    item.quality = 0
