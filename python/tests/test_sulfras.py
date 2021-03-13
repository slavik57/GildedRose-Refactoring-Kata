import unittest

from parameterized import parameterized_class

from gilded_rose import GildedRose
from items.sulfuras import Sulfuras


@parameterized_class([
    {"gilded_rose_factory": GildedRose, "name": "OOP"}
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
