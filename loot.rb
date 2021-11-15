########## Sabareesh Vishwanathan ##########
########## 112585006 #############
########## SAVISHWANATH #############

$pirateColors = [:blue, :green, :purple, :gold]
$maxPlayersAllowed = 5
$minPlayersAllowed = 2
$playerNames = ["Joy", "Nan", "Sat"]

class MerchantShip
  attr_accessor :value

  def initialize(value)
    @value = value
  end

  def get_value
    @value
  end
end

class PirateShip
  attr_accessor :color, :attack_value

  def initialize(color, attack_value)
    @color = color
    @attack_value = attack_value
  end

  def get_color
    @color
  end

  def get_value
    @attack_value
  end
end

class Captain
  attr_accessor :color

  def initialize(color)
    @color = color
  end

  def get_color
    @color
  end
end

class Admiral
  @@instance = nil
  def initialize
    if !@@instance.nil?
      raise RuntimeError
    else
      @@instance = self
    end
  end

  def Admiral.get_instance
    if @@instance.nil?
      Admiral.new()
    end
    return @@instance
  end

  def Admiral.set_instance
    @@instance = nil
  end
end

class Deck
  @@instance = nil
  @@cards = [MerchantShip.new(2), MerchantShip.new(2), MerchantShip.new(2), MerchantShip.new(2),
             MerchantShip.new(2),    MerchantShip.new(3), MerchantShip.new(3), MerchantShip.new(3), MerchantShip.new(3),
             MerchantShip.new(3),    MerchantShip.new(3),    MerchantShip.new(4), MerchantShip.new(4), MerchantShip.new(4), MerchantShip.new(4), MerchantShip.new(4),
             MerchantShip.new(5), MerchantShip.new(5), MerchantShip.new(5), MerchantShip.new(5), MerchantShip.new(5),    MerchantShip.new(6), MerchantShip.new(6), MerchantShip.new(7), MerchantShip.new(8),    PirateShip.new('blue', 1), PirateShip.new('blue', 1),
             PirateShip.new('blue', 2), PirateShip.new('blue', 2),    PirateShip.new('blue', 2), PirateShip.new('blue', 2), PirateShip.new('blue', 3), PirateShip.new('blue', 3),    PirateShip.new('blue', 3), PirateShip.new('blue', 3), PirateShip.new('blue', 4),
             PirateShip.new('blue', 4),    PirateShip.new('green', 1), PirateShip.new('green', 1), PirateShip.new('green', 2),    PirateShip.new('green', 2), PirateShip.new('green', 2), PirateShip.new('green', 2),    PirateShip.new('green', 3), PirateShip.new('green', 3),
             PirateShip.new('green', 3),    PirateShip.new('green', 3), PirateShip.new('green', 4), PirateShip.new('green', 4),    PirateShip.new('purple', 1), PirateShip.new('purple', 1), PirateShip.new('purple', 2),    PirateShip.new('purple', 2), PirateShip.new('purple', 2),
             PirateShip.new('purple', 2),PirateShip.new('purple', 3), PirateShip.new('purple', 3), PirateShip.new('purple', 3),PirateShip.new('purple', 3), PirateShip.new('purple', 4), PirateShip.new('purple', 4),PirateShip.new('gold', 1), PirateShip.new('gold', 1), PirateShip.new('gold', 2),
             PirateShip.new('gold', 2),PirateShip.new('gold', 2), PirateShip.new('gold', 2), PirateShip.new('gold', 3), PirateShip.new('gold', 3),PirateShip.new('gold', 3), PirateShip.new('gold', 3), PirateShip.new('gold', 4), PirateShip.new('gold', 4),Captain.new('blue'),
             Captain.new('green'), Captain.new('purple'), Captain.new('gold'), Admiral.get_instance]
  def initialize
    if !@@instance.nil?
      raise RuntimeError
    else
      @@instance = self
    end
  end

  def self.get_instance
    if @@instance.nil?
      Deck.new()
    end
    return @@instance
  end

  def cards
    @@cards
  end

  def setCards(cards)
    @@cards = cards
  end

  def Deck.set_instance
    @@instance = nil
  end
end

