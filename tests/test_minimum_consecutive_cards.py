from algorithms.minimum_consecutive_cards import minimum_card_pickup


def test_minimum_card_pickup():
    expected = 2
    actual = minimum_card_pickup([1, 2, 6, 2, 1])
    assert expected == actual
