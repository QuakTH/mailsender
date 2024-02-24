from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class EmailExampleWindow(QMainWindow):
    def __init__(self):
        '''
        생성자
        '''
        # 윈도우를 만들고 중앙배치
        super().__init__()

        self.setWindowTitle('이메일 예시')
        self.setFixedSize(300, 200)

        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)

        frame_geom = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame_geom.moveCenter(center)
        self.move(frame_geom.topLeft())