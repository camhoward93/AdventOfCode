# Day 1
# Elf Food Calories

# declare variables
largestSum = 0
currentSum = 0

# open the file
with open('C:\\Users\\camho\\Desktop\\input.txt') as file:
    # loop over the lines
    for line in file:
        # if line is not blank, add to sum
        if line.strip():
            currentSum += int(line)
        # if line is blank, check sum values
        else:
            if currentSum > largestSum:
                largestSum = currentSum

            # reset current sum
            currentSum = 0

# print largest sum found
print(largestSum)
