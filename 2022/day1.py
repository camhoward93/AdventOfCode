# Day 1
# Elf Food Calories

# Part 1

# declare variables
largest_sum = 0
current_sum = 0

# open the file
with open('C:\\Users\\camho\\Desktop\\input.txt') as file:
    # loop over the lines
    for line in file:
        # if line is not blank, add to sum
        if line.strip():
            current_sum += int(line)
        # if line is blank, check sum values
        else:
            if current_sum > largest_sum:
                largest_sum = current_sum

            # reset current sum
            current_sum = 0

# print largest sum found
print(largest_sum)



# Part 2

# declare variables
largest_sums = [0, 0, 0]
current_sum = 0

# open the file
with open('C:\\Users\\camho\\Desktop\\input.txt') as file:
    # loop over the lines
    for line in file:
        # if line is not blank, add to sum
        if line.strip():
            current_sum += int(line)
        # if line is blank, check sum values
        else:
            if current_sum > largest_sums[0]:
                largest_sums[0] = current_sum
                largest_sums.sort()

            # reset current sum
            current_sum = 0

# print largest sum found
print(largest_sums)
print(sum(largest_sums))
