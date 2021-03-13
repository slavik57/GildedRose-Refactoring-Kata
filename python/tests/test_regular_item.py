import unittest

from parameterized import parameterized_class

import gilded_rose
import gilded_rose_functional
from gilded_rose import Item


@parameterized_class([
    {"gilded_rose_factory": gilded_rose.GildedRose, "name": "OOP"},
    {"gilded_rose_factory": gilded_rose_functional.GildedRose, "name": "FP"}
])
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

        gilded_rose = self.gilded_rose_factory(self.items)
        gilded_rose.update_quality()

    def test_item_lowers_sell_in_and_quality(self):
        self.assertEqual(self.item.sell_in, self.initial_sell_in - 1)
        self.assertEqual(self.item.quality, self.initial_quality - 1)

    def test_quality_is_not_negative(self):
        self.assertEqual(self.item_with_zero_quality.quality, 0)

    def test_item_quality_degrades_by_2_after_sell_in(self):
        self.assertEqual(self.item_with_zero_sell_in.sell_in, -1)
        self.assertEqual(self.item_with_zero_sell_in.quality, self.initial_quality - 2)
