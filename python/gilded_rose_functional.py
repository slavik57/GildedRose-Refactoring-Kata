# -*- coding: utf-8 -*-
from aging import OneDayAgerFactory, OneDayAger
from aging_functional import *
from typing import Dict, List

from items.item import Item

AGERS_FACTORIES: Dict[str, OneDayAgerFactory] = {
    "Sulfuras, Hand of Ragnaros": age_sulfuras_by_day,
    "Backstage passes to a TAFKAL80ETC concert": age_backstage_pass_by_day,
    "Aged Brie": improve_item_by_day,
    "Conjured": age_conjured_by_day
}


class GildedRose(object):

    def __init__(self, items: List[Item]):
        self.agers: List[OneDayAger] = [self._to_item_aging(item) for item in items]

    @staticmethod
    def _to_item_aging(item: Item) -> OneDayAger:
        if item.name in AGERS_FACTORIES:
            return AGERS_FACTORIES[item.name](item)

        return age_item_by_day(item)

    def update_quality(self):
        for ager in self.agers:
            ager()
