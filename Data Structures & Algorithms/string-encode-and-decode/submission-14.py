class Solution:

    def encode(self, strs: List[str]) -> str:
        return "__word_separator__".join(strs) if strs else "__empty_input__"

    def decode(self, s: str) -> List[str]:
        return [] if s == "__empty_input__" else s.split("__word_separator__")
