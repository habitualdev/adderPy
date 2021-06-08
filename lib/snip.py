import pyautogui
from pynput import mouse

class GetArea:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.tuple = (0, 0, 0, 0)
        self.listen()

    def click(self, x, y, button, pressed):
        if self.x1 == 0 and self.y1 == 0:
            self.x1 = x
            self.y1 = y
        else:
            self.x2 = x
            self.y2 = y
            return False

    def listen(self):
        with mouse.Listener(on_click=self.click) as listener:
            listener.join()
        with mouse.Listener(on_click=self.click) as listener:
            listener.join()
        self.make_tuple()

    def make_tuple(self):
        width = self.x2 - self.x1
        height = self.y2 - self.y1
        self.tuple = (self.x1, self.y1, width, height)

    def snip(self):
        image = pyautogui.screenshot(region=self.tuple)
        return image


