class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for val in nums:
            if val not in unique:
                unique.add(val)
            else:
                return True
        return False