from items.item import Item
from .ager_types import OneDayAger

from .item_aging import ItemAging, age_item, AgingStrategy

MAX_ITEM_QUALITY = 50


class ItemImprover(ItemAging):
    def __init__(self, item):
        super(ItemImprover, self).__init__(item)

    def _update_quality_before_sell_in(self):
        self._increase_quality_by(1)

    def _update_quality_after_sell_in(self):
        self._increase_quality_by(2)

    def _increase_quality_by(self, quality_to_add):
        self.item.quality = min(self.item.quality + quality_to_add, MAX_ITEM_QUALITY)


def age_item_by_day(item) -> OneDayAger:
    return lambda: age_item(
        item=item,
        strategy=AgingStrategy(before_sell_in=_update_quality_before_sell_in,
                               after_sell_in=_update_quality_after_sell_in)
    )


def _update_quality_before_sell_in(item: Item) -> None:
    increase_quality_by(item, 1)


def _update_quality_after_sell_in(item: Item) -> None:
    increase_quality_by(item, 2)


def increase_quality_by(item: Item, quality_to_add: int) -> None:
    item.quality = min(item.quality + quality_to_add, MAX_ITEM_QUALITY)
