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
numbers = [int(str(num_dict.get(digits[0], digits[0])) + str(num_dict.get(digits[-1], digits[-1])))
           for line in lines
           for digits in [re.findall(r'[0-9]|zero|one|two|three|four|five|six|seven|eight|nine|ten', line)]]

answer = sum(numbers)

print(answer)
