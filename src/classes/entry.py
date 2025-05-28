from datetime import datetime
import json

class Entry:
    """Entry of stuff put into a freezer"""
    def __init__(self):
        self.name = ""
        self.date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.freezerId = 0
        self.expDate = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.location = (0, 0, 0)

    def printEntry(self) -> str:
        return f"Date: {self.date}, Name: {self.name}, ExpirationDate: {self.expDate}, Location: {self.location}"
