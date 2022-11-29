
# title card
def introduction():
    print("******************************************\n* Welcome to my Soccer Analyzer program! *\n******************************************\n")

# takes input of team names and their scores in parallel lists
def getTeamsAndScores():
    teams = []
    scores = []

    breakCode = "" 
    while breakCode != "n": # i could structure this section to not have an extra input for confirmation, but it would make it harder to read the code
        teams.append(input("Enter the name of a team.\n"))
        scores.append(int(input("What is that team's score?\n")))
        breakCode = input("Would you like to continue entering teams and scores? (y/n)\n")
    return teams, scores

# reverses the order of both lists and returns the reversed lists
def reverseTeamsAndScores(teams, scores):
    reverseTeams = []
    reverseScores = []

    for i in range(len(teams)):
        reverseTeams.append(teams[len(teams) - 1 - i]) # "-i" didn't cut it here
    
    for i in range(len(scores)):
        reverseScores.append(scores[len(teams) - 1 - i])
    
    return reverseTeams, reverseScores

# this does almost exactly the same thing as getHighestScore()
def getMostWinningTeam(teams, scores):
    highestTeam = teams[0]
    highestScore = scores[0]

    for i in range(len(teams)): # didn't use max() so i could match up scores and teams easier
        if scores[i] > highestScore:
            highestTeam = teams[i]
            highestScore = scores[i]
    
    return highestTeam

# searches for the highest scoring team and returns its name and its score
def getHighestScore(teams, scores):
    highestTeam = teams[0]
    highestScore = scores[0]

    for i in range(len(teams)):
        if scores[i] > highestScore:
            highestTeam = teams[i]
            highestScore = scores[i]
    
    return highestTeam, highestScore

# searches for the lowest scoring team and returns its name and its score
def getLowestScore(teams, scores):
    lowestTeam = teams[0]
    lowestScore = scores[0]

    for i in range(len(teams)):
        if scores[i] < lowestScore:
            lowestTeam = teams[i]
            lowestScore = scores[i]
    
    return lowestTeam, lowestScore

# prints the teams and scores in this form:
# team
# score
# 
# team
# score
# ...
def prettyPrint(teams, scores):
    print("\nThe teams and scores are:\n")

    for i in range(len(teams)):
        print(teams[i], "\n" + str(scores[i]), "\n")

# i noticed that many of the functions never created anything that would
# be output to the console, so i created an extra function that printed
# their return values out
def extraPrint(reverseTeams, reverseScores, mostWinningTeam, highestTeam, highestScore, lowestTeam, lowestScore):
    print("The reversed teams and scores are:\n")

    for i in range(len(reverseTeams)):
        print(reverseTeams[i], "\n" + str(reverseScores[i]), "\n\n")

    print("The most winning team is:", mostWinningTeam)
    print("The highest scoring team is:", highestTeam, "with a score of", str(highestScore) + ".")
    print("The lowest scoring team is:", lowestTeam, "with a score of", str(lowestScore) + ".")


# calls all previously defined functions
def main():
    introduction()
    teams, scores = getTeamsAndScores()
    reverseTeams, reverseScores = reverseTeamsAndScores(teams, scores)
    mostWinningTeam = getMostWinningTeam(teams, scores)
    highestTeam, highestScore = getHighestScore(teams, scores)
    lowestTeam, lowestScore = getLowestScore(teams, scores)
    prettyPrint(teams, scores)

    extraPrint(reverseTeams, reverseScores, mostWinningTeam, highestTeam, highestScore, lowestTeam, lowestScore)

main()