from algorithms.max_sum import max_sum


def test_max_sum():
    expected = 54
    actual = max_sum([18, 43, 36, 13, 7])
    assert actual == expected
