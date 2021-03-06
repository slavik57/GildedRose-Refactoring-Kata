import unittest

from gilded_rose import GildedRose
from items.aged_brie import AgedBrie


class AgedBrieTest(unittest.TestCase):
    def setUp(self) -> None:
        self.initial_sell_in = 16
        self.initial_quality = 30

        self.aged_brie = AgedBrie(sell_in=self.initial_sell_in, quality=self.initial_quality)
        self.max_quality = AgedBrie(sell_in=self.initial_sell_in, quality=50)

        self.items = [
            self.aged_brie,
            self.max_quality
        ]

        self.gilded_rose = GildedRose(self.items)
        self.gilded_rose.update_quality()

    def test_aged_brie_quality_goes_up(self):
        self.assertEqual(self.aged_brie.quality, self.initial_quality + 1)

    def test_quality_is_limited(self):
        self.assertEqual(self.max_quality.quality, 50)

    def test_aged_brie_max_quality(self):
        while self.max_quality.sell_in > -2:
            self.gilded_rose.update_quality()

        self.assertEqual(self.aged_brie.quality, 50)