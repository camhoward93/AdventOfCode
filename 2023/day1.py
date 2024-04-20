# Day 1
# Trebuchet

# Part 1
import re

# main program
# open the file
with open('C:\\Users\\camho\\Desktop\\input.txt') as file:
    # pull all the lines
    lines = [line.strip() for line in file]

# extract the numbers from each line
numbers = [int(str(re.findall(r'[0-9]', line)[0] + str(re.findall(r'[0-9]', line)[-1]))) for line in lines]

answer = sum(numbers)

print(answer)



# Part 2
import re

# main program
# numeric word dictionary
num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

# open the file
with open('C:\\Users\\camho\\Desktop\\input.txt') as file:
    # pull all the lines
    lines = [line.strip() for line in file]

# initialize number list
numbers = []

# extract the numbers from each line
for line in lines:
    digits = (re.findall(r'[0-9]|zero|one|two|three|four|five|six|seven|eight|nine|ten', line))
    # correct the numerical digits
    for index, value in enumerate(digits):
        if value in num_dict:
            digits[index] = num_dict[value]
    # place the first and last digits together in the numbers list
    numbers.append(int(str(digits[0] + str(digits[-1]))))

# NOTE: I'm sure there is a way to put all of that into a list comprehension, but it would be a monster and likely not
#   readable.

answer = sum(numbers)

print(answer)
