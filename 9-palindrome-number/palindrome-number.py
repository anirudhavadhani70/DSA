class Solution:
    def isPalindrome(self, x: int) -> bool:
        # palindrome
        z=str(x)
        newstring=z[::-1]
        if newstring==z:
            return True
        else:
            return False
        