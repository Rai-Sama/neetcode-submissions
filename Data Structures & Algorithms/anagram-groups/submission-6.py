class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        srtd = [("".join(sorted(i)), indx) for indx, i in enumerate(strs)]

        srtd.sort()

        i, n = 1, len(srtd)
        
        res = [[strs[srtd[0][1]]]]

        while i < n:
            if srtd[i][0] == srtd[i-1][0]:
                res[-1].append(strs[srtd[i][1]])
            else:
                res.append([strs[srtd[i][1]]])
            
            i += 1

        return res
