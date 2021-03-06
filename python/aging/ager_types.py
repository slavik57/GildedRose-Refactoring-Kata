from typing import Callable

from items import Item

OneDayAger = Callable[[], None]
OneDayAgerFactory = Callable[[Item], OneDayAger]
ItemUpdater = Callable[[Item], None]

MAX_ITEM_QUALITY = 50
