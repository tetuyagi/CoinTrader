import json


class Settings:
    def __init__(self, filePath="settings.json"):
        self.api_key = ""
        self.api_secret = ""

        with open(filePath, 'r') as f:
            jsonObj = json.load(f)
            self.api_key = jsonObj["api_key"]
            self.api_secret = jsonObj["api_secret"]


"""
    @staticmethod
    def load(filePath="settings.json"):
        with open(filePath, 'r') as f:
            jsonObj = json.load(f)
            Settings.api_key = jsonObj["api_key"]
            Settings.api_secret = jsonObj["api_secret"]
"""
