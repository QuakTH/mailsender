from typing import TYPE_CHECKING

from PyQt5.QtWidgets import *

if TYPE_CHECKING:
    from gui.main_widget import MainWidget


class BaseLayout(QHBoxLayout):
    def __init__(self, main_widget: 'MainWidget') -> None:
        super().__init__()
        self.set_layout()
        self.main_widget = main_widget

    def set_layout(self):
        raise NotImplementedError
