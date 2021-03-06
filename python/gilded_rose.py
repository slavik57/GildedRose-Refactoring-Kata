# -*- coding: utf-8 -*-
from aging.item_aging import ItemAging
from aging.item_improver import ItemImprover

MAX_ITEM_QUALITY = 50

class GildedRose(object):

    def __init__(self, items):
        self.item_agers = [self.to_item_aging(item) for item in items]

    def to_item_aging(self, item):
        if GildedRose.is_quality_increasing_item(item):
            return ItemImprover(item)
        return ItemAging(item)

    def update_quality(self):
        for item_aging in self.item_agers:
            self.update_item_quality(item_aging.item, item_aging)

    @staticmethod
    def is_quality_increasing_item(item):
        return item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert"

    def update_item_quality(self, item, item_aging):
        if self.is_quality_increasing_item(item):
            item_aging.increase_item_quality()
        elif item.name != "Sulfuras, Hand of Ragnaros":
            item_aging.age_item_by_day()
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            self.update_after_sell_in_date(item)

    @staticmethod
    def update_after_sell_in_date(item):
        if item.name != "Aged Brie":
            if item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                item.quality = item.quality - item.quality
        else:
            if item.quality < MAX_ITEM_QUALITY:
                item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