class Player
  attr_accessor :name, :merchant_ships_at_sea, :merchant_ships_captured, :hand, :merchant_pirates, :dealer
  def initialize(name)
    @name = name
    @merchant_ships_at_sea = []
    @merchant_ships_captured = []
    @hand = []
    @merchant_pirates = {}
    @dealer = FALSE
  end

  def deal(game_state)
    game_state.deck.setCards(game_state.deck.cards.shuffle)
    @dealer = game_state.current_player
    for player in game_state.players
      for i in 1..6
        player.hand.append(game_state.deck.cards[0])
        game_state.deck.cards.drop(1)
      end
    end
  end

  def draw_card(game)
    game.current_player = self
    game.draw_card
  end

  def see_hand
    @hand
  end

  def float_merchant(card)
    if hand.include?(card) and card.instance_of?(MerchantShip)
      @merchant_ships_at_sea.append(card)
      @hand.delete(card)
      return TRUE
    end
    return FALSE
  end

  def play_pirate(pirate_card, merchant_card, pl)
    if !@hand.include?(pirate_card)
      return FALSE
    end
    if !pl.merchant_ships_at_sea.include?(merchant_card)
      return FALSE
    end
    if pl.merchant_pirates != {}
      items = pl.merchant_pirates.keys
      if items[items.length - 1].instance_of?(Admiral) or items[items.length - 1].instance_of?(Captain)
        return FALSE
      end
    end
    if !pirate_card.instance_of?(PirateShip)
      return FALSE
    end
    for attacks in pl.merchant_pirates.values
      if attacks[0][0] == self
        if pirate_card.color != attacks[0][1].color
          return FALSE
        end
      end
    end
    if pl.merchant_pirates[merchant_card] ==nil
      lst = []
      lst.append([self, pirate_card])
      pl.merchant_pirates[merchant_card] = lst
    else
      lst = pl.merchant_pirates[merchant_card]
      for item in lst
        if item[1].instance_of?(Captain) or item[1].instance_of?(Admiral)
          return FALSE
        end
      end
      lst.append([self, pirate_card])
      pl.merchant_pirates[merchant_card] = lst
    end
    @hand.delete(pirate_card)
    return TRUE
  end

  def play_captain(captain_card, merchant_card, pl)
    if !@hand.include?(captain_card)
      return FALSE
    end
    if !pl.merchant_ships_at_sea.include?(merchant_card)
      return FALSE
    end
    if !captain_card.instance_of?(Captain)
      return FALSE
    end
    for attacks in pl.merchant_pirates.values
      if attacks[0][0] == self
        if captain_card.color != attacks[0][1].color
          return FALSE
        end
      end
    end
    if pl.merchant_pirates[merchant_card] == nil
      return FALSE
    else
      lst = pl.merchant_pirates[merchant_card]
      lst.append([self, captain_card])
      pl.merchant_pirates[merchant_card] = lst
    end
    hand.delete(captain_card)
    return TRUE
  end

  def play_admiral(admiral_card, merchant_card)
    if !@hand.include?(admiral_card)
      return FALSE
    end
    if !@merchant_ships_at_sea.include?(merchant_card)
      return FALSE
    end
    if !admiral_card.instance_of?(Admiral)
      return FALSE
    end
    if !merchant_ships_at_sea.include?(merchant_card)
      return FALSE
    end
    if @merchant_pirates[merchant_card] == nil
      lst = []
      lst.append([self, admiral_card])
      @merchant_pirates[merchant_card] = lst
    else
      lst = @merchant_pirates[merchant_card]
      lst.append([self, admiral_card])
      merchant_pirates[merchant_card] = lst
    end
    @hand.delete(admiral_card)
    return TRUE
  end
end

class Game
  attr_accessor :deck, :players, :current_player
  def initialize(deck)
    @deck = deck
    @players = []
    @current_player = nil
  end

  def create_players(names, min_players=2, max_players=5)
    if names.length() < min_players or names.length() > max_players
      raise RuntimeError
    end
    for name in names
      @players.append(Player.new(name))
    end
  end

  def random_player
    if players.length == 0
      return nil
    end
    choose_player(rand(1..@players.length()))
  end

  def start
    index = 0
    for player in @players
      if player.dealer == TRUE
        if index == 0
          return @players[@players.length - 1]
        end
        return @players[index -1]
      end
      index += 1
    end
  end

  def next
    index = 0
    for player in @players
      if player == @current_player
        if index == @players.length() - 1
          return @players[0]
        end
        return @players[index +1]
      end
      index += 1
    end
  end

  def draw_card
    current_player.hand.append(deck.cards.pop(0))
  end

  def choose_player(pos)
    if pos > players.length
      return nil
    end
    players[pos-1]
  end

  def capture_merchant_ships
    
  end

  def show_winner
    players_list = []
    final_list = []
    for player in @players
      gold = 0
      for captured in player.merchant_ships_captured
        gold = gold + captured.get_value
      end
      players_list.append([player, gold])
    end
    players_list = players_list.sort {|a,b| a[1] <=> b[1]}.reverse
    final_list.append(players_list[0])
    for i in (1..players_list.length - 1)
      if players_list[i][1] == final_list[0][1]
        final_list.append(players_list[i])
      end
    end
    return final_list
  end
end
