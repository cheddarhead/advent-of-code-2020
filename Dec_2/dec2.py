# Advent of Code - Dec 2nd

# Input = text file with a list of "passwords" and "rules"
#   Each line gives the password policy and then the password.
#   The password policy indicates the lowest and highest number
#   of times a given letter must appear for the password to be valid.
#   For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
# Goal = find numbers of valid passwords
# Output = single number which is count of valid passwords

from pathlib import Path

print("Starting Dec 2nd")

script_location = Path(__file__).absolute().parent
file_location = script_location / 'input.txt'
input_file = file_location.open()

all_lines = []
for line in input_file:
    all_lines.append(line)

input_file.close()

# Part 1:
valid_passwords = 0
invalid_passwords = 0

for line in all_lines:
    splitStr = line.split(": ")
    required_info = splitStr[0].split(" ")
    min_max = required_info[0].split("-")

    min_value = int(min_max[0])
    max_value = int(min_max[1])
    required_letter = required_info[1]
    password = splitStr[1]

    #print(str("Min: {}  Max: {}  RequiredLetter: {}  Password: {}").format(min_value, max_value, required_letter, password))

    countOfRequiredLetter = password.count(required_letter)
    if min_value <= countOfRequiredLetter <= max_value:
        valid_passwords = valid_passwords + 1
    else:
        invalid_passwords = invalid_passwords + 1

print(str("PART 1 -- Valid: {}  Invalid: {}  Sum: {}").format(valid_passwords, invalid_passwords, (valid_passwords + invalid_passwords)))

# Part 2:
valid_passwords = 0
invalid_passwords = 0

for line in all_lines:
    splitStr = line.split(": ")
    required_info = splitStr[0].split(" ")
    min_max = required_info[0].split("-")

    first_index = int(min_max[0]) - 1
    second_index = int(min_max[1]) - 1
    required_letter = required_info[1]
    password = splitStr[1]

    #print(str("Min: {}  Max: {}  RequiredLetter: {}  Password: {}").format(min_value, max_value, required_letter, password))

    count = 0
    if password[first_index] == required_letter:
        count = count + 1
    if password[second_index] == required_letter:
        count = count + 1

    if count == 1:
        valid_passwords = valid_passwords + 1
    else:
        invalid_passwords = invalid_passwords + 1

print(str("PART 2 -- Valid: {}  Invalid: {}  Sum: {}").format(valid_passwords, invalid_passwords, (valid_passwords + invalid_passwords)))