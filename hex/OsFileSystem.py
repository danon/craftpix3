import os

from hex.core.port import ForReadingSpriteFiles

class OsFileSystem(ForReadingSpriteFiles):
    def list_files(self, path: str) -> list[str]:
        result = []
        for subdir, dirs, files in os.walk(path):
            for file in files:
                result.append(file)
        return result

    def root(self) -> str:
        pass
