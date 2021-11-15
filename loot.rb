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
  end

  def draw_card(game)
  end

  def add_to_hand(card)
  end

  def float_merchant(card)
  end

  def play_pirate(pirate_card, merchant_card, pl)
  end

  def play_captain(captain_card, merchant_card, pl)
  end

  def play_admiral(admiral_card, merchant_card)
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
  end
end
