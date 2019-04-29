from Threading import Thread
import time


def main():
    pass


class TCalc(Thread):
    def __init__(self):
        super(TCalc, self).__init__()
        self.status = "starting"

    def run(self):
        time.sleep(1)
        self.status = "done"


class KillableThread(Thread):
    def __init__(self):
        super(TCalc, self).__init__()
        self.killing = False

    def run(self):
        for i in range(5):
            if self.killing:
                break
        time.sleep(0.2)

    def kill(self):
        self.killing = True
