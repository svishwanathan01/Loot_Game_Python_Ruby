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
            raise RuntimeError()
        else:
            Admiral.__instance = self

    @staticmethod
    def get_instance():
        if Admiral.__instance is None:
            Admiral()
        return Admiral.__instance


class Deck:
    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        pass


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

        pass

    def see_hand(self):
        pass

    def draw_card(self, game_state):
        pass

    def float_merchant(self, card):
        pass

    def play_pirate(self, pirate_card, merchant_card, p1):
        pass

    def play_captain(self, captain_card, merchant_card, p1):
        pass

    def play_admiral(self, admiral_card, merchant_card):
        pass


class Game:
    def __init__(self, deck):
        pass

    def create_players(self, names, min_players, max_players):
        pass

    def random_player(self):
        pass

    def start(self):
        pass

    def next(self):
        pass

    def draw_card(self):
        pass

    def choose_player(self, pos):
        pass

    def capture_merchant_ships(self):
        pass

    def show_winner(self):
        pass
