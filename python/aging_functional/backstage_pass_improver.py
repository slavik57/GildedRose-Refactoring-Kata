from items.item import Item
from aging import OneDayAger, ItemUpdater
from .item_improver import increase_quality_by
from .item_aging import age_item, AgingStrategy


def age_item_by_day(item: Item) -> OneDayAger:
    return lambda: age_item(
        item=item,
        strategy=AgingStrategy(before_sell_in=_increase_quality_based_on_sell_in,
                               after_sell_in=_set_quality_to_0
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


def _set_quality_to_0(item: Item) -> None:
    item.quality = 0
