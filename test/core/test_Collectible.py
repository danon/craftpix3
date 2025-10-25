from hex.core.SpriteLoader import Sprite

class Collectible:
    def __init__(
            self,
            sprite: Sprite,
            idle: int = 0,
            starting_tick=0):
        self.__sprite = sprite
        self.__idle = idle
        self.__sprite_length = len(self.__sprite.frames)
        self.__animation_length = self.__sprite_length + self.__idle

        self.__set_tick(starting_tick)

    def tick(self):
        self.__set_tick(self.__ticks + 1)

    def __set_tick(self, ticks: int):
        self.__ticks = ticks % self.__animation_length

    def frame(self) -> str:
        if self.__ticks < self.__sprite_length:
            return self.__sprite.frames[self.__ticks]
        return self.__sprite.frames[0]

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

def test_collectible_stays_on_first_frame_for_more_ticks():
    sprite = Sprite(['frame1.png', 'frame2.png', 'frame3.png'])
    assert frames(sprite, idle=5) == [
        'frame1.png', 'frame2.png', 'frame3.png',
        'frame1.png', 'frame1.png', 'frame1.png', 'frame1.png', 'frame1.png',
        'frame1.png', 'frame2.png', 'frame3.png'
    ]

def frames(sprite: Sprite, idle: int) -> list[str]:
    return [
        Collectible(sprite, idle, tick).frame()
        for tick in range(0, 11)
    ]
