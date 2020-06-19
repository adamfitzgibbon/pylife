import json


class Patterns:
    def __init__(self):
        with open('patterns.json') as f:
            self.patterns = json.load(f)

    def blinker(self):
        return self.patterns['blinker']

    def toad(self):
        return self.patterns['toad']
