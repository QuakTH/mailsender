from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

from gui.layouts.base_layout import BaseLayout

class SendButtonLayout(BaseLayout):
    def set_layout(self):
        self.email_send_button = QPushButton("이메일 보내기")
        self.email_send_button.setFont(QFont("굴림", 13, 100))
        self.email_send_button.setMaximumWidth(250)
        self.email_send_button.setMinimumHeight(60)
        self.email_send_button.setEnabled(False)
        self.email_send_button.setStyleSheet("background-color:#DDDD11")

        self.addWidget(self.email_send_button)