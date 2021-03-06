# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class Sulfuras(Item):
    def __init__(self):
        super(Sulfuras, self).__init__("Sulfuras, Hand of Ragnaros", sell_in=10, quality=50)
    def __eq__(self, other):
        return self.quality == other.quality and self.sell_in == other.sell_in


class GildedRoseTest(unittest.TestCase):
    def test_sulfuras_does_not_decrease_quality(self):
        items = [Sulfuras()]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0], Sulfuras())

        
if __name__ == '__main__':
    unittest.main()
