class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        srtd = ["".join(sorted(i)) for i in strs]
        op = dict()
        for i in range(n):
            #print(srtd[i])
            if srtd[i] in op:
                op[srtd[i]].append(i)
            else:
                op[srtd[i]] = [i]
        res = []
        for _, v in op.items():
            res.append([strs[i] for i in v])
        return res