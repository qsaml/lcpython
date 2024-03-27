class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # comment: no maps allowed of course because that would be too easy
        n = len(nums)
        # observe there are two cases: there is a missing integer from [1, n] or not
        # if there isn't, return n+1, and if there is, then mark each integer
        for i in range(n):
            # we only care if nums[i] is strictly positive
            # so mark those elements that are OUTSIDE the range from [1, n]
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        # now we mark each integer separately by flipping the sign of the index for that number
        for i in range(n):
            num = abs(nums[i])
            # if we encounter n+1, don't care
            if num > n:
                continue
            # accounts for zero index because we only care about stuff from [1, n]
            num -= 1
            # mark by converting this to a negative number
            if nums[num] > 0:
                nums[num] *= -1
        # finds the first nonnegative number according to the second condition above
        for i in range(n):
            # gap found at this point
            if nums[i] >= 0:
                return i + 1
        # no gaps found, so return according to the first condition
        return n + 1
