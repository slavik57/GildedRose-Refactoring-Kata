from aging.item_aging import ItemAging


class SulfurasAging(ItemAging):
    def __init__(self, item):
        super(SulfurasAging, self).__init__(item)

    def _update_sell_in(self):
        pass

    def _update_quality(self):
        pass

    def update_after_sell_in_date(self):
        pass
