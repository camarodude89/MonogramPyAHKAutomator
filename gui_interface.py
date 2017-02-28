from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, QLabel,
QWidget, QPushButton, QLayout, QLineEdit)
import os

class GUIInterface(QWidget):

    wizInitialTxt = """<div style=\"font-family:Segoe UI;\">
    <h1 align=\"center\">MonogramPyAHKAutomator Setup Wizard</h1>
    <span style=\"font-size:10pt;\" align=\"left\">
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

    locChooseTxt = """<div align=\"left\">
    <h3 style=\"font-family:Segoe UI;\">MonogramPyAHKAutomator Setup Wizard</h3>
    <p style=\"font-size:10pt;\">Enter the physical location of the servers from
    which you will be installing software. (Ex: Memphis for MEM-APP,
    Martinsville for MMSMV-SVR1, etc.)</p>"""

    locTxtBoxLblTxt = """<div align=\"left\" style=\"font-family:Segoe UI;
    font-size:10pt;\">Default Location:</div>"""


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
            self.currentScreen = ["Wizard", 0]
            self.wizLayout = QVBoxLayout()
            self.wizBtnLayout = QHBoxLayout()
            self.init_wizard_UI()

    def clear_layout(self, layout=None):

        layout = self.layout() if layout == None else layout
        for i in reversed(range(layout.count())):
            layoutItem = layout.itemAt(i)
            if issubclass(layoutItem.__class__, QLayout):
                self.clear_layout(layout=layoutItem)
                #removes the sublayout from the main layout
                self.layout().removeItem(layoutItem)
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

        self.wizLayout.addWidget(intro)

        continueBtn = QPushButton("Continue", self)
        GUIInterface.font_size(continueBtn)
        continueBtn.clicked.connect(self.next_screen)
        exitBtn = QPushButton("Exit", self)
        GUIInterface.font_size(exitBtn)
        exitBtn.clicked.connect(self.close)

        self.wizBtnLayout.addWidget(continueBtn)
        self.wizBtnLayout.addWidget(exitBtn)
        self.wizLayout.addLayout(self.wizBtnLayout)

        self.setLayout(self.wizLayout)

        self.show()

    def location_chooser(self):

        desc = QLabel()
        desc.setText(self.locChooseTxt)
        desc.setAlignment(Qt.AlignTop)
        desc.setWordWrap(True)

        locTxtAndLblBoxLayout = QHBoxLayout()

        locTxtBoxLbl = QLabel()
        locTxtBoxLbl.setText(self.locTxtBoxLblTxt)
        locTxtBoxLbl.setAlignment(Qt.AlignCenter)

        self.locTxtBox = QLineEdit()
        GUIInterface.font_size(self.locTxtBox)

        locTxtAndLblBoxLayout.addWidget(locTxtBoxLbl)
        locTxtAndLblBoxLayout.addWidget(self.locTxtBox)
        locTxtAndLblBoxLayout.setAlignment(Qt.AlignTop)

        backBtn = QPushButton("< Back", self)
        GUIInterface.font_size(backBtn)
        backBtn.clicked.connect(self.prev_screen)
        nextBtn = QPushButton("Next >", self)
        GUIInterface.font_size(nextBtn)
        nextBtn.clicked.connect(self.next_screen)

        self.wizBtnLayout.addWidget(backBtn)
        self.wizBtnLayout.addWidget(nextBtn)

        self.wizLayout.addWidget(desc)
        self.wizLayout.addLayout(locTxtAndLblBoxLayout)
        self.wizLayout.addLayout(self.wizBtnLayout)

        self.setLayout(self.wizLayout)

        self.show()

    def next_screen(self):

        self.clear_layout()

        self.currentScreen[1] += 1
        func = self.guiSwitcher.get(self.currentScreen[0]).get(self.currentScreen[1])
        return func()

    def prev_screen(self):

        self.clear_layout()

        self.currentScreen[1] -= 1
        func = self.guiSwitcher.get(self.currentScreen[0]).get(self.currentScreen[1])
        return func()

    @staticmethod
    def font_size(curWidget, size=10):

        font = curWidget.font()
        font.setPointSize(size)
        curWidget.setFont(font)
