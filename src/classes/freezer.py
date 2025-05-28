import json

class Freezer:
    """Freezer abstraction"""
    def __init__(self, initId):
        self.freezerId = initId
        self.temp = -80
        self.grid = [
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
