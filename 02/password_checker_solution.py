MIN_CHARACTERS = 7
SPECIAL_CHARS = ['!', '?', '#', '@', '$', '*']
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

passwords = ['helloWorld', 'imcisamazing69', 'ilovecookies!23', 'python1s@mazingLanguage']

HAS_SPECIAL_CHAR = False
HAS_NUMBER = False
HAS_7_CHARS = False

for password in passwords:
    for num in NUMBERS:
        if (str(num)) in password:
            HAS_NUMBER = True
            break
    for char in SPECIAL_CHARS:
        if char in password:
            HAS_SPECIAL_CHAR = True
            break
    if len(password) >= MIN_CHARACTERS:
        HAS_7_CHARS = True
    if HAS_NUMBER and HAS_7_CHARS and HAS_SPECIAL_CHAR:
        print(f'{password} is a valid password')
    else:
        print(f'{password} is not a valid password')
