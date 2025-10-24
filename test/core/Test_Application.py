from hex.core.Application import Application
from hex.core.port import ForControlling, ForReadingSpriteFiles

def test():
    application: ForControlling = Application(FakeFileSystem([
        'frame1.png', 'frame2.png'
    ]))
    assert application.frames() == [
        '/sprite/frame1.png',
        '/sprite/frame2.png',
    ]

class FakeFileSystem(ForReadingSpriteFiles):
    def __init__(self, files: list[str]):
        self.__files = files

    def list_files(self, path: str) -> list[str]:
        return self.__files

    def root(self) -> str:
        return '/root'
