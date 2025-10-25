import pygame

from hex.core.Color import Color, LIGHT_GRAY
from hex.core.port import ForRenderingView
from hex.core.Rect import Rect
from hex.infra.PygameEngine import PygameEngine

class PygameWindow(ForRenderingView):
    def __init__(self, engine: PygameEngine):
        self.__engine = engine

    def fill_background(self, color: Color):
        self.__engine.screen.fill((color.r, color.g, color.b))

    def draw_frame(self, path: str, x: int, y: int) -> None:
        self.__draw_image_border(x, y, pygame.image.load(path))

    def __draw_image_border(self, x: int, y: int, image):
        self.__engine.screen.blit(image, (x, y))
        self.__engine.draw_rect(self.__image_rect(x, y, image), LIGHT_GRAY)

    def __image_rect(self, x: int, y: int, image) -> Rect:
        return Rect(image.get_width(), image.get_height(), x, y)

    def render_finish(self):
        self.__engine.flip()
