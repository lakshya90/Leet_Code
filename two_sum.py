'''
Problem : Given an array of integers, return indices of the two numbers such that they add up to a specific target.
Note : You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example : Given nums = [2, 7, 11, 15], target = 9,Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
Difficulty : Easy
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rtype = []
        for i in range(len(nums)):
		if nums.count(nums[i]) > 1 and target-nums[i]==nums[i]:
			rtype.append(i)
			rtype.append(len(nums) - nums.index(target-nums[i]) - 1)	
			return rtype
		elif target-nums[i] in nums and  (nums.index(target-nums[i])  > i):
			rtype.append(i)
			rtype.append(nums.index(target-nums[i]))
			return rtype
		else:
			continue
			
if __name__ == "__main__":
	print Solution().twoSum([3,2,4],6)
	print Solution().twoSum([3,3],6)
	print Solution().twoSum([2,4,5,6,7,8,9,10,12,14,16,18,20,32,43,52,23,43,1,4,5,6,8,9,15,4,3,6,8,50,25,43],43)
