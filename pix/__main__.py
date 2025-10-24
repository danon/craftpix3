import pygame

from pix.game.fs import OsFileSystem
from pix.game.sprite_loader import SpriteLoader
from pix.game.state import Element, GameState
from pix.loop import GameLoop, Window, WindowEvent

class Application:
    def start(self):
        sprite_loader = SpriteLoader(OsFileSystem())
        game_state = GameState()
        game_state.element = Element(sprite_loader.sprite('sprite/obstacle/lightning'))
        window = PygameWindow(640, 480)
        loop = GameLoop(game_state, window)
        while loop._running:
            window.fill_background(30, 31, 34)
            window.draw_frame(0, 0, sprite_loader.abs_path(game_state.element.frame()))
            window.render()
            loop.tick()

class PygameWindow(Window):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.__screen = pygame.display.set_mode((width, height))
        self.__clock = pygame.time.Clock()

    def poll_events(self) -> list[WindowEvent]:
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                events.append(WindowEvent.Close)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    events.append(WindowEvent.Click)
        return events

    def fill_background(self, r: int, g: int, b: int) -> None:
        self.__screen.fill((r, g, b))

    def draw_frame(self, x: int, y: int, path: str) -> None:
        self.__screen.blit(pygame.image.load(path), (x, y))

    def render(self) -> None:
        pygame.display.flip()
        self.__clock.tick(16)

if __name__ == '__main__':
    Application().start()
