import os.path

from hex.CliTerminal import CliTerminal
from hex.core.Application import Application
from hex.core.GameLoop import GameLoop
from hex.OsFileSystem import OsFileSystem
from hex.PygameController import PygameController
from hex.PygameEngine import PygameEngine
from hex.PygameWindow import PygameWindow

def main(test_mode: bool):
    root = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resource')
    engine = PygameEngine()
    app = Application(
        PygameWindow(engine),
        OsFileSystem(root),
        CliTerminal())
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
# - actually render a window
