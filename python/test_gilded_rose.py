# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item
from items.aged_brie import AgedBrie
from items.backstage_passes import BackstagePasses
from items.sulfuras import Sulfuras


class GildedRoseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.initial_sell_in = 16
        self.current_sell_in = self.initial_sell_in
        self.initial_quality = 20

        self.item = Item("Some item", sell_in=self.initial_sell_in, quality=self.initial_quality)
        self.sulfuras = Sulfuras()
        self.item_with_zero_quality = Item("Zero quality item", sell_in=self.initial_sell_in, quality=0)
        self.aged_brie = AgedBrie(sell_in=self.initial_sell_in, quality=self.initial_quality)
        self.max_quality = AgedBrie(sell_in=self.initial_sell_in, quality=50)
        self.backstage_passes = BackstagePasses(sell_in=self.initial_sell_in, quality=self.initial_quality)

        self.items = [
            self.item,
            self.sulfuras,
            self.item_with_zero_quality,
            self.aged_brie,
            self.max_quality,
            self.backstage_passes
        ]

        self.gilded_rose = GildedRose(self.items)
        self.update_until_sell_in_is(self.initial_sell_in - 1)

    def update_until_sell_in_is(self, target_sell_in):
        while self.current_sell_in > target_sell_in:
            self.gilded_rose.update_quality()
            self.current_sell_in -= 1

    def test_sulfuras_does_not_decrease_quality(self):
        self.assertEquals(self.sulfuras.sell_in, Sulfuras().sell_in)
        self.assertEquals(self.sulfuras.quality, Sulfuras().quality)

    def test_item_lowers_sell_in_and_quality(self):
        self.assertEquals(self.item.sell_in, self.initial_sell_in - 1)
        self.assertEquals(self.item.quality, self.initial_quality - 1)

    def test_quality_is_not_negative(self):
        self.assertEquals(self.item_with_zero_quality.quality, 0)

    def test_aged_brie_quality_goes_up(self):
        self.assertEquals(self.aged_brie.quality, self.initial_quality + 1)

    def test_quality_is_limited(self):
        self.assertEquals(self.max_quality.quality, 50)

    def test_backstage_passes(self):
        self.assertEquals(self.backstage_passes.sell_in, self.initial_sell_in - 1)
        self.assertEquals(self.backstage_passes.quality, self.initial_quality + 1)

    def test_backstage_passes_with_10_left_days(self):
        self.update_until_sell_in_is(10)
        current_quality = self.backstage_passes.quality
        self.update_until_sell_in_is(9)

        self.assertEquals(self.backstage_passes.sell_in, 9)
        self.assertEquals(self.backstage_passes.quality, current_quality + 2)

    def test_backstage_passes_with_5_left_days(self):
        self.update_until_sell_in_is(5)
        current_quality = self.backstage_passes.quality
        self.update_until_sell_in_is(4)

        self.assertEquals(self.backstage_passes.sell_in, 4)
        self.assertEquals(self.backstage_passes.quality, current_quality + 3)

    def test_backstage_passes_concert_is_over(self):
        self.update_until_sell_in_is(0)
        current_quality = self.backstage_passes.quality
        self.assertGreater(self.backstage_passes.quality, 0)
        self.gilded_rose.update_quality()

        self.assertEquals(self.backstage_passes.sell_in, -1)
        self.assertEquals(self.backstage_passes.quality, 0)


if __name__ == '__main__':
    unittest.main()
