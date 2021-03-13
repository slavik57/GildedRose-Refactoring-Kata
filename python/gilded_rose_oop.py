# -*- coding: utf-8 -*-
from aging_oop import *

agers_factories = {
    "Sulfuras, Hand of Ragnaros": SulfurasAging,
    "Backstage passes to a TAFKAL80ETC concert": BackstagePassImprover,
    "Aged Brie": ItemImprover,
    "Conjured": ConjuredAging
}


class GildedRose(object):

    def __init__(self, items):
        self.item_agers = [self.to_item_aging(item) for item in items]

    @staticmethod
    def to_item_aging(item):
        if item.name in agers_factories:
            return agers_factories[item.name](item)

        return ItemAging(item)

    def update_quality(self):
        for item_aging in self.item_agers:
            item_aging.age_item_by_day()
