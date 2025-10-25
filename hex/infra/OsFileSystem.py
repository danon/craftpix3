import os

from hex.core.port import ForReadingSpriteFiles

class OsFileSystem(ForReadingSpriteFiles):
    def __init__(self, root: str):
        self.__root = root

    def list_files(self, path: str) -> list[str]:
        directory = os.path.join(self.__root, path)
        if not os.path.exists(directory):
            raise Exception('Directory does not exist: ' + path)
        children = os.listdir(directory)
        for child in children:
            if os.path.isdir(os.path.join(directory, child)):
                raise Exception('Expected a file in sprite directory, found: ' + path + '/' + child)
        return children

    def root(self) -> str:
        return self.__root
