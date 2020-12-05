file_name = 'day04.txt'
open_file = open(file_name, 'r')
lines = open_file.readlines()

required_properties = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passports = []
raw_passport = ''
raw_passports = []
valid_passports = 0

def validate_property(prop_name, prop_value) :
    
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if prop_name == 'byr' :
        if len(prop_value) < 4 or len(prop_value) > 4 :
            return False
        if not prop_value.isnumeric() :
            return False
        if prop_value < 1920 or prop_value > 2002 :
            return False
        return True

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if prop_name == 'iyr' :
        if len(prop_value) < 4 or len(prop_value) > 4 :
            return False
        if not prop_value.isnumeric() :
            return False
        if prop_value < 2010 or prop_value > 2020 :
            return False
        return True

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if prop_name == 'eyr' :
        if len(prop_value) < 4 or len(prop_value) > 4 :
            return False
        if not prop_value.isnumeric() :
            return False
        if prop_value < 2020 or prop_value > 2030 :
            return False
        return True
    
    # hgt (Height) - a number followed by either cm or in:
    #   If cm, the number must be at least 150 and at most 193.
    #   If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if prop_name == 'hcl' :
        characters = prop_value.split()
        if characters[0] != '#' :
            return False
        hex_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        for character in characters[-6] :
            if character not in hex_characters :
                return False
        return True

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if prop_name == 'ecl' :
        options = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if prop_value in options :
            return True
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if prop_name == 'pid' :
        characters = prop_value.split()
        if len(characters) != 9 :
            return False
        for character in characters :
            if not character.isnumeric() :
                return False
        return True

    return True

for line in lines :
    cleaned_line = line.strip()

    if len(cleaned_line) == 0 :
        raw_passports.append(raw_passport)
        raw_passport = ''
        continue

    raw_passport += line.replace('\n', ' ')

raw_passports.append(raw_passport)

for passport in raw_passports :
    record = {}
    props = passport.split()
    for prop in props :
        key_value = prop.split(':')
        record[key_value[0]] = key_value[1]
    passports.append(record)

for passport in passports :
    properties = 0
    for prop in required_properties :
        if prop in passport.keys() :
            properties += 1
    if properties == len(required_properties) :
        valid_passports += 1
        
print('Total Passports: {}'.format(len(passports)))
print('Valid Passports: {}'.format(valid_passports))