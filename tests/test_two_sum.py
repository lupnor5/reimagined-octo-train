from algorithms.two_sum import two_sum


def test_is_unique():
    assert two_sum([9, 2, 5, 6], 7) == [1, 2]
    assert two_sum([9, 2, 5, 6], 100) is None
