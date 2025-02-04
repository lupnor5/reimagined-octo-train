"""
Given an array of integers nums, find the maximum value of nums[i] + nums[j],
where nums[i] and nums[j] have the same digit sum (the sum of their individual digits). 
Return -1 if there is no pair of numbers with the same digit sum.
"""
from collections import defaultdict
from typing import List

"""
def max_sum(nums: List[int]) -> int:
    def get_digit_sum(num): 
        digit_sum = 0
        while num: 
            digit_sum+= num%10
            num //=10
        return  digit_sum

    dict = defaultdict(list)
    for num in nums: 
        digit_sum = get_digit_sum(num)
        dict[digit_sum].append(num)

    ans = -1

    for key in dict:
        curr = dict[key]
        if len(curr) > 1:
            curr.sort(reverse=True)
            ans = max(ans, curr[0] + curr[1])
    return ans        
"""


# better complexity because it only stores the maximum number in the map
def max_sum(nums: List[int]) -> int:
    def get_digit_sum(n):
        sum_ = 0
        while n:
            sum_ += n % 10
            n //= 10
        return sum_

    seen = defaultdict(int)
    ans = -1
    for num in nums:
        digit_sum = get_digit_sum(num)
        if digit_sum in seen:
            ans = max(ans, num + seen[digit_sum])
        seen[digit_sum] = max(seen[digit_sum], num)
    return ans
