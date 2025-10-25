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
            if event == WindowEvent.Close:
                self.__is_running = False
            if event == WindowEvent.Click:
                self.__game.click()
