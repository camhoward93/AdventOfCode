# Day 5
# Moving Crates

# Part 1

# functions
def add_crates(string, lst, first, skip):
    # format the crates into a stack
    row_stack = []
    crate_index = first

    # loop over the line and add crates, using * for empty
    while crate_index < len(string):
        if string[crate_index] != ' ':
            row_stack.append(string[crate_index])
        else:
            row_stack.append('*')

        # increment the index by the designated amount
        crate_index += skip

    # add the stack to the list
    lst.append(row_stack)


def format_stacks(lst):
    # find the max number of columns
    max_stacks = max(len(x) for x in lst)
    reversed_list = [[] for x in range(max_stacks)]

    # fill in empty crates for all rows
    for stack in lst:
        while len(stack) < max_stacks:
            stack.append('*')

    # for each row, add the crates at the index if they are not empty
    for row in lst:
        for stack_index, crate in enumerate(row):
            if crate != '*':
                reversed_list[stack_index].append(crate)

    # finally, reverse each list so they can be used as stacks
    formatted_list = [elem[::-1] for elem in reversed_list]

    return formatted_list


def follow_instruction(string, lst):
    numbers = [int(s) for s in string.split() if s.isdigit()]
    num_crates = numbers[0]
    src = lst[numbers[1]-1]
    dst = lst[numbers[2]-1]

    for _ in range(num_crates):
        dst.append(src.pop())


# declare variables
stack_list = []
first_crate_index = 1
crate_char_skip = 4
answer = ''

# main program
# open the file
with open('C:\\Users\\camho\\Desktop\\input.txt') as file:
    # pull all the lines
    lines = [line.strip() for line in file]

# get the crate lines and the instructions
crateLines = [x for x in lines if '[' in x]
instructionLines = lines[len(crateLines)+2:]

# loop through the crate lines and add the crate
for line in crateLines:
    add_crates(line, stack_list, first_crate_index, crate_char_skip)

# format the stack list to columns rather than rows
stack_list = format_stacks(stack_list)

# loop through the instruction lines
for line in instructionLines:
    # execute the instructions
    follow_instruction(line, stack_list)

# print the top crate for each stack
for stack in stack_list:
    answer += stack[-1]

print(answer)
