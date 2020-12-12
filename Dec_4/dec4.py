# Advent of Code - Dec 4th

# Input = text file with a info about various passport info
#   There are 8 passport fields:
#      byr(Birth Year)
#      iyr(Issue Year)
#      eyr(Expiration Year)
#      hgt(Height)
#      hcl(Hair Color)
#      ecl(Eye Color)
#      pid(PassportID)
#      cid(Country ID)
# Goal = find the number of valid passport entries
# Output = number of valid passport entries

from pathlib import Path
import re

print("Starting Dec 4th")

script_location = Path(__file__).absolute().parent
file_location = script_location / 'input.txt'
input_file = file_location.open()

all_passports = []
passport_string = ""
for line in input_file:
    if line != "\n":
        passport_string += line.rstrip()
        passport_string += " "
    else:
        passport_string = passport_string.strip()
        all_passports.append(passport_string)
        passport_string = ""

# include last record:
passport_string = passport_string.strip()
all_passports.append(passport_string)

input_file.close()


# Part 1:
required_fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
valid_passports = 0

for passport in all_passports:
    matching_fields = 0
    for required_field in required_fields:
        if required_field in passport:
            matching_fields += 1
        if matching_fields == len(required_fields):
            valid_passports += 1
            break

print(str("PART 1 -- Count of Valid Passports {}").format(valid_passports))


# Part 2:
def validate_byr(byr):
    birth_year = int(byr)
    return 1920 <= birth_year <= 2002

def validate_iyr(iyr):
    issue_year = int(iyr)
    return 2010 <= issue_year <= 2020

def validate_eyr(eyr):
    expiration_year = int(eyr)
    return 2020 <= expiration_year <= 2030

def validate_hgt(hgt):
    unit = hgt[-2:]
    if unit == "cm":
        height_str = hgt[0:3]
        if can_convert_to_int(height_str):
            height = int(height_str)
            return 150 <= height <= 193
    elif unit == "in":
        height_str = hgt[0:2]
        if can_convert_to_int(height_str):
            height = int(height_str)
            return 59 <= height <= 76
    else:
        return False

def validate_hcl(hcl):
    is_hex_color = re.search("^#[0-9a-f]{6}$", hcl)
    return is_hex_color

def validate_ecl(ecl):
    matches = re.compile("(%s|%s|%s|%s|%s|%s|%s)" % ("^amb$", "^blu$", "^brn$", "^gry$", "^grn$", "^hzl$", "^oth$")).findall(ecl)
    if len(matches) > 0:
        return True
    else:
        return False

def validate_pid(pid):
    is_valid_passport_id = re.search("^[0-9]{9}$", pid)
    return is_valid_passport_id

def validate_cid(cid):
    del cid
    return True

def can_convert_to_int(test_string):
    try:
        int(test_string)
        return True
    except ValueError:
        return False

possibly_valid = []
valid_passports = 0
validation_map = {"byr": validate_byr,
                  "iyr": validate_iyr,
                  "eyr": validate_eyr,
                  "hgt": validate_hgt,
                  "hcl": validate_hcl,
                  "ecl": validate_ecl,
                  "pid": validate_pid,
                  "cid": validate_cid}


for passport in all_passports:
    matching_fields = 0
    for required_field in required_fields:
        if required_field in passport:
            matching_fields += 1
        if matching_fields == len(required_fields):
            possibly_valid.append(passport)
            break

for possible in possibly_valid:
    records = possible.split(" ")
    print(len(records))
    records_valid = True

    for record in records:
        split = record.split(":")

        if len(split) != 2:
            print(split)

        key = split[0]
        value = split[1]

        records_valid = records_valid and validation_map[key](value)

    if records_valid:
        valid_passports += 1

print(str("PART 2 -- Count of Valid Passports {}").format(valid_passports))
