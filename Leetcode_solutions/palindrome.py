
# ok solution

def isPalindrome(x: int):
    x_string = str(x)
    x_string_reversed = x_string[::-1]
    if x_string == x_string_reversed:
        return True
    return False



# better solution

def isPalindrome2(x: int):
    x_string = str(x)
    start = 0
    end = len(x_string) - 1
    while start < end:
        if x_string[start] == x_string[end]:
            start += 1
            end -= 1
            continue
        else:
            return False
    return True

print(isPalindrome2(12))