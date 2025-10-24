import os
from pathlib import Path

from pix.game.fs import FileSystem
from pix.game.sprite import Sprite

class SpriteLoader:
    def __init__(self, fs: FileSystem):
        self.__resource_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'resource')
        self.__fs = fs

    def sprite(self, resource: str) -> Sprite:
        return Sprite([
            self.__norm_path(resource, file)
            for file
            in self.__directory_files(resource)
        ])

    def __directory_files(self, resource: str) -> list[str]:
        return self.__fs.list_files(os.path.join(self.__resource_dir, resource))

    def __norm_path(self, resource: str, file: str) -> str:
        return Path(os.path.join(resource, file)).as_posix()
