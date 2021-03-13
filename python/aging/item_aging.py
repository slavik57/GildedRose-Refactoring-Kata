from typing import List

from items.item import Item
from .ager_types import OneDayAger, ItemUpdater, AgingStrategy


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


def _update_sell_in(item: Item) -> None:
    item.sell_in = item.sell_in - 1


def _update_quality_before_sell_in(item: Item) -> None:
    reduce_quality_by(item, 1)


def _update_quality_after_sell_in(item: Item) -> None:
    reduce_quality_by(item, 2)


def age_item(item: Item, strategy: AgingStrategy) -> None:
    if strategy.update_sell_in is None:
        strategy.update_sell_in = _update_sell_in
    if strategy.before_sell_in is None:
        strategy.before_sell_in = _update_quality_before_sell_in
    if strategy.after_sell_in is None:
        strategy.after_sell_in = _update_quality_after_sell_in

    update_item(item=item,
                updaters=[
                    strategy.update_sell_in,
                    bind_aging_strategy(strategy)
                ])


def update_item(item: Item, updaters: List[ItemUpdater]) -> None:
    for updater in updaters:
        updater(item)


def bind_aging_strategy(strategy: AgingStrategy) -> None:
    def update(item: Item) -> None:
        if item.sell_in < 0:
            strategy.after_sell_in(item)
        else:
            strategy.before_sell_in(item)

    return update


def reduce_quality_by(item: Item, amount: int) -> None:
    item.quality = max(0, item.quality - amount)
