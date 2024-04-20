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
