
def removeDuplicates(nums):
    i = 0
    last = len(nums) - 1
    while i < last:
        if nums[i] == nums[i + 1]:
            del nums[i+1]
            last -= 1
            continue
        i += 1
    return last + 1

print(removeDuplicates([1,1,2,3,4,4,5]))

arr = [1,1,2]

print(removeDuplicates(arr))