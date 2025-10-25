import pygame

from hex.core.Color import Color
from hex.core.port import ForRenderingView
from hex.infra.PygameEngine import PygameEngine

class PygameWindow(ForRenderingView):
    def __init__(self, engine: PygameEngine):
        self.__engine = engine

    def fill_background(self, color: Color):
        self.__engine.screen.fill((color.r, color.g, color.b))

    def draw_frame(self, path: str, x: int, y: int) -> None:
        self.__engine.screen.blit(pygame.image.load(path), (x, y))

    def render_finish(self):
        self.__engine.flip()
