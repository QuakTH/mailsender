from PyQt5.QtWidgets import QWidget, QDesktopWidget


class MainWindow(QWidget):
    '''
    메인 UI
    '''
    def __init__(self):
        '''
        생성자
        '''
        super().__init__()
        self.ui_init()

    def ui_init(self):
        '''
        UI를 생성하는 실질적인 메소드
        '''
        self.setWindowTitle('메일 자동화 프로그램')
        self.resize(600, 400)
        self.center_window()
        self.show()

    def center_window(self):
        '''
        window를 화면 중앙에 배치
        '''
        frame_geom=self.frameGeometry()
        center=QDesktopWidget().availableGeometry().center()
        frame_geom.moveCenter(center)
        self.move(frame_geom.topLeft())