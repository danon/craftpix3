from hex.core.port import ForReadingUserInput, ForRunningGame, WindowEvent

class GameLoop:
    def __init__(self, game: ForRunningGame, input: ForReadingUserInput):
        self.__game = game
        self.__input = input
        self.__is_running = True

    def tick(self):
        self.__game.tick()

    def start(self):
        while self.__is_running:
            self.__game.tick()
            self.__poll_events()

    def __poll_events(self) -> None:
        for event in self.__input.poll_events():
            if event == WindowEvent.Close:
                self.__is_running = False
