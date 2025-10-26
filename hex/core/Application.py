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
        self.hero_idle = self.__loader.sprite(f'hero/knight1/idle')
        self.game_world = GameWorld()

    def right(self):
        self.game_world.player_move_right()

    def left(self):
        self.game_world.player_move_left()

    def click(self):
        pass

    def tick(self):
        self.__window.fill_background(DARK_GRAY)
        self.__window.draw_frame(
            self.__loader.abs_path(self.hero_idle.frames[0]),
            Point(self.game_world.player_x, 0))
        self.__window.render_finish()
