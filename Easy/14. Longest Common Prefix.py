class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = 0
        smallest = min(strs, key=len)
        stop = False
        for i in range(len(smallest)):
            for word in strs:
                # print(word[i], smallest[i], word[i] != smallest[i])
                if word[i] != smallest[i]:
                    stop = True
                    break
            if stop:
                break
            result += 1
        return smallest[:result]