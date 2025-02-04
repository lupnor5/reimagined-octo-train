"""
Given an array of strings strs, group the anagrams together.

For example, given strs = ["eat","tea","tan","ate","nat","bat"], return [["bat"],["nat","tan"],["ate","eat","tea"]].
"""
from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
     groups = defaultdict(list)
     for s in strs: 
          key = "".join(sorted(s))
          groups[key].append(s)

     return list(groups.values())
     

