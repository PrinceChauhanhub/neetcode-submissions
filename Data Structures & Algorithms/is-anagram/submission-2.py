class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = dict()
        t_dict = dict()

        for c in s:
            s_dict[c] = s_dict.get(c,0)+1
        for d in t:
            t_dict[d] = t_dict.get(d,0)+1
        return s_dict == t_dict