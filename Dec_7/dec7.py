# Advent of Code - Dec 7th

# Input = text file with values that represent seat positions in an airplane
#   The first 7 chars are either F(ront) or B(ack)
#   The last 3 chars are either L(eft) or R(ight)
#   These represent a binary search to the seat
# Goal = There is a "UniqueSeatID" found by multiplying the row by 8, then adding the column
# Output = Part 1: The Highest "UniqueSeatID"
#          Part 2: My Seat. The only missing seat that is not at the very front or back of the plane

from pathlib import Path
from collections import defaultdict

print("Starting Dec 7th")

script_location = Path(__file__).absolute().parent
file_location = script_location / 'input.txt'
input_file = file_location.open()

all_bag_rules = []
for line in input_file:
    all_bag_rules.append(line)
input_file.close()


def count_bags(bag):
    global count
    global counted_bags

    if bag in counted_bags:
        print(str("bag {} was already counted").format(bag))
        count -= 1
    elif bag not in bag_map.keys():
        print(str("bag {} had no outside bags").format(bag))
        counted_bags.append(bag)
    else:
        count += len(bag_map[bag])
        counted_bags.append(bag)
        print(str("For inside bag: {} the outside bags are {}").format(bag, bag_map[bag]))
        print(str("current count is {}").format(count))

        for outside in bag_map[bag]:
            print(str("about to check {}").format(outside))
            count_bags(outside)


def count_bags2(bag, outside_count):
    global count2

    if bag not in bag_count_map.keys():
        print(str("bag {} had no inside bags").format(bag))
    else:
        print(str("For outside bag: {} the inside bags are {}").format(bag, bag_count_map[bag]))
        inside_count = 0
        for inside in bag_count_map[bag]:
            num = int(inside[0:1])
            desc = inside[1:]

            inside_count += num
            print(str("about to check {}").format(desc))
            count_bags2(desc, (outside_count * num))

        count2 += (outside_count * inside_count)


def read_next_word(rule, start_index, end_index):
    new_word = rule[start_index:end_index]
    new_start = end_index + 1
    try:
        new_end = rule.index(" ", end_index + 1)
    except ValueError as e:
        new_end = ValueError

    return new_word, new_start, new_end


# Part 1:
bag_map = defaultdict(list)

for rule in all_bag_rules:
    start_index = 0
    end_index = rule.index(" ")

    adj, start_index, end_index = read_next_word(rule, start_index, end_index)
    color, start_index, end_index = read_next_word(rule, start_index, end_index)
    outside_bag = adj+color
    # print(outside_bag)

    discard, start_index, end_index = read_next_word(rule, start_index, end_index)
    discard, start_index, end_index = read_next_word(rule, start_index, end_index)
    discard, start_index, end_index = read_next_word(rule, start_index, end_index)

    if discard == "no":
        continue

    adj, start_index, end_index = read_next_word(rule, start_index, end_index)
    color, start_index, end_index = read_next_word(rule, start_index, end_index)
    inside_bag = adj + color
    # print(inside_bag)
    bag_map[inside_bag].append(outside_bag)

    while end_index != ValueError:
        discard, start_index, end_index = read_next_word(rule, start_index, end_index)
        discard, start_index, end_index = read_next_word(rule, start_index, end_index)

        adj, start_index, end_index = read_next_word(rule, start_index, end_index)
        color, start_index, end_index = read_next_word(rule, start_index, end_index)
        inside_bag = adj + color
        # print(inside_bag)
        bag_map[inside_bag].append(outside_bag)

count = 0
counted_bags = []
count_bags("shinygold")

print(str("PART 1 -- How many bag colors can eventually contain at least one shiny gold bag: {}").format(count))
print("\n\n\n")


# Part 2:
bag_count_map = defaultdict(list)

for rule in all_bag_rules:
    start_index = 0
    end_index = rule.index(" ")

    adj, start_index, end_index = read_next_word(rule, start_index, end_index)
    color, start_index, end_index = read_next_word(rule, start_index, end_index)
    outside_bag = adj+color
    # print(outside_bag)

    discard, start_index, end_index = read_next_word(rule, start_index, end_index)
    discard, start_index, end_index = read_next_word(rule, start_index, end_index)
    count, start_index, end_index = read_next_word(rule, start_index, end_index)

    if count == "no":
        continue

    adj, start_index, end_index = read_next_word(rule, start_index, end_index)
    color, start_index, end_index = read_next_word(rule, start_index, end_index)
    inside_bag = count + adj + color
    # print(inside_bag)
    bag_count_map[outside_bag].append(inside_bag)

    while end_index != ValueError:
        discard, start_index, end_index = read_next_word(rule, start_index, end_index)
        count, start_index, end_index = read_next_word(rule, start_index, end_index)

        adj, start_index, end_index = read_next_word(rule, start_index, end_index)
        color, start_index, end_index = read_next_word(rule, start_index, end_index)
        inside_bag = count + adj + color
        # print(inside_bag)
        bag_count_map[outside_bag].append(inside_bag)

count2 = 0
count_bags2("shinygold", 1)

print(str("PART 2 -- How many individual bags are required inside your single shiny gold bag: {}").format(count2))

