class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1

        aList = []
        for val, freq in dict.items():
            aList.append([freq, val])
        aList.sort()

        res = []
        while len(res) < k:
            res.append(aList.pop()[1])

        return res