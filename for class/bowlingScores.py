# Create a program that prompts the user for 3 bowling scores. 
# The program should then display the 3 scores and the average.

# Print header.

print("+------------------------+\n| Bowling Score Averager |\n+------------------------+\n")

numberOfScores = 3 # Constant

realScore = 1
invalidScoreMessage = "That score is invalid. Try again."

# Retrieve first score.

while realScore == 1:
    realScore = 0

    print("\nEnter the first bowling score:")
    bowlingScore1 = int(input())

    # Check if the score is possible.
    if bowlingScore1 < 0:
        realScore = 1
        print(invalidScoreMessage)
    elif bowlingScore1 > 300:
        realScore = 1
        print(invalidScoreMessage)

realScore = 1

# Retrieve second score.

while realScore == 1:
    realScore = 0

    print("\nEnter the second bowling score:")
    bowlingScore2 = int(input())

    if bowlingScore2 < 0:
        realScore = 1
        print(invalidScoreMessage)
    elif bowlingScore2 > 300:
        realScore = 1
        print(invalidScoreMessage)

realScore = 1

# Retrieve third score.

while realScore == 1:
    realScore = 0

    print("\nEnter the third bowling score:")
    bowlingScore3 = int(input())

    if bowlingScore3 < 0:
        realScore = 1
        print(invalidScoreMessage)
    elif bowlingScore3 > 300:
        realScore = 1
        print(invalidScoreMessage)

# Take average of scores.

averageScore = (bowlingScore1 + bowlingScore2 + bowlingScore3) / numberOfScores

# Print scores in output display.

print("\n\n+------------------+")
print("| The scores are:  |")
print("|  ", bowlingScore1, "  \t   |")
print("|  ", bowlingScore2, "  \t   |")
print("|  ", bowlingScore3, "  \t   |")
print("| And the          |")
print("| average is:      |")
print("|   {:.2f}  \t   |".format(averageScore))
print("+------------------+")
