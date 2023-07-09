def twoSum(self, nums: list[int], target: int) -> list[int]:
    differences = {}

    for index, value in enumerate(nums):
        difference = target - value
        if difference in differences:
            return [differences[difference], index]
        else:
            differences[value] = index
