# define class
class Favorite:
    #set protected and private variables
    def __init__(self):
        self._favoriteVar = "String"
        self.__personalVar = 5

    #define method to get private variable
    def getPersonal(self):
        print(self.__personalVar)

    #define method to change private variable
    def setPersonal(self, personal):
        self.__personalVar = personal

obj = Favorite()
obj._favoriteVar = "Car"
print(obj._favoriteVar)
obj.getPersonal()
obj.setPersonal(23)
obj.getPersonal()

