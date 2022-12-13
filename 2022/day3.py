# Day 3
# Elf Rucksacks

# Part 1

# functions
def split_string(string):
    return string[:len(string) // 2], string[len(string) // 2:]


def get_priority(letter):
    # return priority based on case
    if letter.islower():
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27


# declare variables
priority_sum = 0

# open the file
with open('C:\\Users\\camho\\Desktop\\input.txt') as file:
    # loop over the lines
    for line in file:
        # if line is not blank
        if line.strip():
            # check for even number of items in rucksack
            if len(line.strip()) % 2 != 0:
                print("Invalid input detected")
            else:
                # split the string to get both sack pockets
                sack1, sack2 = split_string(line.strip())
                found_chars = ""

                # for each item in sack1, check if it's in sack2
                for x in sack1:
                    # if there is a duplicate
                    if sack2.find(x) != -1 and found_chars.find(x) == -1:
                        # add to the priority sum and add the found char
                        priority_sum += get_priority(x)
                        found_chars += x

# print priority sum
print(priority_sum)



# Part 2

# functions
def get_priority(letter):
    # return priority based on case
    if letter.islower():
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27


# declare variables
priority_sum = 0

# open the file
with open('C:\\Users\\camho\\Desktop\\input.txt') as file:
    # pull all the lines
    lines = [line.strip() for line in file]

# create the list of each elf group
groups = [lines[x:x+3] for x in range(0, len(lines), 3)]

# loop over the groups
for group in groups:
    found_chars = ""
    # check each character of the first line for a match in the next two
    for character in group[0]:
        # if there is a duplicate
        if group[1].find(character) != -1 and group[2].find(character) != -1 and found_chars.find(character) == -1:
            # add to the priority sum and add the found char
            priority_sum += get_priority(character)
            found_chars += character

# print priority sum
print(priority_sum)
