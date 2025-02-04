"""
Given an integer array cards, find the length of the shortest subarray that contains at least one duplicate.
If the array has no duplicates, return -1.
"""

from collections import defaultdict
from typing import List

"""
def minimum_card_pickup(cards: List[int]) -> int:
    dict = defaultdict(list)
    for i in range(len(cards)):
        dict[cards[i]].append(i)

    ans = float('inf')
    for key in dict: 
        arr = dict[key]
        for i in range(len(arr) -1 ): 
            ans = min(ans, arr[i + 1] - arr[i] )

    return ans if ans < float('inf') else -1             

"""


# improved version to optimize space complexity

def minimum_card_pickup(cards: List[int]) -> int:
    seen = defaultdict(int)
    ans = float('inf')
    for i in range(len(cards)):
        if cards[i] in seen:
            ans = min(ans, i - seen[cards[i]])
        seen[cards[i]] = i

    return ans if ans < float('inf') else - 1
