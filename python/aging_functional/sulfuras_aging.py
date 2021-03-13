from items import Item
from .item_aging import age_item, AgingStrategy
from aging import OneDayAger


def age_item_by_day(item: Item) -> OneDayAger:
    def do_nothing(_item: Item): pass

    return lambda: age_item(
        item=item,
        strategy=AgingStrategy(before_sell_in=do_nothing,
                               update_sell_in=do_nothing,
                               after_sell_in=do_nothing)
    )
