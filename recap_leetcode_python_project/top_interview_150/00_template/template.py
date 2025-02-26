class Solution(object):
    """
    >>> Solution.do_something(Solution,"hello world")
    'hello world'
    """

    def do_something(self, s):
        return s


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
