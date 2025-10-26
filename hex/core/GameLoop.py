from hex.core.port import ForReadingUserInput, ForRunningGame, WindowEvent

class GameLoop:
    def __init__(self, input: ForReadingUserInput, game: ForRunningGame):
        self.__input = input
        self.__game = game
        self.__is_running = True

    def start(self):
        while self.__is_running:
            self.tick()

    def tick(self):
        self.__poll_events()
        self.__game.tick()

    def __poll_events(self) -> None:
        for event in self.__input.poll_events():
            match event:
                case WindowEvent.Close:
                    self.__is_running = False
                case WindowEvent.Click:
                    self.__game.click()
                case WindowEvent.LeftDown:
                    self.__game.left(True)
                case WindowEvent.RightDown:
                    self.__game.right(True)
                case WindowEvent.LeftUp:
                    self.__game.left(False)
                case WindowEvent.RightUp:
                    self.__game.right(False)
