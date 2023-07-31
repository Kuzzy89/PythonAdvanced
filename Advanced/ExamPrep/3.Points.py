def fix_calendar(nums):
    for i in range(len(nums)):
        for r in range(len(nums)):
            if nums[i] < nums[r]:
                nums[i], nums[r] = nums[r], nums[i]

    return nums


numbers = [3, 5, 6, 7, 1]
fixed = fix_calendar(numbers)
print(fixed)