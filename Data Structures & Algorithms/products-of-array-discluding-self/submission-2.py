class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            mul = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                mul *= nums[j]
            out.append(mul)
        return out