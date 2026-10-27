class Solution:

    def encode(self, strs: List[str]) -> str:
        return "__word_separator__".join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split("__word_separator__")
