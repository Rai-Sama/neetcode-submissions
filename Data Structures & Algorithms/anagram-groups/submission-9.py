class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        srtd = [(sorted(i), indx) for indx, i in enumerate(strs)]

        ordrd = sorted(srtd)
        ans = []
        curr = ("", False)
        for i in ordrd:
            if curr[0] and curr[0] == i[0]:
                ans[-1].append(strs[i[1]])
            else:
                if curr[1] != False and curr[0] == i[0]:
                    ans[-1].append(strs[i[1]])
                else:
                    curr = i
                    ans.append([strs[curr[1]]])

        return ans