import unittest

from gilded_rose import GildedRose
from items.sulfuras import Sulfuras


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