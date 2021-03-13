from items.item import Item
from .item_aging import ItemAging, age_item
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


def age_item_by_day(item: Item) -> OneDayAger:
    def noop(_item: Item): pass

    return lambda: age_item(
        item=item,
        before_sell_in=noop,
        update_sell_in=noop,
        after_sell_in=noop
    )
