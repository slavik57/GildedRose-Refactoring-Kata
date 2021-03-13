from items.item import Item
from .ager_types import OneDayAger, ItemUpdater


class ItemAging:
    def __init__(self, item):
        self.item = item

    def age_item_by_day(self):
        self._update_sell_in()

        if self.item.sell_in < 0:
            self._update_quality_after_sell_in()
        else:
            self._update_quality_before_sell_in()

    def _update_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1

    def _update_quality_before_sell_in(self):
        self._reduce_quality_by(1)

    def _update_quality_after_sell_in(self):
        self._reduce_quality_by(2)

    def _reduce_quality_by(self, amount):
        self.item.quality = max(0, self.item.quality - amount)


def age_item_by_day(item: Item) -> OneDayAger:
    return lambda: age_item(
        item=item,
        before_sell_in=_update_quality_before_sell_in,
        after_sell_in=_update_quality_after_sell_in
    )


def _update_sell_in(item: Item) -> None:
    item.sell_in = item.sell_in - 1


def age_item(
        item: Item,
        before_sell_in: ItemUpdater,
        after_sell_in: ItemUpdater,
        update_sell_in: ItemUpdater = _update_sell_in
):
    update_sell_in(item)

    if item.sell_in < 0:
        after_sell_in(item)
    else:
        before_sell_in(item)


def _update_quality_before_sell_in(item: Item) -> None:
    reduce_quality_by(item, 1)


def _update_quality_after_sell_in(item: Item) -> None:
    reduce_quality_by(item, 2)


def reduce_quality_by(item: Item, amount: int) -> None:
    item.quality = max(0, item.quality - amount)
