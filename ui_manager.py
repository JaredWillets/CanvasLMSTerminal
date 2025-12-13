import sys
import termios
import tty
import threading
import shutil

class UIManager:
    def __init__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)          # put terminal in raw mode
            ch = sys.stdin.read(1)  # read one character immediately
            print(f"\nYou pressed: {repr(ch)}")
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        
        self.input_thread = threading.Thread(target = self._input)
        self.update_thread = threading.Thread(target = self._update)

    def start(self):
        self.input_thread.start()
        self.update_thread.start()

    def _input(self):
        pass ## TODO

    def _update(self):
        pass ## TODO 

    
if __name__ == "__main__":
    manager = UIManager()
    