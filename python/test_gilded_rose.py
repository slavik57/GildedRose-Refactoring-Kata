# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item
from items.sulfuras import Sulfuras


class GildedRoseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.item = Item("Some item", sell_in=10, quality=4)
        self.sulfuras = Sulfuras()
        self.item_with_zero_quality = Item("Zero quality item", sell_in=10, quality=0)
        self.aged_brie = Item("Aged Brie", sell_in=10, quality=11)

        self.items = [
            self.item,
            self.sulfuras,
            self.item_with_zero_quality,
            self.aged_brie
        ]

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_sulfuras_does_not_decrease_quality(self):
        self.assertEquals(self.sulfuras, Sulfuras())

    def test_item_lowers_sell_in_and_quality(self):
        self.assertEquals(self.item.sell_in, 9)
        self.assertEquals(self.item.quality, 3)

    def test_quality_is_not_negative(self):
        self.assertEquals(self.item_with_zero_quality.quality, 0)

    def test_aged_brie_quality_goes_up(self):
        self.assertEquals(self.aged_brie.quality, 12)

if __name__ == '__main__':
    unittest.main()
