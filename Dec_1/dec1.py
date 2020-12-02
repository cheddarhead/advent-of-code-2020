# Advent of Code - Dec 1st

# Input = text file with a list of numbers
# Goal = find numbers that add up to 2020 and multiply them
# Output = single number which is the product of the numbers that sum to 2020

from pathlib import Path

print("Starting Dec 1st")

script_location = Path(__file__).absolute().parent
file_location = script_location / 'input.txt'
input_file = file_location.open()

all_numbers = []
for line in input_file:
    number = int(line)
    if 0 < number < 2020:
        all_numbers.append(number)

input_file.close()

# part 1:
for number in all_numbers:
    matchingNumber = 2020 - number
    if matchingNumber in all_numbers:
        print(str("PART 1 -- FOUND THE MATCH {} and {}").format(number, matchingNumber))
        sum = number + matchingNumber
        product = number * matchingNumber
        print(str("PART 1 -- Sum is {} and Product is {}").format(sum, product))

# part 2:
for first_number in all_numbers:
    for second_number in all_numbers:
        sumOfTwo = first_number + second_number
        if sumOfTwo < 2020:
            matchingNumber = 2020 - sumOfTwo
            if matchingNumber in all_numbers:
                print(str("PART 2 -- FOUND THE MATCH {} {} and {}").format(first_number, second_number, matchingNumber))
                sum = first_number + second_number + matchingNumber
                product = first_number * second_number * matchingNumber
                print(str("PART 2 -- Sum is {} and Product is {}").format(sum, product))
