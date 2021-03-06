# -*- coding: utf-8 -*-
from aging.backstage_pass_improver import BackstagePassImprover
from aging.item_aging import ItemAging
from aging.item_improver import ItemImprover
from aging.sulfuras_aging import SulfurasAging

agers_factories = {
    "Sulfuras, Hand of Ragnaros": SulfurasAging,
    "Backstage passes to a TAFKAL80ETC concert": BackstagePassImprover,
    "Aged Brie": ItemImprover
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


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
