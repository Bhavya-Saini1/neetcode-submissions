class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = strs.copy()
        grouped = []
        for i in range(len(strs)):
            if strs[i] in grouping:
                iGroup = [strs[i]]
                for j in range(len(strs)):
                    isAnagram = True
                    if len(strs[i]) != len(strs[j]) or i == j:
                        continue
                    countI, countJ = {}, {}
                    for k in range(len(strs[i])):
                        countI[strs[i][k]] = 1 + countI.get(strs[i][k], 0)
                        countJ[strs[j][k]] = 1 + countJ.get(strs[j][k], 0)
                    for c in countI:
                        if countI[c] != countJ.get(c, 0):
                            isAnagram = False
                    if isAnagram:
                        iGroup.append(strs[j])
                        if strs[j] in grouping: grouping.remove(strs[j])
                grouping.remove(strs[i])
                grouped.append(iGroup)
        
        return grouped