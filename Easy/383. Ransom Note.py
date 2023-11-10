from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = Counter(ransomNote)
        mag_dict = Counter(magazine)
        if ransom_dict & mag_dict == ransom_dict:
            return True
        return False