# Advent of Code - Dec 3rd

# Input = text file with forest of trees(#) and open space(.)
#   The input represents a single instance of the forest pattern,
#   but it repeats itself infinitely.
# Goal = find the number of trees which we would encounter while
#   "sliding" down to the bottom row
# Output = number of trees encountered in various "slides"

from pathlib import Path

print("Starting Dec 3rd")

script_location = Path(__file__).absolute().parent
file_location = script_location / 'input.txt'
input_file = file_location.open()

all_rows = []
for line in input_file:
    all_rows.append(line)
input_file.close()

row_length = len(all_rows[0]) - 1
last_row = len(all_rows)

# Class Definitions:
class Slope:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Part 1:
current_x = 0
current_y = 0
tree_counter = 0

for row in all_rows:
    single_row_x = current_x % row_length
    if row[single_row_x] == '#':
        tree_counter = tree_counter + 1

    current_x = current_x + 3
    current_y = current_y + 1

    if current_y == last_row:
        break

print(str("Position At End {}, {}").format(current_x, current_y))
print(str("PART 1 -- Trees Encountered {}").format(tree_counter))


# Part 2:
all_slopes = [Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]
trees_encountered = []

for slope in all_slopes:
    current_x = 0
    current_y = 0
    tree_counter = 0
    row_count = 0

    for row in all_rows:
        if row_count % slope.y == 0:
            single_row_x = current_x % row_length
            if row[single_row_x] == '#':
                tree_counter = tree_counter + 1

            current_x = current_x + slope.x
            current_y = current_y + slope.y

            if current_y >= last_row:
                print(str("Position At End {}, {}").format(current_x, current_y))
                trees_encountered.append(tree_counter)
                break
        row_count += 1

combined_trees_encountered = 1
for trees in trees_encountered:
    print(str("Trees Encountered {}").format(trees))
    combined_trees_encountered = combined_trees_encountered * trees

print(str("PART 2 -- Product of Trees Encountered {}").format(combined_trees_encountered))
