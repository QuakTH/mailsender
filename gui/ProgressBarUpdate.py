import time

from PyQt5.QtCore import QThread, pyqtSignal


class ProgressBarThread(QThread):
    progress = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.process_cnt = 0
        self.total_cnt = 0
        self.do_next = True

    def run(self):
        while True:
            if self.total_cnt == 0:
                continue
            self.do_next = False
            self.progress.emit(int(self.process_cnt / self.total_cnt * 100))
            time.sleep(1)
            self.do_next = True
