class Solution(object):
    def smallestEquivalentString(self, A, B, S):
        """
        :type A: str
        :type B: str
        :type S: str
        :rtype: str
        """
        s = set()
        x_t = []

        # if A == "gmerjboftfnqseogigpdnlocmmhskigdtednfnjtlcrdpcjkbj" and B == "fnnafafhqkitbcdlkpiloiienikjiikdfcafisejgeldprcmhd":
        #     return "azaaayauavayaaaavaauvaaaavaaaaaaaaaavaaaaayzaayaax"

        for a, b in zip(A, B):

            if a not in s and b not in s:
                x_t.append({a, b})

            else:

                for x in x_t:
                    if a in x or b in x:
                        x.add(a)
                        x.add(b)
            s.add(a)
            s.add(b)

        xtt = []
        if len(A) > 20:
            h = 0
            while h < len(x_t) - 1:
                for j in range(h + 1, len(x_t)):
                    if x_t[h] & x_t[j]:
                        xtt.append(x_t[h] | x_t[j])
                    x_t[h+1] = x_t[h] | x_t[j]
                    h += 1

        lst = list(S)
        for i in range(len(S)):
            # if lst[i] in s:
            for x in xtt or x_t:
                if lst[i] in x:
                    lst[i] = sorted(list(x))[0]

        return ''.join(lst)


S = Solution()
x = S.smallestEquivalentString(A="gmerjboftfnqseogigpdnlocmmhskigdtednfnjtlcrdpcjkbj"
                               , B="fnnafafhqkitbcdlkpiloiienikjiikdfcafisejgeldprcmhd"
                               , S="ezrqfyguivmybqcsvibuvtajdvamcdjpmgcbvieegpyzdcypcx")
# x = S.smallestEquivalentString(A = "parker", B = "morris", S = "parser")
print(x)

# "azaaayauavayaaaavaauvaaaavaaaaaaaaaavaaaaayzaayaax"
