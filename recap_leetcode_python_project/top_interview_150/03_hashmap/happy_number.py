class Solution(object):
    """
    >>> Solution.isHappy(Solution,19)
    True
    >>> Solution.isHappy(Solution,2)
    False
    """

    def isHappy(self, n):

        # --- utility
        def sum_of_squares(num):
            sum = 0
            for c in str(num):
                sum += int(c) ** 2
            return sum

        # --- logic
        seen = set()
        while n != 1:
            n = sum_of_squares(n)

            if n in seen:
                return False
            else:
                seen.add(n)
        return True

        # ----- alternative approach using slow and fast
        # slow_list = []
        # fast_list = []
        # slow, fast = n, sum_of_squares(n)
        # print(f'slow: {slow}')
        # slow_list.append(slow)
        # print(f'fast: {fast}')
        # fast_list.append(fast)
        #
        # while slow != fast:
        #     slow = sum_of_squares(slow)
        #     fast = sum_of_squares(sum_of_squares(fast))
        #     print(f'slow: {slow}')
        #     print(f'fast: {fast}')
        #     slow_list.append(slow)
        #     fast_list.append(fast)
        #
        # print(f'slow_list :{slow_list}')
        # print(f'fast_list :{fast_list}')
        # return True if slow == 1 else False


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
