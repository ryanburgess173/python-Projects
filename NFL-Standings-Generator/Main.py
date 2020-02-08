from Team import Team
from Result import Result
def main():
    teams = [
        Team("New England","Patriots", "AFC-East"),
        Team("Buffalo", "Bills", "AFC-East"),
        Team("New York", "Jets", "AFC-East"),
        Team("Miami", "Dolphins", "AFC-East"),
        Team("Kansas City", "Chiefs", "AFC-West"),
        Team("Denver", "Broncos", "AFC-West"),
        Team("Oakland", "Raiders", "AFC-West"),
        Team("San Diego", "Chargers", "AFC-West")
    ]

    for i in range(len(teams)):

        if(i==4):
            teams[i].addGameResult(
                Result(teams[2], 17, 14, "9/8/1960", "Regular Season"))
        elif((i % 2) == 0):
            teams[i].addGameResult(
                Result(teams[3], 28, 10, "9/1/1960", "Regular Season"))
        else:
            teams[i].addGameResult(Result(teams[1],0,14,"9/15/1960","Regular Season"))

    wins = [0,0,0,0,0,0,0,0]
    losses = [0, 0, 0, 0, 0, 0, 0, 0]
    ties = [0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(len(teams)):
        for j in range(0,1):
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
