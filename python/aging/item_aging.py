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
        strategy=AgingStrategy()
    )


def _reduce_sell_in_by(amount: int) -> ItemUpdater:
    def reduce_item_sell_in(item: Item) -> None:
        item.sell_in = item.sell_in - amount

    return reduce_item_sell_in


def reduce_quality_by(amount: int) -> ItemUpdater:
    def _reduce_item_quality_by(item: Item) -> None:
        item.quality = max(0, item.quality - amount)

    return _reduce_item_quality_by


class AgingStrategy:
    def __init__(self,
                 update_sell_in: ItemUpdater = _reduce_sell_in_by(1),
                 before_sell_in: ItemUpdater = reduce_quality_by(1),
                 after_sell_in: ItemUpdater = reduce_quality_by(2)):
        self.update_sell_in = update_sell_in
        self.before_sell_in = before_sell_in
        self.after_sell_in = after_sell_in


def age_item(item: Item, strategy: AgingStrategy) -> None:
    strategy.update_sell_in(item)

    if item.sell_in < 0:
        strategy.after_sell_in(item)
    else:
        strategy.before_sell_in(item)
