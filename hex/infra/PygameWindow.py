import pygame

from hex.core.Color import Color, LIGHT_GRAY
from hex.core.Point import Point
from hex.core.port import ForRenderingView
from hex.core.Rect import Rect
from hex.infra.PygameEngine import PygameEngine

class PygameWindow(ForRenderingView):
    def __init__(self, engine: PygameEngine):
        self.__engine = engine
        self.__font = pygame.font.Font(None, 24)

    def fill_background(self, color: Color):
        self.__engine.screen.fill(pc(color))

    def draw_frame(self, path: str, pos: Point, flipped: bool) -> None:
        image = pygame.image.load(path)
        if flipped:
            flipped_image = pygame.transform.flip(image, True, False)
        else:
            flipped_image = image
        self.__draw_image_border(pos, flipped_image)

    def __draw_image_border(self, pos: Point, image):
        self.__engine.screen.blit(image, pp(pos))
        self.__engine.draw_rect(self.__image_rect(pos, image), LIGHT_GRAY)

    def __image_rect(self, pos: Point, image) -> Rect:
        return Rect(image.get_width(), image.get_height(), pos.x, pos.y)

    def draw_text(self, text: str, pos: Point):
        render = self.__font.render(text, True, pc(LIGHT_GRAY))
        self.__engine.screen.blit(render, pp(pos))

    def render_finish(self):
        self.__engine.flip()

def pc(color: Color) -> tuple[int, int, int]:
    """Pygame Color"""
    return color.r, color.g, color.b

def pp(point: Point) -> tuple[int, int]:
    """Pygame Point"""
    return point.x, point.y
