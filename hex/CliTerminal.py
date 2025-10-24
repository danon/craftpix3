from hex.core.Application import ForControlling

class CliTerminal:
    def __init__(self, controls: ForControlling):
        self.__controls = controls

    def print(self):
        print(self.__controls.resource_root())
