from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from gui.layouts.base_layout import BaseLayout


class EmailPasswordLayout(BaseLayout):
    def set_layout(self):
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

        self.addStretch(3)
        self.addWidget(email_label)
        self.addStretch(1)
        self.addWidget(email_edit)
        self.addStretch(2)
        self.addWidget(pass_label)
        self.addStretch(1)
        self.addWidget(pass_edit)
        self.addStretch(3)