
'''
You are given a one dimensional array that may contain both
positive and negative integers, find the sum of contiguous
subarray of numbers which has the largest sum.
For example, if the given array is {-2, -5, 6, -2, -3, 1, 5, -6}, then
the maximum subarray sum is 7 (see highlighted elements).
How can you solve it using divide and conquer?
What would be recurrence relation for the same?
1. Divide the given array in two halves
2. Return the maximum of following three
● Maximum subarray sum in left half (a recursive call)
● Maximum subarray sum in right half (a recursive call)
● Maximum subarray sum such that the subarray
crosses the midpoint
Maximum SubArray Sum
'''


def max_sub_arr(nums):
    if len(nums) <= 1:
        return nums[0] if nums else 0
    mid = len(nums) // 2
    left_max = max_sub_arr(nums[:mid]) # max subarr sum for left half
    right_max = max_sub_arr(nums[mid:]) # max subarr sum for right half
    cross_max = max_crossing_sum(nums, mid) # max subarr cross
    return max(left_max, right_max, cross_max)
def max_crossing_sum(nums, mid):
    left_sum = float('-inf') # set left_sum to a very small number, in this case -inf, to compare to total sum for sides
    total = 0
    for i in range(mid-1, -1, -1):
        total += nums[i]
        left_sum = max(left_sum,total)
    right_sum = float('-inf')
    total = 0
    for i in range(mid, len(nums)):
        total += nums[i]
        right_sum = max(right_sum, total)
    return left_sum + right_sum # return total sum of left and right sides
# example usage
nums = [-2, -5, 6, -2, -3, 1, 5, -6]

res = max_sub_arr(nums)
print(res) # Output: 7