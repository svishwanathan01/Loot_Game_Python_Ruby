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
end