# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item
from items.sulfuras import Sulfuras


class GildedRoseTest(unittest.TestCase):
    def test_sulfuras_does_not_decrease_quality(self):
        items = [Sulfuras()]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0], Sulfuras())

    def test_item_lowers_sell_in_and_quality(self):
        items = [Item("Some item", sell_in=10, quality=4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].sell_in, 9)
        self.assertEquals(items[0].quality, 3)

if __name__ == '__main__':
    unittest.main()
