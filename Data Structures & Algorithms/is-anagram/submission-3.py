class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s, list_t = [], []
        for i in range(len(s)):
            list_s.append(s[i])
        for i in range(len(t)):
            list_t.append(t[i])
        if len(list_s) != len(list_t):
            return False
        if len(list_s) > len(list_t): max_list, other_list = list_s, list_t
        else: max_list, other_list = list_t, list_s
        for i in max_list:
            if i in other_list:
                other_list.remove(i)
        print(list_s)
        print(list_t)
        if len(other_list) == 0:
            return True
        return False