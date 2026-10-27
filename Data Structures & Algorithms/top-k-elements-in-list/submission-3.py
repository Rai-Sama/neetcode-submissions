class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [(0, -1001)]*k

        cnts = {}
        for i in nums:
            if i in cnts:
                cnts[i] += 1
            else:
                cnts[i] = 1
            
            
        for i, v in cnts.items():
            j = 0
            while j < k and v > freqs[j][0]:
                    if j:
                        freqs[j-1] = freqs[j]
                        freqs[j] = (v, i)
                    else:
                        freqs[j] = (v, i)
                    j += 1
            
            
        return [i[1] for i in freqs]
                
        
            