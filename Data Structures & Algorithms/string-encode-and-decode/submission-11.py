class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        if strs == [""]:
            return r"000EOW///EOW"
        return r"EOW///EOW".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s == r"000EOW///EOW":
            return [""]
        res = s.split(r'EOW///EOW')
        if len(res)%2:
            res.append("")
        
        return res
