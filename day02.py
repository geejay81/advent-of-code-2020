file_path = 'day02.txt'
file_contents = open(file_path, 'r')
lines = file_contents.readlines()
valid_passwords1 = 0
valid_passwords2 = 0

for line in lines :
    parts = line.split()
    required_count = parts[0].split('-')
    letter = parts[1][0]
    password = parts[2]
    passwordLetters = list(password)
    occurrences = passwordLetters.count(letter)
    
    for required_number in range(int(required_count[0]), int(required_count[1]) + 1) :
        if occurrences == required_number :
            valid_passwords1 += 1
            break

    correct_positions = 0

    if password[int(required_count[0]) - 1] == letter :
        correct_positions += 1

    if password[int(required_count[1]) - 1] == letter :
        correct_positions += 1

    if correct_positions == 1 :
        valid_passwords2 += 1

print('Password Rule 1: ' + str(valid_passwords1))
print('Password Rule 2: ' + str(valid_passwords2))