def longest_consecutive_sequence(nums: list[int]) -> int:
    num_set: set = set(nums)
    longest: int = 0

    for n in nums:
        if (n - 1) not in num_set:
            length = 1
            while (n + length) in num_set:
                length += 1
            longest = max(length, longest)
    return longest
