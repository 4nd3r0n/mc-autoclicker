from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from time import sleep

mouse = MouseController()
keyboard = KeyboardController()

class AutoClick():
    def __init__(self, time: float=0.5) -> None:
        self.time=time
        self.to_stop=True

    def stop(self) -> None:
        self.to_stop=True

    def start(self) -> None:
        self.to_stop=False
        while not self.to_stop:
            mouse.click(Button.right)
            sleep(self.time)
