from hex.core.Color import DARK_GRAY
from hex.core.GameWorld import GameWorld
from hex.core.Point import Point
from hex.core.port import ForReadingSpriteFiles, ForRenderingView, ForRunningGame
from hex.core.SpriteLoader import SpriteLoader

class Application(ForRunningGame):
    def __init__(
            self,
            window: ForRenderingView,
            fs: ForReadingSpriteFiles):
        self.__window = window
        self.__loader = SpriteLoader(fs)
        self.__hero_idle = self.__loader.sprite(f'hero/knight1/idle')
        self.__game_world = GameWorld()

    def right(self, active: bool):
        self.__game_world.player_move_right(active)

    def left(self, active: bool):
        self.__game_world.player_move_left(active)

    def click(self):
        pass

    def tick(self):
        self.__game_world.tick()
        self.__window.fill_background(DARK_GRAY)
        self.__window.draw_frame(
            self.__loader.abs_path(self.__hero_idle.frames[0]),
            Point(self.__game_world.player_x, 0))
        self.__window.render_finish()
