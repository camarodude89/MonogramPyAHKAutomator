from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, QLabel,
QWidget, QPushButton, QLayout)
import os

class GUIInterface(QWidget):

    wizInitialTxt = """<div align=\"center\">
    <h1 style=\"font-family:Segoe UI;\">MonogramPyAHKAutomator Setup Wizard</h1>
    <span style=\"font-family:Segoe UI; font-size:10pt;\" align=\"left\">
    <p>Before using the MonogramPyAHKAutomator
    (MPAHKA), you must first setup the default file locations for each software
    to be automated. This will tell MPAHKA where to look for the setup
    executables for each program. The file locations can be edited later if
    needed.</p>

    <p>You will also have the opportunity to setup file locations based on site
    names such as Memphis, Martinsville, Chandler, etc. for fast setup of the
    desktop or laptop based on the location from which you are setting up the
    machine. This will allow for faster access to the setup files by accessing
    them on a local server rather than a remote one.</p>

    <p>The currently supported software is Adobe Reader, CutePDF and ShoreTel
    Communicator.</p></span></div>"""

    def __init__(self):

        super().__init__()
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('MonogramPyAHKAutomator')
        self.setWindowIcon(QIcon('web.png'))

        self.guiSwitcher = {
            "Wizard": {
                0: self.init_wizard_UI,
                1: self.location_chooser
            }
        }

        if os.path.isfile('locationPaths.json'):
            pass
        else:
            self.init_wizard_UI()
            self.currentScreen = ("Wizard", 0)

    def clear_layout(self, layout=None):

        layout = self.layout() if layout == None else layout
        for i in reversed(range(layout.count())):
            layoutItem = layout.itemAt(i)
            if issubclass(layoutItem.__class__, QLayout):
                self.clear_layout(layout=layoutItem)
                continue
            widgetToRemove = layoutItem.widget()
            layout.removeWidget(widgetToRemove)
            #remove widget from the GUI
            widgetToRemove.setParent(None)

    def init_wizard_UI(self):

        intro = QLabel()
        intro.setText(self.wizInitialTxt)
        intro.setAlignment(Qt.AlignTop)
        intro.setWordWrap(True)

        self.wizLayout = QVBoxLayout()
        self.wizLayout.addWidget(intro)

        self.wizBtnLayout = QHBoxLayout()

        nextBtn = QPushButton("Continue", self)
        nextBtn.clicked.connect(self.next_screen)
        exitBtn = QPushButton("Exit", self)
        exitBtn.clicked.connect(self.close)

        self.wizBtnLayout.addWidget(nextBtn)
        self.wizBtnLayout.addWidget(exitBtn)
        self.wizLayout.addLayout(self.wizBtnLayout)

        self.setLayout(self.wizLayout)

        self.show()

    def location_chooser(self):
        pass

    def next_screen(self):

        self.clear_layout()

        #currentScreen[1] += 1
        #func = guiSwitcher.get(self.currentScreen[0]).get(self.currentScreen[1])
        #return func()
