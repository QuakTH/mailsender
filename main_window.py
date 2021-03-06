from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5 import QtCore


class MainWindow(QMainWindow):
    '''
    메인 윈도우
    '''

    def __init__(self):
        '''
        생성자
        '''
        super().__init__()
        self.email_list_set = False
        self.email_text_set = False
        self.email_list_file = ''
        self.email_text_file = ''
        self.main_widget = MainWidget(self)
        self.init()

    def init(self):
        '''
        윈도우 창을 띄우고
        안에 MainWidget 객체 넣어줌
        '''

        self.setWindowTitle('메일 자동화 프로그램')
        self.setFixedSize(650, 400)

        # 이메일 목록 및 보낼 이메일 뼈대 파일 불러오는 메뉴바
        email_action = QAction('이메일 목록 선택', self)
        email_action.triggered.connect(
            lambda: self.open_file_dialog('이메일 목록 파일 선택', 'EXCEL(*.xlsx);;CSV(*.csv)'))

        mail_body_action = QAction('이메일 내용 선택', self)
        mail_body_action.triggered.connect(
            lambda: self.open_file_dialog('이메일 내용 파일 선택', 'TEXT(*.txt);;'))

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        file_select = menubar.addMenu('파일')
        file_select.addAction(email_action)
        file_select.addAction(mail_body_action)

        self.setCentralWidget(self.main_widget)

    def open_file_dialog(self, action_name, filter):
        '''
        파일 dialog를 여는 메소드

        action_name : 파일 dialog 제목
        filter : 파일 확장자 필터
        '''
        # 이메일 리스트를 먼저 선택하게끔
        if action_name == '이메일 내용 파일 선택' and not self.email_list_set:
            QMessageBox.warning(self, '주의', '이메일 리스트를 먼저 선택해주세요')
            return None

        fname, _ = QFileDialog.getOpenFileName(
            caption=action_name, filter=filter)

        if fname != '':
            if action_name == '이메일 목록 파일 선택':
                self.main_widget.set_email_list_label(fname)
                self.email_list_file = fname
                self.email_list_set = True
            elif action_name == '이메일 내용 파일 선택':
                self.email_text_file = fname
                self.email_text_set = True
        else:
            if action_name == '이메일 목록 파일 선택':
                self.main_widget.set_email_list_label('선택된 이메일 리스트 파일 없음')
                self.email_list_file = None
                self.email_list_set = False
            else:
                self.email_text_file = None
                self.email_text_set = False

        # 이메일 리스트 및 내용을 받은 경우에 수행
        if self.email_list_set and self.email_text_set:
            QMessageBox.about(self, '알림', '이메일 보내기 준비')
            self.main_widget.email_example_button.setEnabled(True)
        else:
            self.main_widget.email_example_button.setEnabled(False)

        return None


class MainWidget(QWidget):
    '''
    메인 UI
    '''

    def __init__(self, parent):
        '''
        생성자
        '''
        super().__init__(parent)
        self.vert_layout = QVBoxLayout()
        self.email_example_dialog = EmailExampleWindow()  # 이메일 예시 Dialog
        self.ui_init()

    def ui_init(self):
        '''
        UI를 생성하는 실질적인 메소드
        '''
        # self.setWindowTitle('메일 자동화 프로그램')
        # self.resize(600, 400)

        # 메일 보낼 수단 선택 layout
        mail_select_layout = self.create_mail_select()

        # 이메일 비밀번호 입력란 layout
        email_pass_layout = self.create_email_pass()

        # 불러온 이메일 목록 파일명 label
        email_list_hbox = self.create_email_list()

        # 이메일 내용 예시 확인
        email_example_hbox = self.create_email_example_button()

        # 보내기 버튼
        send_button_hbox = self.create_send_button()

        # 수직 레이아웃
        self.vert_layout.addStretch(1)
        self.vert_layout.addLayout(mail_select_layout)
        self.vert_layout.addStretch(1)
        self.vert_layout.addLayout(email_pass_layout)
        self.vert_layout.addStretch(1)
        self.vert_layout.addLayout(email_list_hbox)
        self.vert_layout.addStretch(1)
        self.vert_layout.addLayout(email_example_hbox)
        self.vert_layout.addStretch(2)
        self.vert_layout.addLayout(send_button_hbox)
        self.vert_layout.addStretch(6)
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

    def create_email_pass(self):
        '''
        이메일과 비밀번호를 입력받는 란을 만드는 메소드
        '''
        email_pass_layout = QHBoxLayout()

        email_label = QLabel('EMAIL :')
        email_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        email_label.setFont(QFont('굴림', 13))

        email_edit = QLineEdit()
        email_edit.setFixedWidth(200)

        pass_label = QLabel('PASSWORD :')
        pass_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        pass_label.setFont(QFont('굴림', 13))

        pass_edit = QLineEdit()
        pass_edit.setFixedWidth(170)
        pass_edit.setEchoMode(QLineEdit.EchoMode.Password)

        email_pass_layout.addStretch(3)
        email_pass_layout.addWidget(email_label)
        email_pass_layout.addStretch(1)
        email_pass_layout.addWidget(email_edit)
        email_pass_layout.addStretch(2)
        email_pass_layout.addWidget(pass_label)
        email_pass_layout.addStretch(1)
        email_pass_layout.addWidget(pass_edit)
        email_pass_layout.addStretch(3)

        return email_pass_layout

    def create_email_list(self):
        '''
        불러온 email 목록 파일 명을 표시해주는
        QLabel 및 Layout
        '''
        email_list_hbox = QHBoxLayout()

        self.email_list_file = QLabel('선택된 이메일 리스트 파일 없음')
        self.email_list_file.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.email_list_file.setFont(QFont('굴림', 13, 90))

        email_list_hbox.addStretch(1)
        email_list_hbox.addWidget(self.email_list_file)
        email_list_hbox.addStretch(1)

        return email_list_hbox

    def create_email_example_button(self):
        '''
        이메일 예시를 보여주는 창을 띄우는 button 및 layout
        버튼은 초기에 비활성화
        '''
        email_example_hbox = QHBoxLayout()

        self.email_example_button = QPushButton('이메일 예시 확인')
        self.email_example_button.setFont(QFont('굴림', 13))
        self.email_example_button.clicked.connect(
            self.email_example_click_event)
        self.email_example_button.setMaximumWidth(300)
        self.email_example_button.setMinimumHeight(40)
        self.email_example_button.setEnabled(False)

        email_example_hbox.addWidget(self.email_example_button)

        return email_example_hbox

    def email_example_click_event(self):
        '''
        이메일 예시 button을 클릭할 때,
        이메일 리스트와 이메일 내용을 통해 이메일 예시를
        하나 보여주는 window를 여는 event
        '''
        self.email_example_dialog.show()

    def create_send_button(self):
        '''
        이메일 보내기 버튼 레이아웃
        버튼은 초기에 비활성화
        '''
        send_button_hbox = QHBoxLayout()

        email_send_button = QPushButton('이메일 보내기')
        email_send_button.setFont(QFont('굴림', 13, 100))
        email_send_button.setMaximumWidth(250)
        email_send_button.setMinimumHeight(60)
        email_send_button.setEnabled(False)
        email_send_button.setStyleSheet('background-color:#DDDD11')

        send_button_hbox.addWidget(email_send_button)

        return send_button_hbox

    def set_email_list_label(self, file_path):
        '''
        이메일 파일 path를 받으면, 해당 파일명을 보여주게끔 label text 변경

        file_path : 이메일 파일 path
        '''
        file_name = file_path.split('/')[-1]

        self.email_list_file.setText(file_name)


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
