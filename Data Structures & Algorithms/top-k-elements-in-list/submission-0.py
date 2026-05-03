class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        sortedList = []
        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
        for key, value in frequency.items():
            for i in range(len(sortedList)):
                if key in sortedList: continue
                if frequency[sortedList[i]] > value:
                    continue
                else:
                    sortedList.insert(i, key)
            if key not in sortedList:
                sortedList.append(key)
        print(sortedList)
        return sortedList[:k]