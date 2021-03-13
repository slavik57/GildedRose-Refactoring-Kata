import unittest

from parameterized import parameterized_class

import gilded_rose_oop
import gilded_rose_functional
from items.sulfuras import Sulfuras


@parameterized_class([
    {"gilded_rose_factory": gilded_rose_oop.GildedRose, "name": "OOP"},
    {"gilded_rose_factory": gilded_rose_functional.GildedRose, "name": "FP"}
])
class SulfrasTest(unittest.TestCase):
    def setUp(self) -> None:
        self.initial_sell_in = 16
        self.initial_quality = 30

        self.sulfuras = Sulfuras()

        self.items = [self.sulfuras]

        gilded_rose = self.gilded_rose_factory(self.items)
        gilded_rose.update_quality()

    def test_sulfuras_does_not_change(self):
        self.assertEqual(Sulfuras().quality, 80)
        self.assertEqual(self.sulfuras.sell_in, Sulfuras().sell_in)
        self.assertEqual(self.sulfuras.quality, Sulfuras().quality)
