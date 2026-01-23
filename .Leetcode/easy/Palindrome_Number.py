class Solution:
    def isPalindrome(self) -> bool:
        x = int(input("Введите переменную: "))
        s = str(x)
        return s == s[::-1]

sol = Solution()
