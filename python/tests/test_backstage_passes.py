import unittest

from parameterized import parameterized_class

from gilded_rose import GildedRose
from items.backstage_passes import BackstagePasses

@parameterized_class([
    {"gilded_rose_factory": GildedRose, "name": "OOP"}
])
class BackstagePassesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.initial_sell_in = 16
        self.initial_quality = 30

        self.backstage_passes = BackstagePasses(sell_in=self.initial_sell_in, quality=self.initial_quality)
        self.backstage_passes_sell_in_10 = BackstagePasses(sell_in=10, quality=self.initial_quality)
        self.backstage_passes_sell_in_5 = BackstagePasses(sell_in=5, quality=self.initial_quality)
        self.backstage_passes_sell_in_0 = BackstagePasses(sell_in=0, quality=self.initial_quality)
        self.max_quality = BackstagePasses(sell_in=self.initial_sell_in, quality=50)

        self.items = [
            self.backstage_passes,
            self.backstage_passes_sell_in_10,
            self.backstage_passes_sell_in_5,
            self.backstage_passes_sell_in_0,
            self.max_quality
        ]

        self.gilded_rose = self.gilded_rose_factory(self.items)
        self.gilded_rose.update_quality()

    def test_backstage_passes(self):
        self.assertEqual(self.backstage_passes.sell_in, self.initial_sell_in - 1)
        self.assertEqual(self.backstage_passes.quality, self.initial_quality + 1)

    def test_backstage_passes_with_10_left_days(self):
        self.assertEqual(self.backstage_passes_sell_in_10.sell_in, 9)
        self.assertEqual(self.backstage_passes_sell_in_10.quality, self.initial_quality + 2)

    def test_backstage_passes_with_5_left_days(self):
        self.assertEqual(self.backstage_passes_sell_in_5.sell_in, 4)
        self.assertEqual(self.backstage_passes_sell_in_5.quality, self.initial_quality + 3)

    def test_backstage_passes_concert_is_over(self):
        self.assertEqual(self.backstage_passes_sell_in_0.sell_in, -1)
        self.assertEqual(self.backstage_passes_sell_in_0.quality, 0)

    def test_backstage_passes_max_quality(self):
        self.assertEqual(self.max_quality.quality, 50)