class Solution:

    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        if not deck:
            return []
        deck.sort()
        ans = [deck.pop()]
        print("ans", ans)
        while deck:
            temp = ans.pop()
            ans = [deck.pop(), temp] + ans
            print("ans", ans)
        return ans


S = Solution()
a = S.deckRevealedIncreasing([17,13,11,2,3,5,7])
print(a)


class Solution2:

    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        if not deck:
            return []
        deck.sort()

        l = len(deck)
        i = (l+1)//2
        a = deck[:i]
        b = deck[i:]

        c = []
        for i in a:
            c.append(i)
            c.append(b[0])

