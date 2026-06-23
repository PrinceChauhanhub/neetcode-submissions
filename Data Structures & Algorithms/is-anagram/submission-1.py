class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        test = list(s)
        for x in t:
            if x in test:
                test.remove(x)
            else:
                return False

        if len(test)!=0:
            return False
        return True