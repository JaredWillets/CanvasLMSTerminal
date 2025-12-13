import sys
import termios
import tty
import threading
import shutil
from ansi import *
from contextlib import contextmanager

@contextmanager
def raw_mode(file = sys.stdin):
    fd = file.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        yield
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
class UIManager:
    def __init__(self, stop_event = threading.Event()):

        self.stop_event = stop_event
        
        self.input_thread = threading.Thread(target = self._input)
        self.update_thread = threading.Thread(target = self._update)


    def start(self):
        self.input_thread.start()
        self.update_thread.start()

    def _input(self):
        with raw_mode():
            print("Ready for input")
            while not self.stop_event.is_set():
                ch = sys.stdin.read(1)

                if ch == "\x03":
                    self.stop_event.set()
                    break
                else:
                    print(ch, end = "", flush = True)

    def _update(self):
        pass ## TODOs


if __name__ == "__main__":
    manager = UIManager()
    manager.start()