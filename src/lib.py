import os
import pickle

from src.classes.freezer import Freezer
from src.classes.entry import Entry

class App:
    """Overarching app abstraction to keep track of all ongoing data shit"""
    def __init__(self, filepath):
        self.filepath = filepath
        self.freezers = {}
        self.nextId = 0

    def save(self):
        output = {
                'freezers': self.freezers,
                'nextId': self.nextId,
                }
        pickleOutput = pickle.dumps(output)
        with open(self.filepath, 'wb') as saveFile:
            saveFile.write(pickleOutput)
            saveFile.flush()

    def load(self):
        saveFileContent = ""
        with open(self.filepath, 'rb') as saveFile:
            saveFileContent = saveFile.read()
        loadedContent = pickle.loads(saveFileContent)
        self.freezers = loadedContent["freezers"]
        self.nextId = loadedContent["nextId"]

    def getNextId(self):
        output = self.nextId
        self.nextId += 1
        return output

FILEPATH = os.path.expanduser("~") + "/thesis1.pickle"

app = App(FILEPATH)
selectedEntries = {}

def appRun():
    if not os.path.exists(FILEPATH):
        # runInitBootup
        print("No configuration found. Starting init bootup sequence.")
        freezerNum = int(input("Enter amount of freezers: "))
        freezers = {}
        for i in range(0, freezerNum):
            temp = int(input(f"Enter desired temperature for freezer with id {i}: "))
            freezer = Freezer(app.getNextId())
            freezer.temp = temp
            freezers[i] = freezer
        app.freezers = freezers
        app.save()

    # runNormalBootup
    os.system("clear")
    print("Starting thesis1 PoC application.")
    app.load()
    print("Save state loaded.")

    # Main Menu:
    mainMenu()
    print("Exiting thesis1 PoC application.")


def mainMenu():
    while True:
        print("[1] - Add Freezer")
        print("[2] - Select Freezer")
        print("[3] - Save and Exit")
        userSelection = input().strip()
        if userSelection == "1":
            newFreezer = Freezer(app.getNextId())
            newFreezerTemp = int(input(f"Enter desired temperature for new freezer with id {newFreezer.freezerId}: "))
            newFreezer.temp = newFreezerTemp
            app.freezers[newFreezer.freezerId] = newFreezer
            os.system("clear")

        elif userSelection == "2":
            selectedFreezerId = selectFreezer()
            selectedFreezer(selectedFreezerId)
            os.system("clear")

        elif userSelection == "3":
            app.save()
            os.system("clear")
            return

        else:
            unknownOption()

def selectFreezer():
    os.system("clear")
    isValidFreezer = False
    while not isValidFreezer:
        for freezer in app.freezers.values():
            print(f"[{freezer.freezerId}]")
        selection = int(input("Select desired freezer id: "))

        for freezer in app.freezers.values():
            if selection == freezer.freezerId:
                isValidFreezer = True

        if not isValidFreezer:
            unknownOption()

    return selection

def selectedFreezer(freezerId):
    os.system("clear")
    print(f"Selected freezer: {freezerId}")
    while True:
        print("[1] - Edit configuration")
        print("[2] - Display contents")
        print("[3] - Edit contents")
        print("[4] - Create new entry")
        print("[5] - Back")
        userSelection = input().strip()
        if userSelection == "1":
            print(f"Current freezer temperature: {app.freezers[freezerId].temp}")
            newTemp = int(input("Enter new freezer temperature: "))
            app.freezers[freezerId].temp = newTemp
            os.system("clear")

        elif userSelection == "2":
            os.system("clear")
            displayFreezerContents(freezerId, False)
            print()

        elif userSelection == "3":
            os.system("clear")
            displayFreezerContents(freezerId, True)
            selectedEntry = int(input("Select entry to edit: "))
            editEntryInFreezer(freezerId, selectedEntry)

        elif userSelection == "4":
            newEntry = Entry()
            newEntry.freezerId = freezerId
            newEntry.name = input("Enter name of the entry: ")
            newEntry.expDate = input("Enter expiration date for the entry: ")
            newEntryPos = input("Enter the location of the entry in the freezer.\nThe position is given in the format 'shelf,rack,box' provided with numbers, starting at 0: ")
            newEntryPos = newEntryPos.split(",")
            newEntryPos = (int(newEntryPos[0]), int(newEntryPos[1]), int(newEntryPos[2]))
            if not app.freezers[freezerId].grid[newEntryPos[0]][newEntryPos[1]][newEntryPos[2]] == None:
                os.system("clear")
                print("Location is already occupied. Try again.")
                continue

            newEntry.location = newEntryPos
            app.freezers[freezerId].grid[newEntryPos[0]][newEntryPos[1]][newEntryPos[2]] = newEntry
            os.system("clear")

        elif userSelection == "5":
            os.system("clear")
            return

        else:
            unknownOption()

def displayFreezerContents(freezerId, hasPrefix):
    i = 0
    for shelf in range(0, 5):
        for row in range(0, 4):
            for box in range(0, 9):
                if app.freezers[freezerId].grid[shelf][row][box] is None:
                    continue
                selectedEntries[i] = (shelf, row, box)
                toBePrinted = ""
                if hasPrefix:
                    toBePrinted += f"[{i:03}] "
                toBePrinted += app.freezers[freezerId].grid[shelf][row][box].printEntry()
                print(toBePrinted)
                i += 1

def editEntryInFreezer(freezerId, selectedEntry):
    newName = input("Enter new name for entry: ")
    newFreezerId = int(input("Enter new freezer id for entry: "))
    if not newFreezerId in app.freezers.keys():
        os.system("clear")
        print("No such freezer. Try again.")
        return

    newExpDate = input("Enter a new expiration date for entry: ")
    newLocation = input("Enter the new location of the entry in the freezer.\nThe position is given in the format 'shelf,rack,box' provided with numbers, starting at 0: ").strip()
    newLocation = newLocation.split(",")
    newLocation = (int(newLocation[0]), int(newLocation[1]), int(newLocation[2]))

    if not app.freezers[newFreezerId].grid[newLocation[0]][newLocation[1]][newLocation[2]] == None:
        os.system("clear")
        print("Location is already occupied. Try again.")
        return

    app.freezers[newFreezerId].grid[newLocation[0]][newLocation[1]][newLocation[2]] = app.freezers[freezerId].grid[selectedEntries[selectedEntry][0]][selectedEntries[selectedEntry][1]][selectedEntries[selectedEntry][2]]
    app.freezers[newFreezerId].grid[newLocation[0]][newLocation[1]][newLocation[2]].name = newName
    app.freezers[newFreezerId].grid[newLocation[0]][newLocation[1]][newLocation[2]].freezerId = newFreezerId
    app.freezers[newFreezerId].grid[newLocation[0]][newLocation[1]][newLocation[2]].expDate = newExpDate
    app.freezers[newFreezerId].grid[newLocation[0]][newLocation[1]][newLocation[2]].location = newLocation

    app.freezers[freezerId].grid[selectedEntries[selectedEntry][0]][selectedEntries[selectedEntry][1]][selectedEntries[selectedEntry][2]] = None
    os.system("clear")

def unknownOption():
    os.system("clear")
    print("Unknown option, try again.")
    print()

def getNextId():
    return app.getNextId()
