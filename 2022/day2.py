# Day 2
# Rock, Paper, Scissors

# Part 1

# declare variables
totalScore = 0
outcomes = {
    "A X": 4,  # 1 + 3
    "A Y": 8,  # 2 + 6
    "A Z": 3,  # 3 + 0
    "B X": 1,  # 1 + 0
    "B Y": 5,  # 2 + 3
    "B Z": 9,  # 3 + 6
    "C X": 7,  # 1 + 6
    "C Y": 2,  # 2 + 0
    "C Z": 6,  # 3 + 3
}  # rock, paper, scissors has a small enough list of outcomes that this seems efficient

# open the file
with open('C:\\Users\\camho\\Desktop\\input.txt') as file:
    # loop over the lines
    for line in file:
        # if line is not blank
        if line.strip():
            totalScore += outcomes[line.strip()]

# print largest sum found
print(totalScore)



# Part 2

# declare variables
totalScore = 0
outcomes = {
    "A X": 3,  # 0 + 3
    "A Y": 4,  # 3 + 1
    "A Z": 8,  # 6 + 2
    "B X": 1,  # 0 + 1
    "B Y": 5,  # 3 + 2
    "B Z": 9,  # 6 + 3
    "C X": 2,  # 0 + 2
    "C Y": 6,  # 3 + 3
    "C Z": 7,  # 6 + 1
}   # rock, paper, scissors has a small enough list of outcomes that this seems efficient
# this feels slightly cheap because I am calculating the 9 outcomes manually, but it sure is computing efficient

# open the file
with open('C:\\Users\\camho\\Desktop\\input.txt') as file:
    # loop over the lines
    for line in file:
        # if line is not blank
        if line.strip():
            totalScore += outcomes[line.strip()]

# print largest sum found
print(totalScore)
