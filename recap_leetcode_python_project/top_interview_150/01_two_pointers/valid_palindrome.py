class Solution(object):
    def isPalindrome(self, s):
        """
          >>> Solution.isPalindrome(Solution, "A man, a plan, a canal: Panama")
          True
          >>> Solution.isPalindrome(Solution, "race a car")
          False
          >>> Solution.isPalindrome(Solution, " ")
          True
        """
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # print(s[l], s[r])
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
