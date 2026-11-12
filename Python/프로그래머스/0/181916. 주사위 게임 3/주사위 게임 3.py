def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = [nums.count(num) for num in nums]
    if max(counts) == 4:
        return a * 1111
    elif max(counts) == 3:
        return (10 * nums[counts.index(3)] + nums[counts.index(1)]) ** 2
    elif max(counts) == 2:
        if min(counts) == 2:
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else:
            return (a * b * c * d) / nums[counts.index(2)] ** 2
    else:
        return min(nums)