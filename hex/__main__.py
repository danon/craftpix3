import os.path

from hex.core.Application import Application
from hex.core.GameLoop import GameLoop
from hex.infra.OsFileSystem import OsFileSystem
from hex.infra.PygameController import PygameController
from hex.infra.PygameEngine import PygameEngine
from hex.infra.PygameWindow import PygameWindow

def main(test_mode: bool):
    root = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resource')
    engine = PygameEngine(640, 480, test_mode)
    app = Application(
        PygameWindow(engine),
        OsFileSystem(root))
    controller = PygameController(engine)
    loop = GameLoop(controller, app)
    loop.tick()
    if test_mode:
        engine.close()
    loop.start()

if __name__ == '__main__':
    main(False)

# TODO
# - game updates the element
