# Day 4
# Elf Cleaning Sections

# Part 1

# functions
def is_overlap(elf1, elf2):
    if len(elf1) == 2 and len(elf2) == 2:
        if (int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]))\
                or (int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1])):
            return True
        else:
            return False


# declare variables
numOverlaps = 0

# open the file
with open('C:\\Users\\camho\\Desktop\\input.txt') as file:
    # loop over the lines
    for line in file:
        # if line is not blank
        if line.strip():
            # split the line into a pair
            split = line.strip().split(',')

            # split the pairs into min / max section numbers
            firstElf = split[0].split('-')
            secondElf = split[1].split('-')

            # find the max of the min between them
            if is_overlap(firstElf, secondElf):
                numOverlaps += 1

# print number of overlaps
print(numOverlaps)