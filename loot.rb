########## ENTER FULL NAME ##########
########## ENTER SBU ID #############
########## ENTER NET ID #############

$pirateColors = [:blue, :green, :purple, :gold]
$maxPlayersAllowed = 5
$minPlayersAllowed = 2
$playerNames = ["Joy", "Nan", "Sat"]

class MerchantShip
  def initialize(value)
  end
end

class PirateShip
  def initialize(color, attack_value)
  end
end

class Captain
  def initialize(color)
  end
end

class Admiral
  def initialize
  end

  def Admiral.get_instance
  end
end

class Player
  def initialize(name)
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

class Deck
  def initialize
  end

  def self.get_instance
  end
end

class Game
  def initialize(deck)
  end

  def create_players(names, min_players, max_players)
  end

  def random_player
  end

  def start
  end

  def next
  end

  def draw_card
  end

  def choose_player(pos)
  end

  def capture_merchant_ships
  end

  def show_winner
  end
end
