from hex.core.port import ForReadingSpriteFiles

class Sprite:
    def __init__(self, frames: list[str]):
        self.frames = frames

class SpriteLoader:
    def __init__(self, fs: ForReadingSpriteFiles):
        self.__fs = fs

    def sprite(self, path: str) -> Sprite:
        return Sprite([
            path + '/' + file
            for file
            in self.__fs.list_files(path)
        ])

    def abs_path(self, path: str) -> str:
        return self.__fs.root() + '/resource/' + path
