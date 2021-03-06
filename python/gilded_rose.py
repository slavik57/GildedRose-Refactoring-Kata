# -*- coding: utf-8 -*-

MAX_ITEM_QUALITY = 50

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item_quality(item)

    @staticmethod
    def is_quality_increasing_item(item):
        return item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert"

    def update_item_quality(self, item):
        if self.is_quality_increasing_item(item):
            self.increase_item_quality(item)
        else:
            if item.name != "Sulfuras, Hand of Ragnaros":
                self.regular_item_decrease_quality(item)
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            self.update_after_sell_in_date(item)

    @staticmethod
    def increase_item_quality(item):
        if item.quality >= MAX_ITEM_QUALITY:
            return

        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            GildedRose.increase_backstage_passes_quality(item)
        else:
            item.quality = item.quality + 1

    @staticmethod
    def increase_backstage_passes_quality(item):
        if item.sell_in < 6:
            GildedRose.increase_quality_by(item, 3)
        elif item.sell_in < 11:
            GildedRose.increase_quality_by(item, 2)
        else:
            GildedRose.increase_quality_by(item, 1)

    @staticmethod
    def increase_quality_by(item, quality_to_add):
        item.quality = min(item.quality + quality_to_add, MAX_ITEM_QUALITY)

    @staticmethod
    def regular_item_decrease_quality(item):
        if item.quality > 0:
            item.quality = item.quality - 1

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


