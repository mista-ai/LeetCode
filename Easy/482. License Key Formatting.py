class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.split('-')
        S = (('').join(s)).upper()
        remainder = len(S) % k

        first_grp = [S[: remainder]]
        other_grps = [S[i: i + k] for i in range(remainder, len(S), k)]

        if remainder:
            return "-".join(first_grp + other_grps)

        return "-".join(other_grps)
