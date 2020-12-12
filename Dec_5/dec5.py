# Advent of Code - Dec 5th

# Input = text file with values that represent seat positions in an airplane
#   The first 7 chars are either F(ront) or B(ack)
#   The last 3 chars are either L(eft) or R(ight)
#   These represent a binary search to the seat
# Goal = There is a "UniqueSeatID" found by multiplying the row by 8, then adding the column
# Output = Part 1: The Highest "UniqueSeatID"
#          Part 2: My Seat. The only missing seat that is not at the very front or back of the plane

# F = 0 / B = 1
# L = 0 / R = 1

from pathlib import Path

print("Starting Dec 5th")

script_location = Path(__file__).absolute().parent
file_location = script_location / 'input.txt'
input_file = file_location.open()

all_seats = []
for line in input_file:
    all_seats.append(line)
input_file.close()


# Part 1:
highest_unique_seat_id = 0

for seat in all_seats:
    row_str = seat[0:7]
    col_str = seat[7:10]

    row_bin_str = ""
    for char in row_str:
        if char == "F":
            row_bin_str += "0"
        elif char == "B":
            row_bin_str += "1"

    col_bin_str = ""
    for char in col_str:
        if char == "L":
            col_bin_str += "0"
        elif char == "R":
            col_bin_str += "1"

    row_int = int(row_bin_str, 2)
    col_int = int(col_bin_str, 2)
    unique_seat_id = (row_int * 8) + col_int
    highest_unique_seat_id = max(highest_unique_seat_id, unique_seat_id)

    # print(str("row_bin: {}  col_bin: {}").format(row_bin_str, col_bin_str))
    # print(str("row_int: {}  col_int: {}").format(row_int, col_int))
    # print(str("unique_seat_id: {}").format(unique_seat_id))

print(str("PART 1 -- Highest Unique Seat Id: {}").format(highest_unique_seat_id))


# Part 2:
possible_seats = list(range(1001))

for seat in all_seats:
    row_str = seat[0:7]
    col_str = seat[7:10]

    row_bin_str = ""
    for char in row_str:
        if char == "F":
            row_bin_str += "0"
        elif char == "B":
            row_bin_str += "1"

    col_bin_str = ""
    for char in col_str:
        if char == "L":
            col_bin_str += "0"
        elif char == "R":
            col_bin_str += "1"

    row_int = int(row_bin_str, 2)
    col_int = int(col_bin_str, 2)
    unique_seat_id = (row_int * 8) + col_int

    possible_seats.remove(unique_seat_id)

for remaining_seat in possible_seats:
    print(remaining_seat)

    one_seat_less = remaining_seat - 1
    one_seat_more = remaining_seat + 1
    if one_seat_less not in possible_seats and one_seat_more not in possible_seats:
        print(str("PART 2 -- My Seat is: {}").format(remaining_seat))
