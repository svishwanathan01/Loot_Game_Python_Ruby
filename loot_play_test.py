########## Sabareesh Vishwanathan ##########
########## 112585006 #############
########## SAVISHWANATH #############

import unittest
from loot import *

class TestLootPlay(unittest.TestCase):
    def test_create_game(self):
        game = Game(Deck.get_instance())
        self.assertTrue(isinstance(game.deck, Deck), 'Object is not of type Deck')
        self.assertEqual([], game.players, 'Expected players to be empty')
        self.assertEqual(game.current_player, None, 'Expected current player to be None')

    def test_create_players(self):
        game = Game(Deck.get_instance())
        names = ['X', 'Y', 'Z', 'A', 'B', 'C']
        with self.assertRaises(RuntimeError):
            game.create_players(names)
        names = ['X']
        with self.assertRaises(RuntimeError):
            game.create_players(names)
        names = ['X', 'Y', 'Z']
        game.create_players(names)
        playerNames = []
        for player in game.players:
            playerNames.append(player.name)
        self.assertEqual(playerNames, names, 'Expected players to be empty')
        self.assertEqual(game.current_player, None, 'Expected current player to be None')

    def test_random_player(self):
        game = Game(Deck.get_instance())
        self.assertEqual(game.random_player(), None)
        names = ['X', 'Y', 'Z']
        game.create_players(names)
        players = game.players
        self.assertTrue(game.random_player() in players, 'Expected player to be in players')

    def test_start(self):
        game = Game(Deck.get_instance())
        self.assertEqual(game.random_player(), None)
        names = ['X', 'Y', 'Z']
        game.create_players(names)
        players = game.players
        players[0].dealer = True
        self.assertEqual(game.start(), players[2], 'Expected player Z to be next player')
        self.assertEqual(game.current_player, players[2], 'Expected player Z to be current player')
        players[0].dealer = False
        players[1].dealer = True
        self.assertEqual(game.start(), players[0], 'Expected player X to be next player')
        self.assertEqual(game.current_player, players[0], 'Expected player X to be current player')
        players[1].dealer = False
        players[2].dealer = True
        self.assertEqual(game.start(), players[1], 'Expected player Y to be next player')
        self.assertEqual(game.current_player, players[1], 'Expected player Y to be current player')

    def test_next(self):
        game = Game(Deck.get_instance())
        self.assertEqual(game.random_player(), None)
        names = ['X', 'Y', 'Z']
        game.create_players(names, 2, 5)
        players = game.players
        game.current_player = players[0]
        self.assertEqual(game.next(), players[1], 'Expected player Y to be next player')
        game.current_player = players[1]
        self.assertEqual(game.next(), players[2], 'Expected player Z to be next player')
        game.current_player = players[2]
        self.assertEqual(game.next(), players[0], 'Expected player X to be next player')

    def test_draw_card(self):
        game = Game(Deck.get_instance())
        self.assertEqual(game.random_player(), None)
        names = ['X', 'Y', 'Z']
        game.create_players(names, 2, 5)
        players = game.players
        game.current_player = players[0]
        game.draw_card()
        self.assertEqual(len(game.current_player.hand), 1, 'Expected player to have 1 card')
        self.assertEqual(len(players[1].hand), 0, 'Expected player to have 0 card')
        self.assertEqual(len(players[2].hand), 0, 'Expected player to have 0 card')

    def test_choose_player(self):
        game = Game(Deck.get_instance())
        self.assertEqual(game.random_player(), None)
        names = ['X', 'Y', 'Z']
        game.create_players(names, 2, 5)
        players = game.players
        self.assertEqual(game.choose_player(4), None, 'Expected there to not be a player at that position')
        self.assertEqual(game.choose_player(1), players[0], 'Expected player X')
        self.assertEqual(game.choose_player(2), players[1], 'Expected player Y')
        self.assertEqual(game.choose_player(3), players[2], 'Expected player Z')

    # def test_capture_merchant_ship(self):


    def test_show_winner(self):
        game = Game(Deck.get_instance())
        self.assertEqual(game.random_player(), None)
        names = ['X', 'Y', 'Z']
        game.create_players(names, 2, 5)
        players = game.players
        players[0].merchant_ships_captured = [MerchantShip(2), MerchantShip(2), MerchantShip(2)]
        players[1].merchant_ships_captured = [MerchantShip(2), MerchantShip(2), MerchantShip(3)]
        players[2].merchant_ships_captured = [MerchantShip(2), MerchantShip(3), MerchantShip(4)]
        players_list = [[players[0], 6], [players[1], 7], [players[2], 9]]
        self.assertEqual(game.show_winner(), players_list, 'Expected to receive this player list')