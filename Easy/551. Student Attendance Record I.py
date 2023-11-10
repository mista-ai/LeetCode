class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count, late_strike = 0, 0
        prev_late = -1

        for i, x in enumerate(s):
            if x == 'A':
                absent_count += 1
                if absent_count == 2:
                    return False

            elif x == 'L':
                # print(f'{i} -> {prev_late} -> {late_strike}')
                if i - prev_late > 1:
                    prev_late = i
                    late_strike = 1

                else:
                    late_strike += 1
                    prev_late = i
                    if late_strike == 3:
                        return False

        return True