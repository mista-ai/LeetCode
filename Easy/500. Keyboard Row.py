class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}

        return [word for word in words if set(word.lower()).issubset(row1)
                or set(word.lower()).issubset(row2)
                or set(word.lower()).issubset(row3)]