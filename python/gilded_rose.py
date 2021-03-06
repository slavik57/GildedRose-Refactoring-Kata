# -*- coding: utf-8 -*-
from aging.backstage_pass_improver import BackstagePassImprover
from aging.item_aging import ItemAging
from aging.item_improver import ItemImprover
from aging.sulfuras_aging import SulfurasAging

MAX_ITEM_QUALITY = 50


class GildedRose(object):

    def __init__(self, items):
        self.item_agers = [self.to_item_aging(item) for item in items]

    @staticmethod
    def to_item_aging(item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasAging(item)
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassImprover(item)
        if item.name == "Aged Brie":
            return ItemImprover(item)
        return ItemAging(item)

    def update_quality(self):
        for item_aging in self.item_agers:
            self.update_item_quality(item_aging.item, item_aging)

    def update_item_quality(self, item, item_aging):
        item_aging.age_item_by_day()
        if item.sell_in < 0:
            self.update_after_sell_in_date(item, item_aging)

    @staticmethod
    def update_after_sell_in_date(item, item_aging):
        if item.name == "Aged Brie":
            if item.quality < MAX_ITEM_QUALITY:
                item.quality = item.quality + 1
        else:
            if item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.name != "Sulfuras, Hand of Ragnaros":
                    if item.quality > 0:
                        item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
