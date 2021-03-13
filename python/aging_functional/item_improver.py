from aging import MAX_ITEM_QUALITY, OneDayAger, ItemUpdater
from items.item import Item

from .item_aging import age_item, AgingStrategy


def age_item_by_day(item) -> OneDayAger:
    return lambda: age_item(
        item=item,
        strategy=AgingStrategy(before_sell_in=increase_quality_by(1),
                               after_sell_in=increase_quality_by(2))
    )


def increase_quality_by(amount: int) -> ItemUpdater:
    def increase_item_quality(item: Item) -> None:
        item.quality = min(item.quality + amount, MAX_ITEM_QUALITY)

    return increase_item_quality
