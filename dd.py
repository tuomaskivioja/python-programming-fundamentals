
import time

def find_duplicates(numbers):
    unique_numbers = set()
    duplicates = []
    start = time.time()
    for number in numbers:
        if number in unique_numbers:
            duplicates.append(number)
        else:
            unique_numbers.add(number)
    end = time.time()
    print(f"Algorithm took {end - start} seconds to run.")
    return duplicates