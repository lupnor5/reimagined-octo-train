from algorithms.group_anagrams import group_anagrams


def test_group_anagrams():
    expected = [['arresto', 'rastreo'], ['saco', 'caso', 'cosa'], ['programa'],['gato', 'toga'], ['chow']]
    actual = group_anagrams(['saco', 'arresto', 'programa', 'rastreo', 'caso', 'cosa', 'gato', 'toga', 'chow'])
    # Convert inner lists to sets and then compare as sets of sets
    assert set(map(frozenset, actual)) == set(map(frozenset, expected))
