# -*- coding: utf-8 -*-

'''
给定一个整数数列，找出其中和为特定值的那两个数。

你可以假设每个输入都只会有一种答案，同样的元素不能被重用。

示例:
	给定 nums = [2, 7, 11, 15], target = 9
	因为 nums[0] + nums[1] = 2 + 7 = 9
	所以返回 [0, 1]
'''

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for val in nums:
        rest = target - val
        if rest in nums:
            indexArr = [nums.index(val), nums.index(rest)]
            return indexArr

indexs = twoSum([3, 4, 5, 6], 9)
print indexs
