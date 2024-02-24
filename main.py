from PyQt5.QtWidgets import QApplication
import sys

from gui.main_window import MainWindow


def main():
    '''
    main 함수
    '''
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
