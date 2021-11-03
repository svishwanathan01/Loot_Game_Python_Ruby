########## ENTER FULL NAME ##########
########## ENTER SBU ID #############
########## ENTER NET ID #############

import random

pirateColors = ["blue", "green", "purple", "gold"]
maxPlayersAllowed = 5
minPlayersAllowed = 2
playerNames = ["Joy", "Nan", "Sat"]


class MerchantShip:
    def __init__(self, value):
        pass

    def get_value(self):
        pass


class PirateShip:
    def __init__(self, color, attack_value):
        pass

    def get_value(self):
        pass

    def get_color(self):
        pass


class Captain:
    def __init__(self, color):
        pass

    def get_color(self):
        pass


class Admiral:
    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        pass


class Player:
    def __init__(self, name):
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

class Deck:
    def __init__(self):
        pass

    @staticmethod
    def get_instance():
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
