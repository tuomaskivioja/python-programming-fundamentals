def removeElement(nums, val) -> int:
    if val not in nums:
            return len(nums)
    if len(nums) == 1 and val in nums:
        return 0
    idx = 0
    j = len(nums) - 1
    while idx <= j:
        if nums[idx] == val:
            del nums[idx]
            j -= 1
        else:
            idx += 1
    return idx