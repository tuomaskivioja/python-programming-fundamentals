
# brute force


def twoSum(nums, target):
    # loop through each element in nums
    for i in range(len(nums)):
        # loop through each element after i in nums
        for j in range(i + 1, len(nums)):
            # check if the sum of the two elements equals target
            if nums[i] + nums[j] == target:
                # if it does, return the indices of the two elements
                return [i, j]
                

# optimal 

def twoSum(nums, target):
    # create a dictionary to store the complement of each element in nums
    complements = {6: 2, 5: 1}
    # loop through nums
    for i in range(len(nums)):
        # check if the complement of the current element exists in the dictionary
        if nums[i] in complements:
            # if it does, return the indices of the two elements that add up to target
            return [complements[nums[i]], i]
        else:
            # if it doesn't, add the complement of the current element to the dictionary
            complements[target - nums[i]] = i