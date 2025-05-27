import json

from src.classes.grid import Grid

class Freezer:
    """Freezer abstraction"""
    def __init__(self, initId):
        self.freezerId = initId
        self.temp = -80
        self.grid = Grid()

    def save(self):
        gridOutput = self.grid.save()
        output = {
                'id': self.freezerId,
                'temp': self.temp,
                'grid': gridOutput
                }
        return json.dumps(output)

    def load(self, jsonInput):
        x = json.loads(jsonInput)
        self.freezerId = x.id
        self.temp = x.temp
        self.grid = self.__grid.load(x.grid)
