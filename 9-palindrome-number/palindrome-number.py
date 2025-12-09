class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        z=str(x)
        newstring=z[::-1]
        if newstring==z:
            return True
        else:
            return False
        