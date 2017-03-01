from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, QLabel,
QWidget, QPushButton, QLayout, QLineEdit, QFileDialog)
from json_handler import JSONHandler
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

    locChooseTxt = """<div align=\"left\" style=\"font-family:Segoe UI;\">
    <h3>MonogramPyAHKAutomator Setup Wizard</h3>
    <p style=\"font-size:10pt;\">Enter the physical location of the servers from
    which you will be installing software. (Ex: Memphis for MEM-APP,
    Martinsville for MMSMV-SVR1, etc.)</p>"""

    locTxtBoxLblTxt = """<div align=\"left\" style=\"font-family:Segoe UI;
    font-size:10pt;\">Default Location:</div>"""

    fileChooserTxt1 = """<div align=\"left\" style=\"font-family:Segoe UI;\">
    <h3>MonogramPyAHKAutomator Setup Wizard</h3>
    <p style=\"font-size:10pt;\">Enter the path to the setup file for <b>"""

    fileChooserTxt2 = "</b>.</div>"

    setupCompleteTxt = """<div align=\"left\" style=\"font-family:Segoe UI;\">
    <h3>MonogramPyAHKAutomator Setup Wizard</h3>
    <p style=\"font-size:10pt;\">Setup has been completed. Select the Finish
    button to exit.</p></div>"""


    def __init__(self):

        super().__init__()
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('MonogramPyAHKAutomator')
        self.setWindowIcon(QIcon('web.png'))

        self.guiSwitcher = {
            "Wizard": {
                0: self.init_wizard_ui,
                1: self.location_chooser_ui,
                2: self.file_chooser_ui,
                3: self.file_chooser_ui,
                4: self.file_chooser_ui,
                5: self.setup_complete_ui
            },
            "Automator": {
                0: self.init_automator_ui
            }
        }

        self.softwareList = ["Adobe Reader", "CutePDF",
        "ShoreTel Communicator"]

        self.softwarePathList = [""] * 3

        if os.path.isfile('locationPaths.json'):
            self.currentScreen = ["Automator", 0]
            self.init_automator_ui()
        else:
            self.currentScreen = ["Wizard", 0]
            self.firstRun = True
            self.wizLayout = QVBoxLayout()
            self.wizBtnLayout = QHBoxLayout()
            self.init_wizard_ui()

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

    def init_wizard_ui(self):

        if not self.firstRun:
            self.clear_layout()

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

        self.firstRun = False

    def location_chooser_ui(self):

        self.clear_layout()

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

    def file_chooser_ui(self):

        self.text_scrape()
        self.clear_layout()

        desc = QLabel()
        desc.setText(self.fileChooserTxt1 +
                    self.softwareList[self.currentScreen[1] - 2] +
                    self.fileChooserTxt2)
        desc.setAlignment(Qt.AlignTop)
        desc.setWordWrap(True)

        fileChooserHBoxLayout = QHBoxLayout()

        self.fileLocTxtBox = QLineEdit()
        GUIInterface.font_size(self.fileLocTxtBox)

        browseBtn = QPushButton("Browse...", self)
        GUIInterface.font_size(browseBtn)
        browseBtn.clicked.connect(self.choose_file)

        fileChooserHBoxLayout.addWidget(self.fileLocTxtBox)
        fileChooserHBoxLayout.addWidget(browseBtn)
        fileChooserHBoxLayout.setAlignment(Qt.AlignTop)

        backBtn = QPushButton("< Back", self)
        GUIInterface.font_size(backBtn)
        backBtn.clicked.connect(self.prev_screen)
        nextBtn = QPushButton("Next >", self)
        GUIInterface.font_size(nextBtn)
        nextBtn.clicked.connect(self.next_screen)

        self.wizBtnLayout.addWidget(backBtn)
        self.wizBtnLayout.addWidget(nextBtn)

        self.wizLayout.addWidget(desc)
        self.wizLayout.addLayout(fileChooserHBoxLayout)
        self.wizLayout.addLayout(self.wizBtnLayout)

        self.setLayout(self.wizLayout)

        self.show()

    def setup_complete_ui(self):

        self.text_scrape()
        JSONHandler.jsonify(self.defaultLocation,
                            self.softwareList, self.softwarePathList)
        self.clear_layout()

        desc = QLabel()
        desc.setText(self.setupCompleteTxt)
        desc.setAlignment(Qt.AlignTop)
        desc.setWordWrap(True)

        finishBtn = QPushButton("Finish", self)
        GUIInterface.font_size(finishBtn)
        #finishBtn.setFixedWidth(100)
        finishBtn.clicked.connect(self.close)

        self.wizLayout.addWidget(desc)
        self.wizLayout.addWidget(finishBtn)

        self.setLayout(self.wizLayout)

        self.show()

    def init_automator_ui(self):

        stuff = QLabel()
        stuff.setText("Things and stuff go here!!!")
        stuff.setAlignment(Qt.AlignTop)
        stuff.setWordWrap(True)

        self.autoLayout = QVBoxLayout()

        self.autoLayout.addWidget(stuff)

        self.setLayout(self.autoLayout)

        self.show()

    def next_screen(self):

        self.currentScreen[1] += 1
        func = self.guiSwitcher.get(self.currentScreen[0]).get(self.currentScreen[1])
        return func()

    def prev_screen(self):

        self.currentScreen[1] -= 1
        func = self.guiSwitcher.get(self.currentScreen[0]).get(self.currentScreen[1])
        return func()

    def text_scrape(self):

        curScrInd = self.currentScreen[1]

        if curScrInd == 2:
            self.defaultLocation = self.locTxtBox.text()
            print("Default location set to {}".format(self.defaultLocation))
        elif curScrInd == 3:
            self.softwarePathList[0] = self.fileLocTxtBox.text()
            print("{} is located in {}".format(self.softwareList[curScrInd - 3],
                 self.softwarePathList[curScrInd - 3]))
        elif curScrInd == 4:
            self.softwarePathList[1] = self.fileLocTxtBox.text()
            print("{} is located in {}".format(self.softwareList[curScrInd - 3],
                 self.softwarePathList[curScrInd - 3]))
        elif curScrInd == 5:
            self.softwarePathList[2] = self.fileLocTxtBox.text()
            print("{} is located in {}".format(self.softwareList[curScrInd - 3],
                 self.softwarePathList[curScrInd - 3]))

    def choose_file(self):
        options = QFileDialog.Options()
        filePath = QFileDialog.getOpenFileName(self, "Choose Install File",
                   "", "All Files (*);;Exe Files (*.exe)", options=options)
        self.fileLocTxtBox.setText(filePath[0])

    @staticmethod
    def font_size(curWidget, size=10):

        font = curWidget.font()
        font.setPointSize(size)
        curWidget.setFont(font)
