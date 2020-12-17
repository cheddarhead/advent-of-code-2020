# Advent of Code - Dec 6th

# Input = text file with answers to customs questions from each group of people
#    There are questions a-z and each line contains the questions someone answered 'yes' to
#    Each group is separated by a blank line. For instance:
#       abc
#
#       a
#       b
#       c
#   The first group is one person who answered yes to "abc" and the second group is
#   3 people who each answered yes to one question
# Goal = Count the number of questions answered "yes" to with different rules
# Output = Part 1: The sum of all questions that anyone in a group answered "yes" to
#          Part 2: The sum of all questions that everyone in a group answered "yes" to

from pathlib import Path

print("Starting Dec 6th")

# Part 1:
script_location = Path(__file__).absolute().parent
file_location = script_location / 'input.txt'
input_file = file_location.open()

records_with_any_yes = []
record_string = ""

for line in input_file:
    if line != "\n":
        line = line.rstrip()

        for char in line:
            if char not in record_string:
                record_string += char
    else:
        record_string = record_string.strip()
        records_with_any_yes.append(record_string)
        record_string = ""
input_file.close()

any_yes_count = 0

for record in records_with_any_yes:
    print(record)
    print(len(record))
    any_yes_count += len(record)

print(str("PART 1 -- Questions to which Anyone in a group responded with Yes: {}").format(any_yes_count))


# Part 2:
script_location = Path(__file__).absolute().parent
file_location = script_location / 'input.txt'
input_file = file_location.open()

records_with_all_yes = []
group_strings = []
record_string = ""

for line in input_file:
    if line != "\n":
        line = line.rstrip()
        line = "".join(set(line))
        group_strings.append(line)
    else:
        if len(group_strings) > 1:
            for char in group_strings[0]:
                i = 1
                while i < len(group_strings):
                    if char not in group_strings[i]:
                        group_strings[0] = group_strings[0].replace(char, "")
                    i += 1

        record_string = group_strings[0]
        record_string = record_string.strip()
        records_with_all_yes.append(record_string)

        group_strings = []
        record_string = ""
input_file.close()

all_yes_count = 0

for record in records_with_all_yes:
    print(record)
    print(len(record))
    all_yes_count += len(record)

print(str("PART 2 -- Questions to which Everyone in a group responded with Yes: {}").format(all_yes_count))
