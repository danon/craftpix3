from hex.core.Application import ForControlling

class FakeControls(ForControlling):
    def __init__(self, root: str):
        self.__root = root

    def resource_root(self) -> str:
        return self.__root
