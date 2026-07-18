class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = []
        for index, num in enumerate(nums):
            sortedNums.append([num, index])

        sortedNums.sort()
        res = []

        l,r = 0, len(nums) - 1
        while l < r:
            if (sortedNums[l][0] + sortedNums[r][0] < target):
                l += 1
            elif (sortedNums[l][0] + sortedNums[r][0] > target):
                r -= 1
            else:
                res.append(sortedNums[l][1])
                res.append(sortedNums[r][1])
                break
        res.sort()
        return res