class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        srted = [("".join(sorted(i)), indx) for indx, i in enumerate(strs)]
        
        ordrd = sorted(srted)

        res = [[strs[ordrd[0][1]]]]

        i = 1
    
        while i < len(ordrd):
            if ordrd[i][0] == ordrd[i-1][0]:
                res[-1].append(strs[ordrd[i][1]])
            else:
                res.append([strs[ordrd[i][1]]])
            i += 1
        return res