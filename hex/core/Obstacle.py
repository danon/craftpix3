from hex.core.SpriteLoader import Sprite

class Obstacle:
    def __init__(self, sprite: Sprite):
        self.__sprite = sprite
        self.__initiated = False
        self.__frame = 0

    def initiate(self) -> None:
        self.__initiated = True

    def tick(self) -> None:
        if self.__initiated:
            self.__frame += 1
            if self.__frame == len(self.__sprite.frames):
                self.__initiated = False
                self.__frame = 0

    def frame(self) -> str:
        return self.__sprite.frames[self.__frame]
