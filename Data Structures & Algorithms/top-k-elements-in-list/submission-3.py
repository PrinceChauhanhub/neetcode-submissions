class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        
        return [sorted_items[i][0] for i in range(k)]