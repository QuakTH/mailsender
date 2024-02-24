from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QFont, QRegExpValidator

from gui.email_example_window import EmailExampleWindow
from gui.layouts.email_example_layout import EmailExampleLayout
from gui.layouts.email_list_layout import EmailListLayout
from gui.layouts.email_password_layout import EmailPasswordLayout
from gui.layouts.mail_sender_select_layout import MailSenderSelectLayout
from gui.layouts.send_button_layout import SendButtonLayout


class MainWidget(QWidget):
    """
    메인 UI
    """

    def __init__(self, parent):
        """
        생성자
        """
        super().__init__(parent)
        self.main_window = parent
        self.vert_layout = QVBoxLayout()
        self.email_example_dialog = EmailExampleWindow()  # 이메일 예시 Dialog
        self.ui_init()

    def ui_init(self):
        """
        UI를 생성하는 실질적인 메소드
        """
        self.mail_sender_select_layout = MailSenderSelectLayout(self)
        self.email_password_layout = EmailPasswordLayout(self)
        self.email_list_layout = EmailListLayout(self)
        self.email_example_layout = EmailExampleLayout(self)
        self.send_button_layout = SendButtonLayout(self)

        self.vert_layout.addStretch(1)
        self.vert_layout.addLayout(self.mail_sender_select_layout)
        self.vert_layout.addStretch(1)
        self.vert_layout.addLayout(self.email_password_layout)
        self.vert_layout.addStretch(1)
        self.vert_layout.addLayout(self.email_list_layout)
        self.vert_layout.addStretch(1)
        self.vert_layout.addLayout(self.email_example_layout)
        self.vert_layout.addStretch(2)
        self.vert_layout.addLayout(self.send_button_layout)
        self.vert_layout.addStretch(6)
        self.setLayout(self.vert_layout)

        self.center_window()
        self.show()

    def center_window(self):
        """
        window를 화면 중앙에 배치
        """
        frame_geom = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame_geom.moveCenter(center)
        self.move(frame_geom.topLeft())

    def set_email_list_label(self, file_path):
        """
        이메일 파일 path를 받으면, 해당 파일명을 보여주게끔 label text 변경

        file_path : 이메일 파일 path
        """
        file_name = file_path.split("/")[-1]

        self.email_list_layout.email_list_file.setText(file_name)
