from pix.game.fs import FileSystem
from pix.game.sprite_loader import SpriteLoader

def test_frames_are_loaded_from_fs():
    sprite_loader = SpriteLoader(FakeFs('/', ['frame1.png', 'frame2.png']))
    sprite = sprite_loader.sprite('sprite/obstacle/rock')
    assert sprite.frames == [
        'sprite/obstacle/rock/frame1.png',
        'sprite/obstacle/rock/frame2.png',
    ]

def test_abs_path():
    sprite_loader = SpriteLoader(FakeFs('/root', []))
    path = sprite_loader.abs_path('sprite/obstacle/rock/frame1.png')
    assert path == '/root/resource/sprite/obstacle/rock/frame1.png'

class FakeFs(FileSystem):
    def __init__(self, root: str, filenames: list[str]):
        self.__root = root
        self.__filenames = filenames

    def list_files(self, path: str) -> list[str]:
        return self.__filenames

    def root(self) -> str:
        return self.__root
