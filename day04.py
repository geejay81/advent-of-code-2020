file_name = 'day04.txt'
open_file = open(file_name, 'r')
lines = open_file.readlines()

required_properties = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passports = []
raw_passport = ''
raw_passports = []
valid_passports = 0

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