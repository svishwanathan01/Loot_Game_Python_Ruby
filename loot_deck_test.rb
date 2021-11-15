########## Sabareesh Vishwanathan ##########
########## 112585006 #############
########## SAVISHWANATH #############

require 'test/unit'
require 'test/unit/assertions'
require_relative "./loot.rb"

class MyTest < Test::Unit::TestCase
  def test_create_merchant_ship
    merchant_ship = MerchantShip.new(2)
    assert_equal(2, merchant_ship.get_value, "Value doesn't match")
    assert_not_equal(0, merchant_ship.get_value, "Value matches")
  end

  def test_create_pirate_ship
    pirateShip = PirateShip.new('green', 2)
    assert_equal(2, pirateShip.get_value, "Value doesn't match")
    assert_not_equal(0, pirateShip.get_value, "Value matches")
    assert_equal('green', pirateShip.get_color, "Color doesn't match")
    assert_not_equal('blue', pirateShip.get_color, "Color matches")
  end

  def test_create_captain
    captain = Captain.new('green')
    assert_equal('green', captain.get_color, "Color doesn't match")
    assert_not_equal('blue', captain.get_color, "Color matches")
  end
  def test_create_deck_and_admiral
    # deckie = Deck()
    deck = Deck.new
    for i in (0..24)
        assert_true(deck.cards[i].instance_of?(MerchantShip), 'Object is not of type MerchantShip')
    end
    for i in (25..72)
        assert_true(deck.cards[i].instance_of?(PirateShip), 'Object is not of type PirateShip')
    end
    for i in (73..76)
        assert_true(deck.cards[i].instance_of?(Captain), 'Object is not of type Captain')
    end
    assert_true(deck.cards[77].instance_of?(Admiral), 'Object is not of type Admiral')
  end
end
