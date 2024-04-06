from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from gui.new_main_widget import MainWidget


def main():
    """
    main 함수
    """
    app = QApplication([])
    main_window = QMainWindow()
    main_window.setFixedSize(QSize(650, 490))

    main_widget = MainWidget()
    main_widget.setupUi(main_window)

    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
