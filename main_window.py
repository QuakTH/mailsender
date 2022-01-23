from PyQt5.QtWidgets import QWidget, QDesktopWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class MainWindow(QWidget):
    '''
    메인 UI
    '''

    def __init__(self):
        '''
        생성자
        '''
        super().__init__()
        self.vert_layout = QVBoxLayout()
        self.ui_init()

    def ui_init(self):
        '''
        UI를 생성하는 실질적인 메소드
        '''
        self.setWindowTitle('메일 자동화 프로그램')
        self.resize(600, 400)

        # 메일 보낼 수단 선택 layout
        mail_select_layout = self.create_mail_select()

        self.vert_layout.addStretch(1)
        self.vert_layout.addLayout(mail_select_layout)
        self.vert_layout.addStretch(3)
        self.setLayout(self.vert_layout)

        self.center_window()
        self.show()

    def center_window(self):
        '''
        window를 화면 중앙에 배치
        '''
        frame_geom = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame_geom.moveCenter(center)
        self.move(frame_geom.topLeft())

    def create_mail_select(self):
        '''
        메일 보내는 사이트를 정하는 layout을 구현하는 메소드
        '''
        mail_select_hbox = QHBoxLayout()

        mail_select_label = QLabel('메일 사이트 선택 :')
        mail_select_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        mail_select_label.setFont(QFont('굴림', 13, 90))

        radio_group = QButtonGroup()

        naver_radio_btn = QRadioButton('네이버')
        naver_radio_btn.setFont(QFont('굴림', 13))
        radio_group.addButton(naver_radio_btn)

        google_radio_btn = QRadioButton('구글')
        google_radio_btn.setFont(QFont('굴림', 13))
        radio_group.addButton(google_radio_btn)

        daum_radio_btn = QRadioButton('다음')
        daum_radio_btn.setFont(QFont('굴림', 13))
        radio_group.addButton(daum_radio_btn)

        mail_select_hbox.addStretch(1)
        mail_select_hbox.addWidget(mail_select_label)
        mail_select_hbox.addStretch(1)
        mail_select_hbox.addWidget(naver_radio_btn)
        mail_select_hbox.addWidget(google_radio_btn)
        mail_select_hbox.addWidget(daum_radio_btn)
        mail_select_hbox.addStretch(1)

        return mail_select_hbox
