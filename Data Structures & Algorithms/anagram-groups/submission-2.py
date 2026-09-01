class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op = defaultdict(list)

        for s in strs:
            cnt = [0] * 26

            for i in s:
                cnt[ord(i) - ord("a")] += 1
            
            op[tuple(cnt)].append(s)
        res = [v for k, v in op.items()]
        return res
        