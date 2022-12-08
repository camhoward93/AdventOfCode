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
prioritySum = 0

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
                foundChars = ""

                # for each item in sack1, check if it's in sack2
                for x in sack1:
                    # if there is a duplicate
                    if sack2.find(x) != -1 and foundChars.find(x) == -1:
                        # add to the priority sum and add the found char
                        prioritySum += get_priority(x)
                        foundChars += x

# print priority sum
print(prioritySum)



# Part 2

