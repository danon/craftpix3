import os
from abc import ABC, abstractmethod

class FileSystem(ABC):
    @abstractmethod
    def list_files(self, path: str) -> list[str]:
        pass

class ResourceFs(FileSystem):
    def list_files(self, path: str) -> list[str]:
        result = []
        for subdir, dirs, files in os.walk(path):
            for file in files:
                result.append(file)
        return result
