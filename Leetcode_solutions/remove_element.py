

def remove_element(nums, target):

    result = []
    for number in nums:
        if number == target:
            continue
        else:
            result.append(number)
    return result


print(remove_element([2,8,6,3,3,5,3,2], 2))