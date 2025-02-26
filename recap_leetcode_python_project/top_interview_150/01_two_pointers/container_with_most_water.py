class Solution(object):
    """
    >>> Solution.maxArea(Solution,[1,8,6,2,5,4,8,3,7])
    49
    >>> Solution.maxArea(Solution,[1,1])
    1
    """

    def maxArea(self, height):
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if l < r:
                l += 1
            elif l > r:
                r -= 1

        return max_area


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
