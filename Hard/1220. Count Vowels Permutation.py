class Solution:
    def countVowelPermutation(self, n: int) -> int:
        BIG = 1_000_000_007

        if n > 125:
            trans = [[0,1,1,0,1],[1,0,1,0,0],[0,1,0,1,0],[0,0,1,0,0],[0,0,1,1,0]]
            def matmul(m1, m2):
                c = [[0] * 5 for _ in range(5)]
                for i in range(5):
                    for j in range(5):
                        for k in range(5):
                            c[i][j] += m1[i][k] * m2[k][j]
                        c[i][j] %= BIG
                return c
            def matpow(mat, n):
                ans = None
                for i in f"{n:b}":
                    if ans is None:
                        ans = mat
                        continue
                    ans = matmul(ans, ans)
                    if i == '1':
                        ans = matmul(ans, mat)
                return ans
            # print(matmul(trans, trans))
            result = matpow(trans, n - 1)
            ans = sum(sum(r) for r in result)
            return ans % BIG
        else:
            a = e = i = o = u = 1
            for k in range(n - 1):
                ii = (a + e + o + u) % BIG
                ee = (a + i) % BIG
                o = (i + u) % BIG
                u = a
                a = e
                i = ii
                e = ee
            return (a + e + i + o + u) % BIG