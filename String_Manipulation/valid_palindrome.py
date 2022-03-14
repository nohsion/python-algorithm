class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for i in s:
            if i.isalnum():
                string.append(i.lower())
        string = ''.join(string)
        if string == string[::-1]:
            return True
