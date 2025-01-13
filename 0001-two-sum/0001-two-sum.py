class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        answer = []

        for i in range(len(nums)):
            for x in range(len(nums)):
                if i == x:
                    continue
                if nums[i] + nums[x] == target:
                    answer.append(i)
                    answer.append(x)
                    return answer

        