class Solution:

    def encode(self, strs: List[str]) -> str:
        return r"EOW///EOW".join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split(r'EOW///EOW')
