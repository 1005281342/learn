class Solution:
    def isPalindrome(self, s: str) -> bool:
        UsChar = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                  't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', }
        s = s.lower()
        for char in s:
            if char not in UsChar:
                s = s.replace(char, '')
        return s == s[::-1]


S = Solution()
a = S.isPalindrome("A man, a plan, a canal: Panama")
print(a)
