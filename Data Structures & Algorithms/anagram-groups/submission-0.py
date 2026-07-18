class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for word in strs:
            sortedS = ''.join(sorted(list(word)))
            if sortedS not in dict:
                dict[sortedS] = [word]
            else:
                dict[sortedS].append(word)

        res = []
        for sub in dict.values():
            res.append(sub)
        return res