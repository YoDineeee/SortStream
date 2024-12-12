class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hash_map = {}
        res = majority = 0

        for n in nums:
            
            hash_map[n] = hash_map.get(n, 0) + 1
            
            
            if hash_map[n] > majority:
                res = n
                majority = hash_map[n]
        return res