########## Sabareesh Vishwanathan ##########
########## 112585006 #############
########## SAVISHWANATH #############

require 'test/unit'
require 'test/unit/assertions'
require_relative "./loot.rb"

class MyTest < Test::Unit::TestCase
  def test_create_players
    game = Game.new(Deck.get_instance())
    names = ['X', 'Y', 'Z', 'A', 'B', 'C']
    assert_raises RuntimeError do
      game.create_players(names)
    end
    names = ['X']
    assert_raises RuntimeError do
      game.create_players(names)
    end
    names = ['X', 'Y', 'Z']
    game.create_players(names)
    playerNames = []
    for player in game.players
      playerNames.append(player.name)
    end
    assert_equal(playerNames, names, 'Expected players to be empty')
    assert_equal(game.current_player, nil, 'Expected current player to be None')
  end

  def test_random_player
    game = Game.new(Deck.get_instance())
    assert_equal(game.random_player(), nil)
    names = ['X', 'Y', 'Z']
    game.create_players(names)
    players = game.players
    assert_true(game.players.include?(game.random_player), 'Expected player to be in players')
  end

  def test_start
    game = Game.new(Deck.get_instance())
    names = ['X', 'Y', 'Z']
    game.create_players(names)
    players = game.players
    players[0].dealer = TRUE
    # print(players.length)
    # print(game.start().name)
    assert_equal(game.start(), players[2], 'Expected player Z to be next player')
    # self.assertEqual(game.current_player, players[2], 'Expected player Z to be current player')
    players[0].dealer = FALSE
    players[1].dealer = TRUE
    assert_equal(game.start(), players[0], 'Expected player X to be next player')
    # self.assertEqual(game.current_player, players[0], 'Expected player X to be current player')
    players[1].dealer = FALSE
    players[2].dealer = TRUE
    assert_equal(game.start(), players[1], 'Expected player Y to be next player')
  end

  def test_next
    game = Game.new(Deck.get_instance())
    names = ['X', 'Y', 'Z']
    game.create_players(names, 2, 5)
    players = game.players
    game.current_player = players[0]
    assert_equal(game.next(), players[1], 'Expected player Y to be next player')
    game.current_player = players[1]
    assert_equal(game.next(), players[2], 'Expected player Z to be next player')
    game.current_player = players[2]
    assert_equal(game.next(), players[0], 'Expected player X to be next player')
  end

  def test_draw_card
    game = Game.new(Deck.get_instance())
    names = ['X', 'Y', 'Z']
    game.create_players(names, 2, 5)
    players = game.players
    game.current_player = players[0]
    game.draw_card()
    assert_equal(game.current_player.hand.length, 1, 'Expected player to have 1 card')
    assert_equal(players[1].hand.length, 0, 'Expected player to have 0 card')
    assert_equal(players[2].hand.length, 0, 'Expected player to have 0 card')
  end

  def test_choose_player
    game = Game.new(Deck.get_instance())
    names = ['X', 'Y', 'Z']
    game.create_players(names, 2, 5)
    players = game.players
    assert_equal(game.choose_player(4), nil, 'Expected there to not be a player at that position')
    assert_equal(game.choose_player(1), players[0], 'Expected player X')
    assert_equal(game.choose_player(2), players[1], 'Expected player Y')
    assert_equal(game.choose_player(3), players[2], 'Expected player Z')
  end

  def test_show_winner
    game = Game.new(Deck.get_instance())
    names = ['X', 'Y', 'Z']
    game.create_players(names, 2, 5)
    players = game.players
    # print(players)
    players[0].merchant_ships_captured = [MerchantShip.new(2), MerchantShip.new(2), MerchantShip.new(2)]
    players[1].merchant_ships_captured = [MerchantShip.new(2), MerchantShip.new(4), MerchantShip.new(3)]
    players[2].merchant_ships_captured = [MerchantShip.new(2), MerchantShip.new(3), MerchantShip.new(4)]
    players_list = [[players[1], 9],[players[2], 9]]
    assert_equal(game.show_winner, players_list.reverse, 'Expected to receive this player list')
  end
  def test_player
    player = Player.new('X')
    assert_equal(player.name, 'X', "Expected to get player name")
    assert_equal(player.merchant_ships_at_sea, [], 'Expected empty list')
    assert_equal(player.merchant_ships_captured, [], 'Expected empty list')
    assert_equal(player.hand, [], 'Expected empty list')
    assert_equal(player.merchant_pirates, {}, 'Expected empty dictionary')
    assert_equal(player.dealer, FALSE, 'Expected to not be dealer')
  end

  def test_player_deal
    game = Game.new(Deck.get_instance())
    names = ['X', 'Y', 'Z']
    game.create_players(names, 2, 5)
    players = game.players
    players[0].deal(game)
    assert_equal(players[0].hand.length, 6, 'Expected to have 6 cards in hand')
    assert_equal(players[1].hand.length, 6, 'Expected to have 6 cards in hand')
    assert_equal(players[2].hand.length, 6, 'Expected to have 6 cards in hand')
  end

  def test_player_draw_card
    game = Game.new(Deck.get_instance())
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
    assert_equal(players[0].hand.length, 7, 'Expected to have 6 cards in hand')
    assert_equal(players[1].hand.length, 8, 'Expected to have 6 cards in hand')
    assert_equal(players[2].hand.length, 9, 'Expected to have 6 cards in hand')
  end

  def test_player_float_merchant
    Deck.set_instance()
    Admiral.set_instance()
    game = Game.new(Deck.get_instance())
    assert_equal(game.deck.cards.length, 78)
    # print(game.deck.cards)
    names = ['X', 'Y', 'Z']
    game.create_players(names)
    players = game.players
    players[0].deal(game)
    # puts()
    # print(players[0].hand)
    # print(players[1].hand)
    # print(players[2].hand)
    # print(len(Deck.get_instance().cards))
    player0Merchants = []
    player1Merchants = []
    player2Merchants = []
    # print(players[0].see_hand)
    for card in players[0].see_hand()
      if card.instance_of?(MerchantShip)
        players[0].float_merchant(card)
        player0Merchants.append(card)
      end
    end
    for card in players[1].see_hand()
      if card.instance_of?(MerchantShip)
        players[1].float_merchant(card)
        player1Merchants.append(card)
      end
    end
    for card in players[2].see_hand()
      if card.instance_of?(MerchantShip)
        players[2].float_merchant(card)
        player2Merchants.append(card)
      end
    end
    print(player0Merchants)
    assert_equal(players[0].merchant_ships_at_sea, player0Merchants)
    assert_equal(players[1].merchant_ships_at_sea, player1Merchants)
    assert_equal(players[2].merchant_ships_at_sea, player2Merchants)
  end

  def test_player_play_pirate
    Deck.set_instance()
    Admiral.set_instance()
    deck = Deck.get_instance()
    game = Game.new(deck)
    game.create_players($playerNames)

    p1 = game.players[0]
    p1pirate1 = PirateShip.new("purple", 2)
    p1pirate2 = PirateShip.new("green", 2)
    p1pirate3 = PirateShip.new("purple", 3)
    p1.hand = [p1pirate1, p1pirate2, p1pirate3]

    p2 = game.players[1]
    p2pirate = PirateShip.new("purple", 2)
    p2merchant = MerchantShip.new(2)
    p2.hand = [p2pirate]
    p2.merchant_ships_at_sea = [p2merchant]
    assert_true(p1.play_pirate(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                "Expected to play pirate against merchant ship")
    assert_equal([[p1, p1pirate1]], p2.merchant_pirates[p2merchant],
                 "Expected to show tuple from merchant_pirates dictionary")
    assert_false(p1.play_pirate(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                 "Cannot play a different colored PirateShip")
    assert_true(p1.play_pirate(p1.hand[1], p2.merchant_ships_at_sea[0], p2),
                "Expected to play pirate against merchant ship")
    assert_equal([[p1, p1pirate1], [p1, p1pirate3]], p2.merchant_pirates[p2merchant],
                 "Expected to show tuple from merchant_pirates dictionary")
  end

  def test_player_play_captain
    Deck.set_instance()
    Admiral.set_instance()
    deck = Deck.get_instance()
    game = Game.new(deck)
    game.create_players($playerNames)
    p1 = game.players[0]
    p1.hand = [PirateShip.new("blue", 2), Captain.new('blue'), PirateShip.new("green", 2)]
    p1pirate1 = p1.hand[0]
    p1Captain = p1.hand[1]
    p1pirate2 = p1.hand[2]

    p2 = game.players[1]
    p2.hand = [PirateShip.new("purple", 2)]
    p2.merchant_ships_at_sea = [MerchantShip.new(2)]

    assert_true(p1.play_pirate(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                'Expected to successfully play pirate ship')
    assert_true(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                'Expected to successfully play pirate ship')
    assert_equal([[p1, p1pirate1], [p1, p1Captain]], p2.merchant_pirates[p2.merchant_ships_at_sea[0]],
                 'Expected to see tuple in merchant_pirates instance')
    assert_false(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                 'Cannot play non-captain object')
  end

  def test_player_play_captain2
    Deck.set_instance()
    Admiral.set_instance()
    deck = Deck.get_instance()
    game = Game.new(deck)
    game.create_players($playerNames)
    p1 = game.players[0]
    p1.hand = [PirateShip.new("green", 2), Captain.new('blue'),]
    p1pirate1 = p1.hand[0]
    p1pirate2 = p1.hand[1]

    p2 = game.players[1]
    p2.hand = [PirateShip.new("purple", 2)]
    p2.merchant_ships_at_sea = [MerchantShip.new(2)]

    assert_true(p1.play_pirate(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                "Expected to play pirate against merchant ship")
    assert_false(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                 'Cannot play different colored Captain')
    # self.assertEqual([(p1, p1pirate1)], p2.merchant_pirates[p2.merchant_ships_at_sea[0]])
    # self.assertFalse(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2))
  end

  def test_player_play_captain3
    Deck.set_instance()
    Admiral.set_instance()
    deck = Deck.get_instance()
    game = Game.new(deck)
    game.create_players($playerNames)
    p1 = game.players[0]
    p1.hand = [PirateShip.new("blue", 2), Captain.new('blue'),]
    p1pirate1 = p1.hand[0]
    p1pirate2 = p1.hand[1]

    p2 = game.players[1]
    p2.hand = [PirateShip.new("purple", 2)]
    p2.merchant_ships_at_sea = [MerchantShip.new(2)]

    assert_true(p1.play_pirate(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                "Expected to play pirate against merchant ship")
    assert_true(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                'Cannot play different colored Captain')
    # print(p2.merchant_pirates[p2.merchant_ships_at_sea[0]][1])
    # print(p2.merchant_pirates[p2.merchant_ships_at_sea[1]])
    assert_equal([[p1, p1pirate1], [p1, p1pirate2]], p2.merchant_pirates[p2.merchant_ships_at_sea[0]],
                 'Expected to find attack tuples in merchant_pirates object')
  end

  def test_player_play_captain4
    Deck.set_instance()
    Admiral.set_instance()
    deck = Deck.get_instance()
    game = Game.new(deck)
    game.create_players($playerNames)

    p1 = game.players[0]
    p1pirate = PirateShip.new("blue", 2)
    p1captain = Captain.new("blue")
    p1.hand = [p1pirate, p1captain]

    p2 = game.players[1]
    p2pirate = PirateShip.new("blue", 2)
    p2merchant = MerchantShip.new(2)
    p2.hand = [p2pirate]
    p2.merchant_ships_at_sea = [p2merchant]

    assert_false(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2), "Expected P1 Captain!")
    assert_false(p1.play_captain(p1.hand[1], p2.hand[0], p2), "Expected P2 MerchantShip!")
    assert_false(p1.play_captain(Captain.new("blue"), p2.merchant_ships_at_sea[0], p2),
                 "Captain must be in P1 hand!")
    assert_false(p1.play_captain(p1.hand[1], MerchantShip.new(2), p2), "MerchantShip must be in P2 sea!")
    # print(p1.hand[1])
    assert_false(p1.play_captain(p1.hand[1], p2.merchant_ships_at_sea[0], p2), "No PirateShip in play!")

    assert_true(p1.play_pirate(p1.hand[0], p2.merchant_ships_at_sea[0], p2), "Expected play to work!")
    assert_true(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2), "Expected play to work!")
    assert_false(p1.hand.include?(p1captain))
    assert_equal([[p1, p1pirate], [p1, p1captain]], p2.merchant_pirates[p2merchant],
                 "Expected to show played (Player,Attacker)")
  end

  def test_player_play_captain5
    Deck.set_instance()
    Admiral.set_instance()
    deck = Deck.get_instance()
    game = Game.new(deck)
    game.create_players($playerNames)

    p1 = game.players[0]
    p1pirate = PirateShip.new("blue", 2)
    p1captain = Captain.new("blue")
    p1.hand = [p1pirate, p1captain]

    p2 = game.players[1]
    p2pirate = PirateShip.new("green", 2)
    p2merchant = MerchantShip.new(2)
    p2.hand = [p2pirate]
    p2.merchant_ships_at_sea = [p2merchant]

    assert_true(p1.play_pirate(p1.hand[0], p2.merchant_ships_at_sea[0], p2), "Expected play to work!")
    assert_true(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2), "Expected play to work!")
    assert_false(p2.play_pirate(p2.hand[0], p2.merchant_ships_at_sea[0], p2),
                 "Cannot play a PirateShip after a Captain has been played!")
  end

  def test_player_play_captain6
    Deck.set_instance()
    Admiral.set_instance()
    deck = Deck.get_instance()
    game = Game.new(deck)
    game.create_players($playerNames)

    p1 = game.players[0]
    p1pirate = PirateShip.new("blue", 2)
    p1captain = Captain.new("blue")
    p1.hand = [p1pirate, p1captain]

    p2 = game.players[1]
    p2pirate = PirateShip.new("green", 2)
    p2captain = Captain.new("green")
    p2merchant = MerchantShip.new(2)
    p2.hand = [p2pirate, p2captain]
    p2.merchant_ships_at_sea = [p2merchant]

    assert_true(p1.play_pirate(p1.hand[0], p2.merchant_ships_at_sea[0], p2), "Expected play to work!")
    assert_true(p2.play_pirate(p2.hand[0], p2.merchant_ships_at_sea[0], p2), "Expected play to work!")
    assert_true(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2), "Expected play to work!")
    assert_true(p2.play_captain(p2.hand[0], p2.merchant_ships_at_sea[0], p2), "Expected play to work!")
    assert_false(p2.hand.include?(p2captain))
    assert_equal([[p1, p1pirate], [p2, p2pirate], [p1, p1captain], [p2, p2captain]],
                 p2.merchant_pirates[p2merchant], "Expected to show played (Player,Attacker)")
  end

  def test_player_play_admiral1
    Deck.set_instance()
    Admiral.set_instance()
    deck = Deck.get_instance()
    game = Game.new(deck)
    game.create_players($playerNames)
    p1 = game.players[0]
    p1.hand = [PirateShip.new("blue", 2), Captain.new('blue'), PirateShip.new("green", 2)]
    p1pirate1 = p1.hand[0]
    p1Captain = p1.hand[1]
    p1pirate2 = p1.hand[2]

    p2 = game.players[1]
    p2.hand = [Admiral.get_instance(), PirateShip.new("purple", 2),]
    p2Admiral = p2.hand[0]
    p2Pirate = p2.hand[1]
    p2.merchant_ships_at_sea = [MerchantShip.new(2)]

    assert_true(p1.play_pirate(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                'Expected to successfully play pirate ship')
    assert_true(p1.play_captain(p1.hand[0], p2.merchant_ships_at_sea[0], p2),
                'Expected to successfully play pirate ship')
    assert_equal([[p1, p1pirate1], [p1, p1Captain]], p2.merchant_pirates[p2.merchant_ships_at_sea[0]],
                 'Expected to see tuple in merchant_pirates instance')
    assert_true(p2.play_admiral(p2Admiral, p2.merchant_ships_at_sea[0]),
                'Expected to successfully play captain')
    assert_equal([[p1, p1pirate1], [p1, p1Captain], [p2, p2Admiral]], p2.merchant_pirates[p2.merchant_ships_at_sea[0]],
                 'Expected to see tuple in merchant_pirates instance')

  end

  def test_player_play_admiral2
    Deck.set_instance()
    Admiral.set_instance()
    deck = Deck.get_instance()
    game = Game.new(deck)
    game.create_players($playerNames)

    p1 = game.players[0]
    p1pirate = PirateShip.new("blue", 2)
    admiral = Admiral.get_instance()
    p1merchant = MerchantShip.new(2)
    p1.merchant_ships_at_sea = [p1merchant]
    assert_false(p1.play_admiral(Admiral.get_instance(), p1.merchant_ships_at_sea[0]),
                 "Admiral must be in P1 hand!")
    p1.hand = [p1pirate, admiral]

    assert_false(p1.play_admiral(p1.hand[0], p1.merchant_ships_at_sea[0]), "Expected Admiral!")
    assert_false(p1.play_admiral(p1.hand[1], p1.hand[0]), "Expected P1 MerchantShip!")
    assert_false(p1.play_admiral(p1.hand[1], MerchantShip.new(2)), "MerchantShip must be in P1 sea!")
    assert_true(p1.play_admiral(p1.hand[1], p1.merchant_ships_at_sea[0]), "Expected play to work!")
    assert_false(p1.hand.include?(admiral))
    assert_equal([[p1, admiral]], p1.merchant_pirates[p1merchant])

  end
end