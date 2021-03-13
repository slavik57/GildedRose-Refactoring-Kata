from .ager_types import OneDayAger
from .item_aging import ItemAging


class ConjuredAging(ItemAging):
    def __init__(self, item):
        super().__init__(item)

    def _update_quality_before_sell_in(self):
        self._reduce_quality_by(2)

    def _update_quality_after_sell_in(self):
        self._reduce_quality_by(4)


def age_item_by_day(item) -> OneDayAger:
    item_aging = ConjuredAging(item)
    return lambda: item_aging.age_item_by_day()
