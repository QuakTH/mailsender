from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

from gui.layouts.base_layout import BaseLayout

class EmailExampleLayout(BaseLayout):
    def set_layout(self):
        self.email_example_button = QPushButton("이메일 예시 확인")
        self.email_example_button.setFont(QFont("굴림", 13))
        self.email_example_button.clicked.connect(self.email_example_click_event)
        self.email_example_button.setMaximumWidth(300)
        self.email_example_button.setMinimumHeight(40)
        self.email_example_button.setEnabled(False)

        self.addWidget(self.email_example_button)

    def email_example_click_event(self):
        self.main_widget.email_example_dialog.show()