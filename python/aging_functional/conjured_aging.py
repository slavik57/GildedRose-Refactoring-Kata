from aging import OneDayAger
from .item_aging import reduce_quality_by, age_item, AgingStrategy


def age_item_by_day(item) -> OneDayAger:
    return lambda: age_item(
        item=item,
        strategy=AgingStrategy(before_sell_in=reduce_quality_by(2),
                               after_sell_in=reduce_quality_by(4))
    )
