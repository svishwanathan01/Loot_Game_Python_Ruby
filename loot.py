########## Sabareesh Vishwanathan ##########
########## 112585006 #############
########## SAVISHWANATH #############

import random

pirateColors = ["blue", "green", "purple", "gold"]
maxPlayersAllowed = 5
minPlayersAllowed = 2
playerNames = ["Joy", "Nan", "Sat"]


class MerchantShip:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class PirateShip:
    def __init__(self, color, attack_value):
        self.color = color
        self.attack_value = attack_value

    def get_value(self):
        return self.attack_value

    def get_color(self):
        return self.color


class Captain:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Admiral:
    __instance = None

    def __init__(self):
        if Admiral.__instance is not None:
            raise RuntimeError('Singleton')
        else:
            Admiral.__instance = self

    @staticmethod
    def get_instance():
        if Admiral.__instance is None:
            Admiral()
        return Admiral.__instance


class Deck:
    __instance = None

    def __init__(self):
        if Deck.__instance is not None:
            raise RuntimeError('Singleton')
        else:
            Deck.__instance = self
            Deck.__instance.cards = \
                        [MerchantShip(2), MerchantShip(2), MerchantShip(2), MerchantShip(2), MerchantShip(2),
                          MerchantShip(3), MerchantShip(3), MerchantShip(3), MerchantShip(3), MerchantShip(3),
                          MerchantShip(3),
                          MerchantShip(4), MerchantShip(4), MerchantShip(4), MerchantShip(4), MerchantShip(4),
                          MerchantShip(5), MerchantShip(5), MerchantShip(5), MerchantShip(5), MerchantShip(5),
                          MerchantShip(6), MerchantShip(6), MerchantShip(7), MerchantShip(8),
                          PirateShip('blue', 1), PirateShip('blue', 1), PirateShip('blue', 2), PirateShip('blue', 2),
                          PirateShip('blue', 2), PirateShip('blue', 2), PirateShip('blue', 3), PirateShip('blue', 3),
                          PirateShip('blue', 3), PirateShip('blue', 3), PirateShip('blue', 4), PirateShip('blue', 4),
                          PirateShip('green', 1), PirateShip('green', 1), PirateShip('green', 2),
                          PirateShip('green', 2), PirateShip('green', 2), PirateShip('green', 2),
                          PirateShip('green', 3), PirateShip('green', 3), PirateShip('green', 3),
                          PirateShip('green', 3), PirateShip('green', 4), PirateShip('green', 4),
                          PirateShip('purple', 1), PirateShip('purple', 1), PirateShip('purple', 2),
                          PirateShip('purple', 2), PirateShip('purple', 2), PirateShip('purple', 2),
                          PirateShip('purple', 3), PirateShip('purple', 3), PirateShip('purple', 3),
                          PirateShip('purple', 3), PirateShip('purple', 4), PirateShip('purple', 4),
                          PirateShip('gold', 1), PirateShip('gold', 1), PirateShip('gold', 2), PirateShip('gold', 2),
                          PirateShip('gold', 2), PirateShip('gold', 2), PirateShip('gold', 3), PirateShip('gold', 3),
                          PirateShip('gold', 3), PirateShip('gold', 3), PirateShip('gold', 4), PirateShip('gold', 4),
                          Captain('blue'), Captain('green'), Captain('purple'), Captain('gold'), Admiral()]

    @staticmethod
    def get_instance():
        if Deck.__instance is None:
            Deck()
        return Deck.__instance


class Player:
    def __init__(self, name):
        self.name = name
        self.merchant_ships_at_sea = []
        self.merchant_ships_captured = []
        self.hand = []
        self.merchant_pirates = {}
        self.dealer = False
        pass

    def deal(self, game_state):
        random.shuffle(game_state.deck)
        self.dealer = game_state.current_player
        for player in game_state.players:
            for i in range(1, 7):
                player.hand.append(game_state.deck.pop(0))

    def see_hand(self):
        pass

    def draw_card(self, game_state):
        game_state.draw_card()

    def float_merchant(self, card):
        if card in self.hand and isinstance(card, MerchantShip):
            self.merchant_ships_at_sea.append(card)
            return True
        return False

    def play_pirate(self, pirate_card, merchant_card, p1):
        if pirate_card not in self.hand or merchant_card not in p1.merchant_pirates.keys():
            return False
        exist = False
        for attacks in p1.merchant_pirates.values():
            if attacks[0] == self:
                if pirate_card.get_Color() != attacks[1].get_color():
                    return False
                exist = True
                attacks[1].attack_value = pirate_card.attack_value + attacks[1].attack_value
        if exist == False:
            for attacks in p1.merchant_pirates.values(): # check if ship has been attacked with color already
                if pirate_card.get_Color() == attacks[1].get_color():
                    return False
            p1.merchant_pirates[merchant_card] = [self, pirate_card.attack_value]
        return True

    def play_captain(self, captain_card, merchant_card, p1):
        if captain_card not in self.hand or merchant_card not in p1.merchant_pirates.keys():
            return False
        exist = False
        for attacks in p1.merchant_pirates.values():
            for attack in attacks:
                if attacks[0] == self:
                    if captain_card.get_Color() != attacks[1].get_color():
                        return False
                # exist = True
                # attacks[1].attack_value = pirate_card.attack_value + attacks[1].attack_value
        p1.merchant_pirates[merchant_card] = [self, captain_card.attack_value]

    def play_admiral(self, admiral_card, merchant_card):
        pass


class Game:
    def __init__(self, deck):
        self.deck = deck
        self.players = []
        self.current_player = None

    def create_players(self, names, min_players=2, max_players=5):
        if len(names) < min_players or len(names) > max_players:
            raise RuntimeError
        for name in names:
            self.players.append(Player(name))

    def random_player(self):
        if self.players == []:
            return None
        return self.players[random.randint(0, len(self.players) - 1)]

    def start(self):
        index = 0
        for player in self.players:
            if player.dealer == True:
                if index == 0:
                    self.current_player = self.players[len(self.players) - 1]
                    return self.players[len(self.players) - 1]
                self.current_player = self.players[index - 1]
                return self.players[index - 1]
            index += 1

    def next(self):
        index = 0
        for player in self.players:
            if player == self.current_player:
                if index == len(self.players) - 1:
                    self.current_player = self.players[0]
                    return self.players[0]
                self.current_player = self.players[index+1]
                return self.players[index+1]
            index += 1

    def draw_card(self):
        self.current_player.hand.append(self.deck.cards.pop(0))

    def choose_player(self, pos):
        if pos > len(self.players):
            return None
        return self.players[pos-1]

    def capture_merchant_ships(self):
        pass

    def show_winner(self):
        players_list = []
        for player in self.players:
            gold = 0
            for captured in player.merchant_ships_captured:
                gold = gold + captured.get_value()
            players_list.append([player, gold])
        return players_list
