from PyQt5.QtWidgets import *

from gui.main_widget import MainWidget

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
            lambda: self.open_file_dialog('이메일 목록 파일 선택', 'EXCEL,CSV(*.xlsx *.csv)'))

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
            self.main_widget.send_button_layout.email_send_button.setEnabled(True)
        else:
            self.main_widget.send_button_layout.email_send_button.setEnabled(False)

        return None