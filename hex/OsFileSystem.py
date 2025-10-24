import os

from hex.core.port import ForReadingSpriteFiles

class OsFileSystem(ForReadingSpriteFiles):
    def __init__(self, root: str):
        self.__root = root

    def list_files(self, path: str) -> list[str]:
        directory = os.path.join(self.__root, path)
        result = []
        for subdir, dirs, files in os.walk(directory):
            for file in files:
                result.append(file)
        return result

    def root(self) -> str:
        pass
