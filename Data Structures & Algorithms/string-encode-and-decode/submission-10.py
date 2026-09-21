class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        if strs == [""]:
            return r"EOW///EOW"
        return r"EOW///EOW".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s == r"EOW///EOW":
            return [""]
        return s.split(r'EOW///EOW')
