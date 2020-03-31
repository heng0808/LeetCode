class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        import heapq
        head = []
        for val in nums:
            heapq.heappush(head, v)
        values = heapq.nlargest(k, nums)
        values.reverse()
        heapq.heappop()
        return None if len(values) == 0 else values[0]


print(Solution().findKthLargest([3,2,1,5,6,4], 2))