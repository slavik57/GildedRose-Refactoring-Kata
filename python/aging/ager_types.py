from typing import Callable

from items.item import Item

OneDayAger = Callable[[], None]
OneDayAgerFactory = Callable[[Item], OneDayAger]
ItemUpdater = Callable[[Item], None]


class AgingStrategy:
    def __init__(self,
                 update_sell_in: ItemUpdater = None,
                 before_sell_in: ItemUpdater = None,
                 after_sell_in: ItemUpdater = None):
        self.update_sell_in = update_sell_in
        self.before_sell_in = before_sell_in
        self.after_sell_in = after_sell_in
