

# @hetang
# T https://leetcode-cn.com/contest/weekly-contest-112/problems/minimum-increment-to-make-array-unique/
class Solution(object):
    """
        A -> res
        A[0] == res[0]
        A[2] > res[2]
        A[6] < res[6]

    """
    def minIncrementForUnique(self, A):         # A: 1 3 5 7 7 3 9
                                                # res: 1 3 4 5 7 8 9  ,  inc 2
        if len(A) == 0:
            return 0
        A.sort()    # 1 3 3 5 7 7 9
        bound = A[0]
        inc = 0
        for a in A:
            if a == bound:  # A[0], A[0]+1, ...
                bound += 1
            elif a > bound:     # A[x]+1
                bound = a + 1
            else:       # a < bound
                inc += (bound - a)
                bound += 1
        return inc
