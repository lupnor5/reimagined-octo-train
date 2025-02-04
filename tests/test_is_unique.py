from algorithms.is_unique import is_unique


def test_is_unique():
    assert is_unique("abcdef") is True
    assert is_unique("abcdefaa") is False
