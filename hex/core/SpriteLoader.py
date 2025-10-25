import os.path
import re
from dataclasses import dataclass

from hex.core.port import ForReadingSpriteFiles

class Sprite:
    def __init__(self, frames: list[str]):
        self.frames = frames

@dataclass
class Frame:
    path: str

    def index(self) -> int:
        return self.__extracted_number(self.__basename())

    def __basename(self):
        return os.path.basename(self.path)

    def __extracted_number(self, string: str) -> int:
        index = re.search(r'\d+', string)
        if index is None:
            raise Exception('Failed to parse sprite frame filename: ' + string)
        return int(index.group())

class SpriteLoader:
    def __init__(self, fs: ForReadingSpriteFiles):
        self.__fs = fs

    def sprite(self, path: str) -> Sprite:
        return Sprite([
            path + '/' + frame.path
            for frame
            in
            sorted(
                self.__sprite_frames(path),
                key=lambda frame: frame.index())
        ])

    def __sprite_frames(self, path: str) -> list[Frame]:
        return [
            Frame(path)
            for path in self.__fs.list_files(path)
        ]

    def abs_path(self, path: str) -> str:
        return self.__fs.root() + '/' + path
