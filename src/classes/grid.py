import json

class Grid:
    """Abstraction of Freezer inventory"""
    def __init__(self):
        self.__internalGrid = [
                [
                    [None,None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None,None],
                    ],
                [
                    [None,None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None,None],
                    ],
                [
                    [None,None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None,None],
                    ],
                [
                    [None,None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None,None],
                    ],
                [
                    [None,None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None,None],
                    ],
                ]

    def load(self, jsonInput):
        self.__internalGrid = json.loads(jsonInput)

    def save(self):
        return json.dumps(self.__internalGrid)
