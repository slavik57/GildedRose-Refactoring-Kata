from .item_aging import ItemAging
from .ager_types import OneDayAger


class SulfurasAging(ItemAging):
    def __init__(self, item):
        super(SulfurasAging, self).__init__(item)

    def _update_sell_in(self):
        pass

    def _update_quality_before_sell_in(self):
        pass

    def _update_quality_after_sell_in(self):
        pass


def age_item_by_day(item) -> OneDayAger:
    item_aging = SulfurasAging(item)
    return lambda: item_aging.age_item_by_day()
