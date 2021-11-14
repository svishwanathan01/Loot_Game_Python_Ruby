########## Sabareesh Vishwanathan ##########
########## 112585006 #############
########## SAVISHWANATH #############

import random, operator

pirateColors = ["blue", "green", "purple", "gold"]
maxPlayersAllowed = 5
minPlayersAllowed = 2
playerNames = ["Joy", "Nan", "Sat"]


class MerchantShip:
    def __init__(self, value):
        self.value = value
        # self.attacksValues = {}

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

    @staticmethod
    def set_instance():
        Admiral.__instance = None


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
                          Captain('blue'), Captain('green'), Captain('purple'), Captain('gold'), Admiral.get_instance()]

    @staticmethod
    def get_instance():
        if Deck.__instance is None:
            Deck()
        return Deck.__instance

    @staticmethod
    def set_instance():
        Deck.__instance = None


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
        random.shuffle(game_state.deck.cards)
        # print(game_state.deck.cards)
        # print(game_state.deck)
        self.dealer = game_state.current_player
        for player in game_state.players:
            for i in range(1, 7):
                player.hand.append(game_state.deck.cards.pop(0))

    def see_hand(self):
        return self.hand

    def draw_card(self, game_state):
        game_state.current_player = self
        game_state.draw_card()

    def float_merchant(self, card):
        if card in self.hand and isinstance(card, MerchantShip):
            self.merchant_ships_at_sea.append(card)
            self.hand.remove(card)
            return True
        return False

    def play_pirate(self, pirate_card, merchant_card, p1):
        # if pirate_card not in self.hand or merchant_card not in p1.merchant_ships_at_sea:
        if pirate_card not in self.hand:
            return False
        if merchant_card not in p1.merchant_ships_at_sea:
            return False
        if p1.merchant_pirates != {}:
            items = list(p1.merchant_pirates.items())
            if isinstance(items[len(items)-1], Admiral) or isinstance(items[len(items)-1], Captain):
                return False
        if not isinstance(pirate_card, PirateShip):
            return False
        for attacks in p1.merchant_pirates.values(): # check if ship has been attacked with color already
            if attacks[0][0] == self:
                if pirate_card.color != attacks[0][1].color:
                    return False
        for attacks in p1.merchant_pirates.values(): # check if ship has been attacked with color already
            if attacks[0][0] == self:
                if pirate_card.color != attacks[0][1].color:
                    return False
        for attacks in p1.merchant_pirates.values(): # check if ship has been attacked with color already
            if attacks[0][0] != self:
                if pirate_card.color == attacks[0][1].color:
                    return False
        if p1.merchant_pirates.get(merchant_card) is None:
            lst = []
            lst.append((self, pirate_card))
            p1.merchant_pirates[merchant_card] = lst
            # merchant_card.attacksValues[self] = pirate_card.attack_value
        else:
            lst = p1.merchant_pirates.get(merchant_card)
            for item in lst:
                if isinstance(item[1], Captain) or isinstance(item[1], Admiral):
                    return False
            lst.append((self, pirate_card))
            p1.merchant_pirates[merchant_card] = lst
            # if merchant_card.attacksValues.get(self) is None:
            #     merchant_card.attacksValues[self] = pirate_card.attack_value
            # else:
            #     merchant_card.attacksValues[self] += pirate_card.attack_value
        self.hand.remove(pirate_card)
        return True

    def play_captain(self, captain_card, merchant_card, p1):
        if captain_card not in self.hand:
            return False
        if merchant_card not in p1.merchant_ships_at_sea:
            return False
        if not isinstance(captain_card, Captain):
            return False
        for attacks in p1.merchant_pirates.values():
            if attacks[0][0] == self:
                if captain_card.color != attacks[0][1].color:
                    return False
        if p1.merchant_pirates.get(merchant_card) is None:
            return False
        else:
            lst = p1.merchant_pirates.get(merchant_card)
            lst.append((self, captain_card))
            p1.merchant_pirates[merchant_card] = lst
        self.hand.remove(captain_card)
        return True

    def play_admiral(self, admiral_card, merchant_card):
        if admiral_card not in self.hand:
            return False
        if merchant_card not in self.merchant_ships_at_sea:
            return False
        if not isinstance(admiral_card, Admiral):
            return False
        if merchant_card not in self.merchant_ships_at_sea:
            return False
        if self.merchant_pirates.get(merchant_card) is None:
            lst = []
            lst.append((self, admiral_card))
            self.merchant_pirates[merchant_card] = lst
        else:
            lst = self.merchant_pirates.get(merchant_card)
            lst.append((self, admiral_card))
            self.merchant_pirates[merchant_card] = lst
        self.hand.remove(admiral_card)
        return True


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
                    # self.current_player = self.players[len(self.players) - 1]
                    return self.players[len(self.players) - 1]
                # self.current_player = self.players[index - 1]
                return self.players[index - 1]
            index += 1

    def next(self):
        index = 0
        for player in self.players:
            if player == self.current_player:
                if index == len(self.players) - 1:
                    # self.current_player = self.players[0]
                    return self.players[0]
                # self.current_player = self.players[index+1]
                return self.players[index+1]
            index += 1

    def draw_card(self):
        self.current_player.hand.append(self.deck.cards.pop(0))

    def choose_player(self, pos):
        if pos > len(self.players):
            return None
        return self.players[pos-1]

    def capture_merchant_ships(self):
        atEnd = False
        ships_at_sea = self.current_player.merchant_ships_at_sea
        to_remove = []
        for i in range(0, len(ships_at_sea)):        # for ship in ships_at_sea:
            keys = list(self.current_player.merchant_pirates.keys())
            ship = ships_at_sea[i]
            if ship not in keys:
                to_remove.append(ship)
                # self.current_player.merchant_ships_at_sea.remove(ship)
                self.current_player.merchant_ships_captured.append(ship)
                # break
        for ship in to_remove:
            self.current_player.merchant_ships_at_sea.remove(ship)
        keys = list(self.current_player.merchant_pirates.keys())
        for key in keys:
            attacks = self.current_player.merchant_pirates[key]
            if isinstance(attacks[len(attacks) - 1][1], Admiral) or isinstance(attacks[len(attacks) - 1][1], Captain):
                atEnd = True
                if attacks[len(attacks) - 1][0] == self.current_player:
                    self.current_player.merchant_ships_at_sea.remove(key)
                    self.current_player.merchant_ships_captured.append(key)
                    break

        if atEnd == False:
            for player in self.players:
                to_remove = []
                shipsAttacked = player.merchant_pirates.keys()
                for ship in shipsAttacked:
                    attacks = player.merchant_pirates[ship]
                    attackMax = {}
                    for attack in attacks:
                        if attack[0] not in list(attackMax.keys()):
                            attackMax[attack[0]] = attack[1].attack_value
                        else:
                            attackMax[attack[0]] = attackMax[attack[0]] + attack[1].attack_value
                    sorted_d = dict(sorted(attackMax.items(), key=operator.itemgetter(1), reverse=True))
                    lst = list(sorted_d.keys())
                    if lst[0] == self.current_player:
                        if len(lst) == 1:
                            player.merchant_ships_at_sea.remove(ship)
                            self.current_player.merchant_ships_captured.append(ship)
                        elif attackMax[lst[0]] != attackMax[lst[1]]:
                            player.merchant_ships_at_sea.remove(ship)
                            self.current_player.merchant_ships_captured.append(ship)


    def show_winner(self):
        players_list = []
        final_list = []
        for player in self.players:
            gold = 0
            for captured in player.merchant_ships_captured:
                gold = gold + captured.get_value()
            players_list.append((player, gold))
        players_list.sort(key=lambda x:x[1], reverse=True)
        final_list.append(players_list[0])
        for i in range (1, len(players_list)):
            if players_list[i][1] == final_list[0][1]:
                final_list.append(players_list[i])
        return final_list
