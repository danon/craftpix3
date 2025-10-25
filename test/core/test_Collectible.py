from hex.core.SpriteLoader import Sprite

class Collectible:
    def __init__(self, sprite: Sprite):
        self.__sprite = sprite
        self.__frame = 0

    def tick(self):
        self.__frame = (self.__frame + 1) % len(self.__sprite.frames)

    def frame(self) -> str:
        return self.__sprite.frames[self.__frame]

def test_collectible_has_first_frame():
    collectible = Collectible(Sprite(['frame1.png', 'frame2.png']))
    assert collectible.frame() == 'frame1.png'

def test_collectible_after_tick__has_first_frame():
    collectible = Collectible(Sprite(['frame1.png', 'frame2.png']))
    collectible.tick()
    assert collectible.frame() == 'frame2.png'

def test_collectible_cycles_frames():
    collectible = Collectible(Sprite(['frame1.png', 'frame2.png', 'frame3.png']))
    collectible.tick()
    collectible.tick()
    collectible.tick()
    assert collectible.frame() == 'frame1.png'
