class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        return r"EOW///EOW".join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split(r'EOW///EOW') if s else []
