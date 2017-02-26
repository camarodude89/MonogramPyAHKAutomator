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
        if not os.path.isfile('locationPaths.json'):
            self.initWizardUI()

    def clearLayout(self, layout=None):
        layout = self.layout() if layout == None else layout
        for i in reversed(range(layout.count())):
            layoutItem = layout.itemAt(i)
            if issubclass(layoutItem.__class__, QLayout):
                self.clearLayout(layout=layoutItem)
                continue
            widgetToRemove = layoutItem.widget()
            layout.removeWidget(widgetToRemove)
            #remove widget from the GUI
            widgetToRemove.setParent(None)

    def initWizardUI(self):

        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('MonogramPyAHKAutomator')
        self.setWindowIcon(QIcon('web.png'))

        self.title = QLabel()
        self.title.setText(self.wizInitialTxt)
        self.title.setAlignment(Qt.AlignTop)
        self.title.setWordWrap(True)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.title)

        self.buttonLayout = QHBoxLayout()

        self.nextBtn = QPushButton("Continue", self)
        self.nextBtn.clicked.connect(self.next_screen)
        self.exitBtn = QPushButton("Exit", self)
        self.exitBtn.clicked.connect(self.close)

        self.buttonLayout.addWidget(self.nextBtn)
        self.buttonLayout.addWidget(self.exitBtn)
        self.mainLayout.addLayout(self.buttonLayout)

        self.setLayout(self.mainLayout)

        self.show()

    def next_screen(self):
        self.clearLayout()
