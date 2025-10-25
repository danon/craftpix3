import os.path

from hex.core.Application import Application
from hex.core.GameLoop import GameLoop
from hex.core.port import ForReadingSpriteFiles, ForRenderingView, ForRunningGame
from hex.core.SpritePreview import SpritePreview
from hex.infra.OsFileSystem import OsFileSystem
from hex.infra.PygameController import PygameController
from hex.infra.PygameEngine import PygameEngine
from hex.infra.PygameWindow import PygameWindow

def main(test_mode: bool):
    preview_sprites = False
    root = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resource')
    engine = PygameEngine(2048, 1152, test_mode)
    app = __app(
        preview_sprites,
        PygameWindow(engine),
        OsFileSystem(root))
    controller = PygameController(engine)
    loop = GameLoop(controller, app)
    loop.tick()
    if test_mode:
        engine.close()
    loop.start()

def __app(preview: bool, window: ForRenderingView, fs: ForReadingSpriteFiles) -> ForRunningGame:
    if preview:
        return SpritePreview(window, fs)
    return Application(window, fs)

if __name__ == '__main__':
    main(False)
