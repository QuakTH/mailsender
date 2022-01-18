from PyQt5.QtWidgets import QWidget, QDesktopWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self):
        self.setWindowTitle('메일 자동화 프로그램')
        self.resize(600, 400)
        self.center_window()
        self.show()

    def center_window(self):
        frame_geom=self.frameGeometry()
        center=QDesktopWidget().availableGeometry().center()
        frame_geom.moveCenter(center)
        self.move(frame_geom.topLeft())