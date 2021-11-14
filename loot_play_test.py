########## Sabareesh Vishwanathan ##########
########## 112585006 #############
########## SAVISHWANATH #############

import unittest
from loot import *

class TestLootPlay(unittest.TestCase):

    def test_create_game(self):
        Deck.set_instance()
        Admiral.set_instance()
        game = Game(Deck.get_instance())
        self.assertTrue(isinstance(game.deck, Deck), 'Object is not of type Deck')
        self.assertEqual([], game.players, 'Expected players to be empty')
        self.assertEqual(game.current_player, None, 'Expected current player to be None')

    def test_create_players(self):
        Deck.set_instance()
        Admiral.set_instance()
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
        Deck.set_instance()
        Admiral.set_instance()
        game = Game(Deck.get_instance())
        self.assertEqual(game.random_player(), None)
        names = ['X', 'Y', 'Z']
        game.create_players(names)
        players = game.players
        self.assertTrue(game.random_player() in players, 'Expected player to be in players')

    def test_start(self):
        Deck.set_instance()
        Admiral.set_instance()
        game = Game(Deck.get_instance())
        names = ['X', 'Y', 'Z']
        game.create_players(names)
        players = game.players
        players[0].dealer = True
        self.assertEqual(game.start(), players[2], 'Expected player Z to be next player')
        # self.assertEqual(game.current_player, players[2], 'Expected player Z to be current player')
        players[0].dealer = False
        players[1].dealer = True
        self.assertEqual(game.start(), players[0], 'Expected player X to be next player')
        # self.assertEqual(game.current_player, players[0], 'Expected player X to be current player')
        players[1].dealer = False
        players[2].dealer = True
        self.assertEqual(game.start(), players[1], 'Expected player Y to be next player')
        # self.assertEqual(game.current_player, players[1], 'Expected player Y to be current player')

    def test_next(self):
        Deck.set_instance()
        Admiral.set_instance()
        game = Game(Deck.get_instance())
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
        Deck.set_instance()
        Admiral.set_instance()
        game = Game(Deck.get_instance())
        names = ['X', 'Y', 'Z']
        game.create_players(names, 2, 5)
        players = game.players
        game.current_player = players[0]
        game.draw_card()
        self.assertEqual(len(game.current_player.hand), 1, 'Expected player to have 1 card')
        self.assertEqual(len(players[1].hand), 0, 'Expected player to have 0 card')
        self.assertEqual(len(players[2].hand), 0, 'Expected player to have 0 card')

    def test_choose_player(self):
        Deck.set_instance()
        Admiral.set_instance()
        game = Game(Deck.get_instance())
        names = ['X', 'Y', 'Z']
        game.create_players(names, 2, 5)
        players = game.players
        self.assertEqual(game.choose_player(4), None, 'Expected there to not be a player at that position')
        self.assertEqual(game.choose_player(1), players[0], 'Expected player X')
        self.assertEqual(game.choose_player(2), players[1], 'Expected player Y')
        self.assertEqual(game.choose_player(3), players[2], 'Expected player Z')

    def test_capture_merchant_ship(self):
        Deck.set_instance()
        Admiral.set_instance()
        game = Game(Deck.get_instance())
        names = ['X', 'Y', 'Z']
        game.create_players(names, 2, 5)
        players = game.players
        players[0].deal(game)
        # print(players[0].see_hand())
        # print(players[1].see_hand())
        # print(players[2].see_hand())
        for card in players[0].see_hand():
            if isinstance(card, MerchantShip):
                players[0].float_merchant(card)
        for card in players[1].see_hand():
            if isinstance(card, MerchantShip):
                players[1].float_merchant(card)
        for card in players[2].see_hand():
            if isinstance(card, MerchantShip):
                players[2].float_merchant(card)
        # print(players[0].merchant_ships_at_sea)
        # print(players[1].merchant_ships_at_sea)
        # print(players[2].merchant_ships_at_sea)

        # players[0].merchant_ships_at_sea = [MerchantShip(2), MerchantShip(2)]
        # players[1].merchant_ships_at_sea = [MerchantShip(2), MerchantShip(3)]
        # players[2].merchant_ships_at_sea = [MerchantShip(2), MerchantShip(4)]


    def test_show_winner(self):
        Deck.set_instance()
        Admiral.set_instance()
        game = Game(Deck.get_instance())
        names = ['X', 'Y', 'Z']
        game.create_players(names, 2, 5)
        players = game.players
        players[0].merchant_ships_captured = [MerchantShip(2), MerchantShip(2), MerchantShip(2)]
        players[1].merchant_ships_captured = [MerchantShip(2), MerchantShip(4), MerchantShip(3)]
        players[2].merchant_ships_captured = [MerchantShip(2), MerchantShip(3), MerchantShip(4)]
        # players_list = [[players[0], 6], [players[1], 7], [players[2], 9]]
        players_list = [(players[1], 9), (players[2], 9)]
        self.assertEqual(game.show_winner(), players_list, 'Expected to receive this player list')

    def test_player(self):
        Deck.set_instance()
        Admiral.set_instance()
        player = Player('X')
        self.assertEqual(player.name, 'X', "Expected to get player name")
        self.assertEqual(player.merchant_ships_at_sea, [], 'Expected empty list')
        self.assertEqual(player.merchant_ships_captured, [], 'Expected empty list')
        self.assertEqual(player.hand, [], 'Expected empty list')
        self.assertEqual(player.merchant_pirates, {}, 'Expected empty dictionary')
        self.assertEqual(player.dealer, False, 'Expected to not be dealer')

    def test_player_deal(self):
        Deck.set_instance()
        Admiral.set_instance()
        game = Game(Deck.get_instance())
        names = ['X', 'Y', 'Z']
        game.create_players(names, 2, 5)
        players = game.players
        players[0].deal(game)
        self.assertEqual(len(players[0].hand), 6, 'Expected to have 6 cards in hand')
        self.assertEqual(len(players[1].hand), 6, 'Expected to have 6 cards in hand')
        self.assertEqual(len(players[2].hand), 6, 'Expected to have 6 cards in hand')

    def test_player_draw_card(self):
        Deck.set_instance()
        Admiral.set_instance()
        game = Game(Deck.get_instance())
        names = ['X', 'Y', 'Z']
        game.create_players(names, 2, 5)
        players = game.players
        # game.current_player = players[0]
        players[0].deal(game)
        players[0].draw_card(game)
        players[1].draw_card(game)
        players[1].draw_card(game)
        players[2].draw_card(game)
        players[2].draw_card(game)
        players[2].draw_card(game)
        self.assertEqual(len(players[0].hand), 7, 'Expected to have 6 cards in hand')
        self.assertEqual(len(players[1].hand), 8, 'Expected to have 6 cards in hand')
        self.assertEqual(len(players[2].hand), 9, 'Expected to have 6 cards in hand')

    def test_player_float_merchant(self):
        Deck.set_instance()
        Admiral.set_instance()
        game = Game(Deck.get_instance())
        names = ['X', 'Y', 'Z']
        game.create_players(names)
        players = game.players
        players[0].deal(game)
        # print(len(Deck.get_instance().cards))
        player0Merchants = []
        player1Merchants = []
        player2Merchants = []
        for card in players[0].see_hand():
            if isinstance(card, MerchantShip):
                players[0].float_merchant(card)
                player0Merchants.append(card)
        for card in players[1].see_hand():
            if isinstance(card, MerchantShip):
                players[1].float_merchant(card)
                player1Merchants.append(card)
        for card in players[2].see_hand():
            if isinstance(card, MerchantShip):
                players[2].float_merchant(card)
                player2Merchants.append(card)
        self.assertEqual(players[0].merchant_ships_at_sea, player0Merchants)
        self.assertEqual(players[1].merchant_ships_at_sea, player1Merchants)
        self.assertEqual(players[2].merchant_ships_at_sea, player2Merchants)

    def test_player_play_pirate_1(self):
        Deck.set_instance()
        Admiral.set_instance()
        game = Game(Deck.get_instance())
        names = ['X', 'Y', 'Z']
        game.create_players(names)
        players = game.players
        players[0].deal(game)
        # print(len(Deck.get_instance().cards))
        player0Merchants = []
        player1Merchants = []
        player2Merchants = []
        player0Pirates = []
        player1Pirates = []
        player2Pirates = []
        for card in players[0].see_hand():
            if isinstance(card, MerchantShip):
                players[0].float_merchant(card)
                player0Merchants.append(card)
        for card in players[1].see_hand():
            if isinstance(card, MerchantShip):
                players[1].float_merchant(card)
                player1Merchants.append(card)
        for card in players[2].see_hand():
            if isinstance(card, MerchantShip):
                players[2].float_merchant(card)
                player2Merchants.append(card)
        for card in players[0].see_hand():
            if isinstance(card, PirateShip):
                player0Pirates.append(card)
        for card in players[1].see_hand():
            if isinstance(card, PirateShip):
                player1Pirates.append(card)
        for card in players[2].see_hand():
            if isinstance(card, PirateShip):
                player2Pirates.append(card)
        self.assertTrue(players[1].play_pirate(player1Pirates[0], player0Merchants[0], players[0]))

    def test_player_play_pirate_2(self):
        Deck.set_instance()
        Admiral.set_instance()
        game = Game(Deck.get_instance())
        deck = Deck.get_instance()
        names = ['X', 'Y', 'Z']
        game.create_players(names)
        players = game.players
        player0Merchants = [MerchantShip(2), MerchantShip(2), MerchantShip(2),]
        player1Merchants = [MerchantShip(3), MerchantShip(3), MerchantShip(3),]
        player2Merchants = [MerchantShip(4), MerchantShip(4), MerchantShip(4),]
        players[0].merchant_ships_at_sea = player0Merchants
        players[1].merchant_ships_at_sea = player1Merchants
        players[2].merchant_ships_at_sea = player2Merchants
        player0Pirates = [PirateShip('blue', 1), PirateShip('blue', 1), PirateShip('blue', 2),]
        player1Pirates = [PirateShip('green', 2), PirateShip('green', 2), PirateShip('green', 2),]
        player2Pirates = [PirateShip('purple', 3), PirateShip('purple', 4), PirateShip('purple', 4),]
        players[0].hand = player0Merchants + player0Pirates
        players[1].hand = player1Merchants + player1Pirates
        players[2].hand = player2Merchants + player2Pirates

        deck.cards = \
            [MerchantShip(2), MerchantShip(2),
             MerchantShip(3), MerchantShip(3), MerchantShip(3),
             MerchantShip(4), MerchantShip(4), MerchantShip(5), MerchantShip(5), MerchantShip(5), MerchantShip(5), MerchantShip(5),
             MerchantShip(6), MerchantShip(6), MerchantShip(7), MerchantShip(8),
             PirateShip('blue', 2),
             PirateShip('blue', 2), PirateShip('blue', 2), PirateShip('blue', 3), PirateShip('blue', 3),
             PirateShip('blue', 3), PirateShip('blue', 3), PirateShip('blue', 4), PirateShip('blue', 4),
             PirateShip('green', 1), PirateShip('green', 1), PirateShip('green', 2),
             PirateShip('green', 3), PirateShip('green', 3), PirateShip('green', 3),
             PirateShip('green', 3), PirateShip('green', 4), PirateShip('green', 4),
             PirateShip('purple', 1), PirateShip('purple', 1), PirateShip('purple', 2),
             PirateShip('purple', 2), PirateShip('purple', 2), PirateShip('purple', 2),
             PirateShip('purple', 3), PirateShip('purple', 3), PirateShip('purple', 3),
             PirateShip('gold', 1), PirateShip('gold', 1), PirateShip('gold', 2), PirateShip('gold', 2),
             PirateShip('gold', 2), PirateShip('gold', 2), PirateShip('gold', 3), PirateShip('gold', 3),
             PirateShip('gold', 3), PirateShip('gold', 3), PirateShip('gold', 4), PirateShip('gold', 4),
             Captain('blue'), Captain('green'), Captain('purple'), Captain('gold'), Admiral.get_instance(),]
        self.assertTrue(players[1].play_pirate(player1Pirates[0], player0Merchants[0], players[0]))
        print(players[0].merchant_pirates)
        self.assertTrue(players[2].play_pirate(player2Pirates[0], player0Merchants[0], players[0]))
        print(players[0].merchant_pirates)

    def test_player_play_pirate3(self):
        Deck.set_instance()
        Admiral.set_instance()
        deck = Deck.get_instance()
        game = Game(deck)
        game.create_players(playerNames)

        p1 = game.players[0]
        p1pirate1 = PirateShip("purple", 2)
        p1pirate2 = PirateShip("green", 2)
        p1pirate3 = PirateShip("purple", 3)
        p1.hand = [p1pirate1, p1pirate2, p1pirate3]

        p2 = game.players[1]
        p2pirate = PirateShip("purple", 2)
        p2merchant = MerchantShip(2)
        p2.hand = [p2pirate]
        p2.merchant_ships_at_sea = [p2merchant]
        self.assertTrue(p1.play_pirate(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                        "Expected to play pirate against merchant ship")
        self.assertEqual([(p1, p1pirate1)], p2.merchant_pirates[p2merchant],
                         "Expected to show tuple from merchant_pirates dictionary")
        self.assertFalse(p1.play_pirate(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                         "Cannot play a different colored PirateShip")
        self.assertTrue(p1.play_pirate(p1.hand[1], p2.merchant_ships_at_sea[0], p2),
                        "Expected to play pirate against merchant ship")
        self.assertEqual([(p1, p1pirate1), (p1, p1pirate3)], p2.merchant_pirates[p2merchant],
                         "Expected to show tuple from merchant_pirates dictionary")

    def test_player_play_captain1(self):
        Deck.set_instance()
        Admiral.set_instance()
        deck = Deck.get_instance()
        game = Game(deck)
        game.create_players(playerNames)
        p1 = game.players[0]
        p1.hand = [Captain('blue'), PirateShip("green", 2)]
        p1pirate1 = p1.hand[0]
        p1pirate2 = p1.hand[1]

        p2 = game.players[1]
        p2.hand = [PirateShip("purple", 2)]
        p2.merchant_ships_at_sea = [MerchantShip(2)]

        self.assertTrue(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                        'Expected to successfully play captain')
        self.assertEqual([(p1, p1pirate1)], p2.merchant_pirates[p2.merchant_ships_at_sea[0]],
                         'Expected to see tuple in merchant_pirates instance')
        self.assertFalse(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                         'Cannot play non-captain object')

    def test_player_play_captain2(self):
        Deck.set_instance()
        Admiral.set_instance()
        deck = Deck.get_instance()
        game = Game(deck)
        game.create_players(playerNames)
        p1 = game.players[0]
        p1.hand = [PirateShip("green", 2), Captain('blue'),]
        p1pirate1 = p1.hand[0]
        p1pirate2 = p1.hand[1]

        p2 = game.players[1]
        p2.hand = [PirateShip("purple", 2)]
        p2.merchant_ships_at_sea = [MerchantShip(2)]

        self.assertTrue(p1.play_pirate(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                        "Expected to play pirate against merchant ship")
        self.assertFalse(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                         'Cannot play different colored Captain')
        # self.assertEqual([(p1, p1pirate1)], p2.merchant_pirates[p2.merchant_ships_at_sea[0]])
        # self.assertFalse(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2))

    def test_player_play_captain3(self):
        Deck.set_instance()
        Admiral.set_instance()
        deck = Deck.get_instance()
        game = Game(deck)
        game.create_players(playerNames)
        p1 = game.players[0]
        p1.hand = [PirateShip("blue", 2), Captain('blue'),]
        p1pirate1 = p1.hand[0]
        p1pirate2 = p1.hand[1]

        p2 = game.players[1]
        p2.hand = [PirateShip("purple", 2)]
        p2.merchant_ships_at_sea = [MerchantShip(2)]

        self.assertTrue(p1.play_pirate(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                        "Expected to play pirate against merchant ship")
        self.assertTrue(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                         'Cannot play different colored Captain')
        print(p2.merchant_pirates[p2.merchant_ships_at_sea[0]][1])
        # print(p2.merchant_pirates[p2.merchant_ships_at_sea[1]])
        self.assertEqual([(p1, p1pirate1), (p1, p1pirate2)], p2.merchant_pirates[p2.merchant_ships_at_sea[0]],
                         'Expected to find attack tuples in merchant_pirates object')

    def test_player_play_admiral1(self):
        Deck.set_instance()
        Admiral.set_instance()
        deck = Deck.get_instance()
        game = Game(deck)
        game.create_players(playerNames)
        p1 = game.players[0]
        p1.hand = [Captain('blue'), PirateShip("green", 2)]
        p1pirate1 = p1.hand[0]
        p1pirate2 = p1.hand[1]

        p2 = game.players[1]
        p2.hand = [Admiral.get_instance(), PirateShip("purple", 2),]
        p2Admiral = p2.hand[0]
        p2Pirate = p2.hand[1]
        p2.merchant_ships_at_sea = [MerchantShip(2)]

        self.assertTrue(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                        'Expected to successfully play captain')
        self.assertEqual([(p1, p1pirate1)], p2.merchant_pirates[p2.merchant_ships_at_sea[0]],
                         'Expected to see tuple in merchant_pirates instance')
        self.assertTrue(p2.play_admiral(p2Admiral, p2.merchant_ships_at_sea[0]),
                        'Expected to successfully play captain')
        self.assertEqual([(p1, p1pirate1), (p2, p2Admiral)], p2.merchant_pirates[p2.merchant_ships_at_sea[0]],
                         'Expected to see tuple in merchant_pirates instance')