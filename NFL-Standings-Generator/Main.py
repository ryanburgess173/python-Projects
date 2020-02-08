from Team import Team
from Result import Result
import random
def main():
    teams = [
        Team("New England","Patriots", "AFC-East"),
        Team("Buffalo", "Bills", "AFC-East"),
        Team("New York", "Jets", "AFC-East"),
        Team("Miami", "Dolphins", "AFC-East"),
        Team("Kansas City", "Chiefs", "AFC-West"),
        Team("Denver", "Broncos", "AFC-West"),
        Team("Oakland", "Raiders", "AFC-West"),
        Team("San Diego", "Chargers", "AFC-West"),
        Team("Baltimore", "Ravens", "AFC-North"),
        Team("Pittsburg", "Steelers", "AFC-North"),
        Team("Cleveland", "Browns", "AFC-North"),
        Team("Cinncinati", "Bengals", "AFC-North"),
        Team("Houston", "Texans", "AFC-South"),
        Team("Tennessee", "Titans", "AFC-South"),
        Team("Indianapolis", "Colts", "AFC-South"),
        Team("Jacksonville", "Jaguars", "AFC-South")
    ]

    possibleScores = [0, 3, 7, 10, 13, 14, 17, 20,
                      21, 24, 28, 31, 35, 38, 42, 49, 52, 56]

    num = 0
    for i in range(0,len(teams),1):
        for j in range(len(teams)-1, -1, -1):
            if(j!=i):
                num = num + 1
                teams[i].addGameResult(Result(teams[j], possibleScores[random.randint(1, 16)], possibleScores[random.randint(1, 16)], "9/8/1960", "Regular Season"))
        num = 0

    wins = []
    losses = []
    ties = []
    for i in range(len(teams)):
        wins.append(0)
        losses.append(0)
        ties.append(0)
    
    for i in range(len(teams)):
        for j in range(15):
            w_or_l = teams[i].getGameResults(j).getResult()
            if(w_or_l == "W"):
                wins[i]+=1
            if(w_or_l == "L"):
                losses[i]+=1
            else:
                ties[i]+=1

    for i in range(len(teams)):
        print(teams[i].getFullName() + "\t\t" + str(wins[i]) + "-" + str(losses[i]) + "-" + str(ties[i]))
main()
