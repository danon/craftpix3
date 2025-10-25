from hex.core.port import ForRunningGame

class CliTerminal:
    def __init__(self, game: ForRunningGame):
        self.__game = game

    def print(self):
        print(self.__game.frames())
