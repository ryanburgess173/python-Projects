class Team:
    def __init__(self, city, name, division):
        self.__city = city
        self.__name = name
        self.__division = division
        self.__division_titles = 0
        self.__wildcard_wins = 0
        self.__division_round_wins = 0
        self.__conference_championships = 0
        self.__superbowls = 0
        self.__gameResults = []

    def getGameResults(self, index):
        return self.__gameResults[index]

    def addGameResult(self,result):
        self.__gameResults.append(result)

    def getFullName(self):
        return self.__city+" "+self.__name