########## Sabareesh Vishwanathan ##########
########## 112585006 #############
########## SAVISHWANATH #############
import time
import unittest
from threading import Thread

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

    def test_create_deck_and_admiral(self):
        # deckie = Deck()
        deck = Deck().get_instance()
        for i in range(0, 25):
            self.assertTrue(isinstance(deck.cards[i], MerchantShip), 'Object is not of type MerchantShip')
        for i in range(25, 73):
            self.assertTrue(isinstance(deck.cards[i], PirateShip), 'Object is not of type PirateShip')
        for i in range(73, 77):
            self.assertTrue(isinstance(deck.cards[i], Captain), 'Object is not of type Captain')
        self.assertTrue(isinstance(deck.cards[77], Admiral), 'Object is not of type Admiral')
        with self.assertRaises(RuntimeError) as cm:
            Deck()
        self.assertEqual('Singleton', str(cm.exception))

    # def test_create_admiral(self):
    #     admiral = Admiral().get_instance()
    #     self.assertTrue(isinstance(admiral, Admiral), "Object is not of type Admiral")
    #     with self.assertRaises(RuntimeError) as cm:
    #         Admiral()
    #     self.assertEqual('Singleton', str(cm.exception))



















