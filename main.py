import sys
from PyQt5.QtWidgets import QApplication
from gui_interface import GUIInterface
import json

if __name__ == '__main__':

    app = QApplication(sys.argv)
    gi = GUIInterface()
    sys.exit(app.exec_())
