class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int) # num => frequency
        for n in nums:
            freq[n] += 1
        
        arr = [None] * len(freq)
        for i, (n, f) in enumerate(freq.items()):
            arr[i] = (f, n)

        heapq.heapify(arr)
        return [v[1] for v in heapq.nlargest(k, arr)]