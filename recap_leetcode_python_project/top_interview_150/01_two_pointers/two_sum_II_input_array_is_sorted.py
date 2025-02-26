class Solution(object):
    def twoSum(self, numbers, target):
        """
         >>> Solution.twoSum(Solution, [2,7,11,15], 9 )
         [1, 2]
         >>> Solution.twoSum(Solution, [2,3,4], 6 )
         [1, 3]
         >>> Solution.twoSum(Solution, [-1,0], -1 )
         [1, 2]
       """
        l, r = 0, len(numbers) - 1
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
