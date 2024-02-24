from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from gui.layouts.base_layout import BaseLayout

class EmailListLayout(BaseLayout):
    def set_layout(self):
        self.email_list_file = QLabel("선택된 이메일 리스트 파일 없음")
        self.email_list_file.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.email_list_file.setFont(QFont("굴림", 13, 90))

        self.addStretch(1)
        self.addWidget(self.email_list_file)
        self.addStretch(1)