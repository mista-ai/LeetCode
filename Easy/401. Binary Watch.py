bad = {'1100', '1101', '1110', '1111', '111100', '111101', '111110', '111111'}
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        answer = []
        for h in range(12):
            for m in range(60):
                if h.bit_count() + m.bit_count() == turnedOn:
                    answer.append(str(h) + ':' + (str(m) if m>=10 else '0' + str(m)))
        return answer