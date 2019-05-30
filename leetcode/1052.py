class Solution:
    def maxSatisfied(self, customers: list, grumpy: list, X: int) -> int:

        k, v = 0, 0
        for i in range(len(grumpy) + 1 - X):
            # print(customers[i:i + X])
            a = sum((x for x, y in zip(customers[i:i + X], grumpy[i:i + X]) if y > 0))
            if a > k:
                k, v = a, i

        index = v
        for ii in range(index, index + X):
            grumpy[ii] = 0
        # print(grumpy)
        return sum((x for x, y in zip(customers, grumpy) if y == 0))


S = Solution()
print(S.maxSatisfied())
