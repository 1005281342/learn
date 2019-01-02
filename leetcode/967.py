class Solution:

    def __init__(self):

        self.s = dict()

    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """

        for x in range(K, 10):

            mb = x-K
            self.s[str(x)] = str(mb)
        min_num = 10 ** (N-1)

        nums = set()
        if N % 2 == 0:
            t = -1
        else:
            t = N
        for a, b in self.s.items():
            num_str = ""
            num_str_2 = ""
            while len(num_str) < N:
                num_str += a
                num_str += b
                num_str_2 += b
                num_str_2 += a
            num_1 = int(num_str[:t])
            num_2 = int(num_str_2[:t])
            if num_1 >= min_num:
                nums.add(num_1)
            if num_2 >= min_num:
                nums.add(num_2)
        a = list(nums)
        a.sort()
        return a


aa = Solution()
b = aa.numsSameConsecDiff(N = 3, K = 2)
print(b)
