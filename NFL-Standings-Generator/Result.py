class Result:

    def __init__(self, opponent, theirScore, yourScore, date, gameType):
        self.__opponent = opponent
        self.__theirScore = theirScore
        self.__yourScore = yourScore
        self.__date = date
        self.__gameType = gameType
        if(self.__theirScore>self.__yourScore):
            self.__result = "L"
        elif(self.__yourScore>self.__theirScore):
            self.__result = "W"
        else:
            self.__result = "T"

    def getResult(self):
        return self.__result