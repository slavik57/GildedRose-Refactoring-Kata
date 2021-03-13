import unittest

from parameterized import parameterized_class

import gilded_rose
import gilded_rose_functional
from items.Conjured import Conjured


@parameterized_class([
    {"gilded_rose_factory": gilded_rose.GildedRose, "name": "OOP"},
    {"gilded_rose_factory": gilded_rose_functional.GildedRose, "name": "FP"}
])
class ConjuredTest(unittest.TestCase):
    def setUp(self) -> None:
        self.initial_sell_in = 16
        self.initial_quality = 30

        self.conjured = Conjured(sell_in=self.initial_sell_in, quality=self.initial_quality)
        self.conjured_zero_sell_in = Conjured(sell_in=0, quality=self.initial_quality)

        self.items = [
            self.conjured,
            self.conjured_zero_sell_in
        ]

        gilded_rose = self.gilded_rose_factory(self.items)
        gilded_rose.update_quality()

    def test_conjured_item_quality(self):
        self.assertEqual(self.conjured.sell_in, self.initial_sell_in - 1)
        self.assertEqual(self.conjured.quality, self.initial_quality - 2)

        self.assertEqual(self.conjured_zero_sell_in.sell_in, -1)
        self.assertEqual(self.conjured_zero_sell_in.quality, self.initial_quality - 4)
