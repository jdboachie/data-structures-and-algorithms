def contains_duplicate(self, nums: list[int]) -> bool:
    nums_dict = {}

    for num in nums:
        if nums_dict.get(num, False):
            return True
        else:
            nums_dict[num] = True

    return False
