
# pedantic solution
def romanToInt(s: str) -> int:
    r = 0
    i = 0
    l = len(s)
    while i < len(s):
        if s[i] == 'I':
            if (i + 1) <= l-1:
                if s[i+1] == 'V':
                    r += 4
                    i += 2
                    continue
                elif s[i+1] == 'X':
                    r += 9
                    i += 2
                    continue
            r += 1
        elif s[i] == 'V':
            r += 5
        elif s[i] == 'X':
            if (i + 1) <= l-1:
                if s[i+1] == 'L':
                    r += 40
                    i += 2
                    continue
                elif s[i+1] == 'C':
                    r += 90
                    i += 2
                    continue 
            r += 10
        elif s[i] == 'L':
            r += 50
        elif s[i] == 'C':
            if (i + 1) <= l-1:
                if s[i+1] == 'D':
                    r += 400
                    i += 2
                    continue
                elif s[i+1] == 'M':
                    r += 900
                    i += 2
                    continue
            r += 100
        elif s[i] == 'D':
            r += 500
        elif s[i] == 'M':
            r += 1000
        i += 1
    return r


# better solution

def romanToInt(s: str) -> int:
    # Create a hash table to map each roman numeral character to its corresponding value.
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # Initialize the result variable to zero.
    result = 0
    # Iterate over the input string from left to right.
    for i in range(len(s)):
        # If the current character is smaller than the next character, subtract its value from the result.
        if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
            result -= roman_to_int[s[i]]
        # Otherwise, add its value to the result.
        else:
            result += roman_to_int[s[i]]
    # Return the result.
    return result