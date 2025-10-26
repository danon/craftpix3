from hex.core.Color import DARK_GRAY
from hex.core.GameWorld import GameWorld, PlayerStance
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
        self.__hero_walk = self.__loader.sprite(f'hero/knight1/walk')
        self.__game_world = GameWorld()
        self.__ticks = 0

    def right(self, active: bool):
        self.__game_world.player_move_right(active)

    def left(self, active: bool):
        self.__game_world.player_move_left(active)

    def click(self):
        pass

    def tick(self):
        self.__game_world.tick()
        self.__window.fill_background(DARK_GRAY)
        pos = Point(self.__game_world.player_x, 0)
        if self.__game_world.player_stance == PlayerStance.Idle:
            sprite = self.__hero_idle
        else:
            sprite = self.__hero_walk
        self.__window.draw_frame(self.__loader.abs_path(
            sprite.frames[self.__ticks % len(sprite.frames)]
        ), pos)
        self.__window.draw_text(str(self.__game_world.player_stance), pos)
        self.__window.render_finish()
        self.__ticks += 1
