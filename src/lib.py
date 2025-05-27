import os
import json

from src.classes.freezer import Freezer

class App:
    """Overarching app abstraction to keep track of all ongoing data shit"""
    def __init__(self, filepath):
        self.filepath = filepath
        self.freezers = []
        self.nextId = 0

    def save(self):
        freezersOutput = "["
        for freezer in self.freezers:
            freezersOutput += freezer.save()
            freezersOutput += ","
        freezersOutput = freezersOutput[:-1]
        freezersOutput += "],"

        output = {
                'freezers': freezersOutput,
                'nextId': self.nextId,
                }
        with open(self.filepath, "w") as file:
            file.write(json.dumps(output))
            file.flush()

    def load(self):
        jsonInput = None
        with open(self.filepath, "r") as file:
            jsonInput = file.read()
        x = json.loads(jsonInput)
        loadedFreezers = json.loads(x["freezers"])
        for loadedFreezer in loadedFreezers:
            freezer = Freezer()
            freezer.load(loadedFreezer)
            self.freezers.append(freezer)
        self.nextId = x["nextId"]

    def getNextId(self):
        output = self.nextId
        self.nextId += 1
        return output

FILEPATH = os.path.expanduser("~") + "/thesis1.json"
app = App(FILEPATH)

def appRun():
    if not os.path.exists(FILEPATH):
        # runInitBootup
        print("No configuration found. Starting init bootup sequence.")
        freezerNum = int(input("Enter amount of freezers: "))
        freezers = []
        for i in range(0, freezerNum):
            temp = int(input(f"Enter desired temperature for freezer with id {i}: "))
            freezer = Freezer(app.getNextId())
            freezer.temp = temp
            freezers.append(freezer)
        app.freezers = freezers
        app.save()

    # runNormalBootup
    print("Starting thesis1 PoC application.")
    app.load()
    print("Save state loaded.")
    print("Freezers loaded:")
    for freezer in app.freezers:
        print(freezer.freezerId)
        print(freezer.temp)


def getNextId():
    return app.getNextId()
