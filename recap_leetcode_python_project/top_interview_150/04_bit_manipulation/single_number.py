class Solution(object):
    """
    >>> Solution.singleNumber(Solution,[2,2,1])
    1
    >>> Solution.singleNumber(Solution,[4,1,2,1,2])
    4
    >>> Solution.singleNumber(Solution,[1])
    1
    """

    def singleNumber(self, nums):
        res = 0
        for n in nums:
            res = res ^ n  # XOR of two same numbers always result in cancellation
        return res


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
