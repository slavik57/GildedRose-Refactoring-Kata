# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from items.sulfuras import Sulfuras


class GildedRoseTest(unittest.TestCase):
    def test_sulfuras_does_not_decrease_quality(self):
        items = [Sulfuras()]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0], Sulfuras())

        
if __name__ == '__main__':
    unittest.main()
