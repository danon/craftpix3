from hex.core.Color import Color
from hex.core.obstacle import Obstacle
from hex.core.port import ForReadingSpriteFiles, ForRenderingView, ForRunningGame
from hex.core.SpriteLoader import SpriteLoader

class Application(ForRunningGame):
    def __init__(self, window: ForRenderingView, fs: ForReadingSpriteFiles):
        self.__window = window
        self.__loader = SpriteLoader(fs)
        self.__ticks = 0
        self.__obstacles = [
            Obstacle(self.__loader.sprite('obstacle/asid_drop')),
            Obstacle(self.__loader.sprite('obstacle/axe')),
            Obstacle(self.__loader.sprite('obstacle/bomb')),
            Obstacle(self.__loader.sprite('obstacle/chest')),
            Obstacle(self.__loader.sprite('obstacle/fire_skull')),
            Obstacle(self.__loader.sprite('obstacle/ghost_bottle')),
            Obstacle(self.__loader.sprite('obstacle/guillotine')),
            Obstacle(self.__loader.sprite('obstacle/lightning')),
            Obstacle(self.__loader.sprite('obstacle/ram')),
            Obstacle(self.__loader.sprite('obstacle/stone1')),
            Obstacle(self.__loader.sprite('obstacle/stone2')),
            Obstacle(self.__loader.sprite('obstacle/stone3')),
            Obstacle(self.__loader.sprite('obstacle/stone4')),
            Obstacle(self.__loader.sprite('obstacle/trap')),
            Obstacle(self.__loader.sprite('obstacle/web')),
        ]
        self.__obstacle_index = 6

    def tick(self):
        for element in self.__obstacles:
            element.tick()
        self.__window.fill_background(Color(30, 31, 34))
        self.__window.draw_frame(
            self.__loader.abs_path(self.__current_obstacle().frame())
        )
        self.__window.render_finish()
        self.__ticks += 1

    def __current_obstacle(self) -> Obstacle:
        return self.__obstacles[self.__obstacle_index]

    def click(self):
        for element in self.__obstacles:
            element.initiate()

    def left(self):
        self.__obstacle_index -= 1

    def right(self):
        self.__obstacle_index = (self.__obstacle_index + 1) % len(self.__obstacles)
