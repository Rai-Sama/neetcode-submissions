class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordrd = []
        for i, j in enumerate(strs):
            ordrd.append(["".join(sorted(j)), i])

        ordrd.sort()
        #print(ordrd)
        op = []
        i = 0
        #curr = ordrd[0]
        sublst = []
        while i < len(strs):
            curr = ordrd[i][0]
            while ordrd[i][0] == curr:
                sublst.append(strs[ordrd[i][1]])
                i += 1
                if i >= len(strs):
                    break
            
            op.append(sublst)
            sublst = []
                
        
        return op