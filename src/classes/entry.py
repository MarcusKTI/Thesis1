from datetime import datetime
import json

class Entry:
    """Entry of stuff put into a freezer"""
    def __init__(self):
        __name = ""
        __date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        __freezerId = 0
        __expDate = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        __location = (0, 0, 0)

    def save(self):
        output = {
                'name': self.__name,
                'date': self.__date,
                'freezerId': self.__freezerId,
                'expDate': self.__expDate,
                'location': self.__location
                }
        return json.dumps(output)

    def load(self, jsonInput):
        x = json.loads(jsonInput)
        self.__name = x.name
        self.__date = x.date
        self.__freezerId = x.freezerId
        self.__expDate = x.expDate
        self.__location = x.location

    def edit(self):
        newName = input("Set name for entry: ")
        newDate = input("Set date for entry: ")
        newFreezer = input("Set freezer for entry: ")
        newExpDate = input("Set expiration date for entry: ")
        newLocation = input("Set location for entry: ")
        self.__name = newName
        self.__date = newDate
        self.__freezerId = newFreezer
        self.__expDate = newExpDate
        self.__location = newLocation

