# brute force

def threeSum(nums, target):
    res = []
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j]+nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
    return res



# optimal

def threeSum(nums, target):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:  # skip duplicate values
            continue
        left, right = i+1, len(nums)-1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == target:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:  # skip duplicate values
                    left += 1
                while left < right and nums[right] == nums[right-1]:  # skip duplicate values
                    right -= 1
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    return res