# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item
from items.Conjured import Conjured
from items.aged_brie import AgedBrie
from items.backstage_passes import BackstagePasses
from items.sulfuras import Sulfuras


class RegularItemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.initial_sell_in = 16
        self.initial_quality = 30

        self.item = Item("Some item", sell_in=self.initial_sell_in, quality=self.initial_quality)
        self.item_with_zero_quality = Item("Zero quality item", sell_in=self.initial_sell_in, quality=0)
        self.item_with_zero_sell_in = Item("Zero sell in", sell_in=0, quality=self.initial_quality)

        self.items = [
            self.item,
            self.item_with_zero_quality,
            self.item_with_zero_sell_in
        ]

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_item_lowers_sell_in_and_quality(self):
        self.assertEqual(self.item.sell_in, self.initial_sell_in - 1)
        self.assertEqual(self.item.quality, self.initial_quality - 1)

    def test_quality_is_not_negative(self):
        self.assertEqual(self.item_with_zero_quality.quality, 0)

    def test_item_quality_degrades_by_2_after_sell_in(self):
        self.assertEqual(self.item_with_zero_sell_in.sell_in, -1)
        self.assertEqual(self.item_with_zero_sell_in.quality, self.initial_quality - 2)


class SulfrasTest(unittest.TestCase):
    def setUp(self) -> None:
        self.initial_sell_in = 16
        self.initial_quality = 30

        self.sulfuras = Sulfuras()

        self.items = [self.sulfuras]

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_sulfuras_does_not_change(self):
        self.assertEqual(Sulfuras().quality, 80)
        self.assertEqual(self.sulfuras.sell_in, Sulfuras().sell_in)
        self.assertEqual(self.sulfuras.quality, Sulfuras().quality)


class GildedRoseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.initial_sell_in = 16
        self.current_sell_in = self.initial_sell_in
        self.initial_quality = 30

        self.aged_brie = AgedBrie(sell_in=self.initial_sell_in, quality=self.initial_quality)
        self.max_quality = AgedBrie(sell_in=self.initial_sell_in, quality=50)
        self.backstage_passes = BackstagePasses(sell_in=self.initial_sell_in, quality=self.initial_quality)
        self.conjured = Conjured(sell_in=self.initial_sell_in, quality=self.initial_quality)

        self.items = [
            self.aged_brie,
            self.max_quality,
            self.backstage_passes,
            self.conjured
        ]

        self.gilded_rose = GildedRose(self.items)
        self.update_until_sell_in_is(self.initial_sell_in - 1)

    def update_until_sell_in_is(self, target_sell_in):
        while self.current_sell_in > target_sell_in:
            self.gilded_rose.update_quality()
            self.current_sell_in -= 1

    def test_aged_brie_quality_goes_up(self):
        self.assertEqual(self.aged_brie.quality, self.initial_quality + 1)

    def test_quality_is_limited(self):
        self.assertEqual(self.max_quality.quality, 50)

    def test_backstage_passes(self):
        self.assertEqual(self.backstage_passes.sell_in, self.initial_sell_in - 1)
        self.assertEqual(self.backstage_passes.quality, self.initial_quality + 1)

    def test_backstage_passes_with_10_left_days(self):
        self.update_until_sell_in_is(10)
        current_quality = self.backstage_passes.quality
        self.update_until_sell_in_is(9)

        self.assertEqual(self.backstage_passes.sell_in, 9)
        self.assertEqual(self.backstage_passes.quality, current_quality + 2)

    def test_backstage_passes_with_5_left_days(self):
        self.update_until_sell_in_is(5)
        current_quality = self.backstage_passes.quality
        self.update_until_sell_in_is(4)

        self.assertEqual(self.backstage_passes.sell_in, 4)
        self.assertEqual(self.backstage_passes.quality, current_quality + 3)

    def test_backstage_passes_concert_is_over(self):
        self.update_until_sell_in_is(0)
        self.assertGreater(self.backstage_passes.quality, 0)
        self.update_until_sell_in_is(-1)

        self.assertEqual(self.backstage_passes.sell_in, -1)
        self.assertEqual(self.backstage_passes.quality, 0)

    def test_backstage_passes_max_quality(self):
        self.update_until_sell_in_is(1)
        self.assertEqual(self.backstage_passes.quality, 50)

        self.update_until_sell_in_is(0)
        self.assertEqual(self.backstage_passes.quality, 50)

    def test_aged_brie_max_quality(self):
        self.update_until_sell_in_is(-10)
        self.assertEqual(self.aged_brie.quality, 50)

        self.update_until_sell_in_is(-11)
        self.assertEqual(self.aged_brie.quality, 50)

    def test_conjured_item_quality(self):
        self.conjured.quality = 10
        self.conjured.sell_in = 1

        self.gilded_rose.update_quality()
        self.assertEqual(self.conjured.sell_in, 0)
        self.assertEqual(self.conjured.quality, 8)

        self.gilded_rose.update_quality()
        self.assertEqual(self.conjured.sell_in, -1)
        self.assertEqual(self.conjured.quality, 4)


if __name__ == '__main__':
    unittest.main()
