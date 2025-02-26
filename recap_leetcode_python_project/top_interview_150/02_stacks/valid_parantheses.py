class Solution(object):
    """
    >>> Solution.isValid(Solution,"()")
    True
    >>> Solution.isValid(Solution,"()[]{}")
    True
    >>> Solution.isValid(Solution,"(]")
    False
    >>> Solution.isValid(Solution,"([])")
    True
    """

    def isValid(self, s):
        lookup = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for b in s:
            if b in lookup.values():
                stack.append(b)
            elif stack and lookup[b] == stack[-1]:
                stack.pop()
            else:
                return False

        return stack == []


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
