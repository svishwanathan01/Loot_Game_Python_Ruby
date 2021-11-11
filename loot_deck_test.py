########## Sabareesh Vishwanathan ##########
########## 112585006 #############
########## SAVISHWANATH #############

import unittest
from loot import *

class TestLootDeck(unittest.TestCase):
    def test_create_merchant_ship(self):
         merchant_ship = MerchantShip(2)
         self.assertEqual(2, merchant_ship.value, "Value doesn't match")
         self.assertNotEqual(0, merchant_ship.value, "Value matches")

    def test_create_pirate_ship(self):
        pirateShip = PirateShip('green', 2)
        self.assertEqual(2, pirateShip.attack_value, "Value doesn't match")
        self.assertNotEqual(0, pirateShip.attack_value, "Value matches")
        self.assertEqual('green', pirateShip.color, "Color doesn't match")
        self.assertNotEqual('blue', pirateShip.color, "Color matches")

    def test_create_captain(self):
        captain = Captain('green')
        self.assertEqual('green', captain.color, "Color doesn't match")
        self.assertNotEqual('blue', captain.color, "Color matches")



