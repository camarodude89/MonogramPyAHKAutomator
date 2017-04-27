from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, QLabel,
QWidget, QPushButton, QLayout, QLineEdit, QFileDialog)
from json_handler import JSONHandler
import os

class GUIInterface(QWidget):

    FILENAME = "locationPaths.json"

    WIZ_INITIAL_TXT = """<div style=\"font-family:Segoe UI;\">
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

    LOC_CHOOSE_TXT = """<div align=\"left\" style=\"font-family:Segoe UI;\">
    <h3>MonogramPyAHKAutomator Setup Wizard</h3>
    <p style=\"font-size:10pt;\">Enter the physical location of the servers from
    which you will be installing software. (Ex: Memphis for MEM-APP,
    Martinsville for MMSMV-SVR1, etc.)</p>"""

    LOC_TXT_BOX_LBL_TXT = """<div align=\"left\" style=\"font-family:Segoe UI;
    font-size:10pt;\">Default Location:</div>"""

    FILE_CHOOSER_TXT_1 = """<div align=\"left\" style=\"font-family:Segoe UI;\">
    <h3>MonogramPyAHKAutomator Setup Wizard</h3>
    <p style=\"font-size:10pt;\">Enter the path to the setup file for <b>"""

    FILE_CHOOSER_TXT_2 = "</b>.</div>"

    SETUP_COMPLETE_TXT = """<div align=\"left\" style=\"font-family:Segoe UI;\">
    <h3>MonogramPyAHKAutomator Setup Wizard</h3>
    <p style=\"font-size:10pt;\">Setup has been completed. Select the Finish
    button to exit.</p></div>"""


    def __init__(self):

        super().__init__()
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('MonogramPyAHKAutomator')
        self.setWindowIcon(QIcon('web.png'))

        self.gui_switcher = {
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

        self.software_list = ["Adobe Reader", "CutePDF",
        "ShoreTel Communicator"]

        self.software_path_list = list()

        if os.path.isfile('locationPaths.json'):

            self.current_screen = ["Automator", 0]
            self.init_automator_ui()
        else:

            self.current_screen = ["Wizard", 0]
            self.first_run = True
            self.wiz_layout = QVBoxLayout()
            self.wiz_btn_layout = QHBoxLayout()
            self.init_wizard_ui()

    def clear_layout(self, layout=None):

        layout = layout or self.layout()
        for i in reversed(range(layout.count())):
            layout_item = layout.itemAt(i)
            if issubclass(layout_item.__class__, QLayout):
                self.clear_layout(layout=layout_item)
                #removes the sublayout from the main layout
                self.layout().removeItem(layout_item)
                continue
            widget_to_remove = layout_item.widget()
            layout.removeWidget(widget_to_remove)
            #remove widget from the GUI
            widget_to_remove.setParent(None)

    def init_wizard_ui(self):

        #Allows moving back to this screen without issue
        if not self.first_run:
            self.clear_layout()

        intro = QLabel()
        intro.setText(self.WIZ_INITIAL_TXT)
        intro.setAlignment(Qt.AlignTop)
        intro.setWordWrap(True)

        self.wiz_layout.addWidget(intro)

        continue_btn = QPushButton("Continue", self)
        GUIInterface.font_size(continue_btn)
        continue_btn.clicked.connect(self.next_screen)
        exit_btn = QPushButton("Exit", self)
        GUIInterface.font_size(exit_btn)
        exit_btn.clicked.connect(self.close)

        self.wiz_btn_layout.addWidget(continue_btn)
        self.wiz_btn_layout.addWidget(exit_btn)
        self.wiz_layout.addLayout(self.wiz_btn_layout)

        self.setLayout(self.wiz_layout)

        self.show()

        self.first_run = False

    def location_chooser_ui(self):

        self.clear_layout()

        desc = QLabel()
        desc.setText(self.LOC_CHOOSE_TXT)
        desc.setAlignment(Qt.AlignTop)
        desc.setWordWrap(True)

        loc_txt_and_lbl_box_layout = QHBoxLayout()

        loc_txt_box_lbl = QLabel()
        loc_txt_box_lbl.setText(self.LOC_TXT_BOX_LBL_TXT)
        loc_txt_box_lbl.setAlignment(Qt.AlignCenter)

        self.loc_txt_box = QLineEdit()
        GUIInterface.font_size(self.loc_txt_box)

        loc_txt_and_lbl_box_layout.addWidget(loc_txt_box_lbl)
        loc_txt_and_lbl_box_layout.addWidget(self.loc_txt_box)
        loc_txt_and_lbl_box_layout.setAlignment(Qt.AlignTop)

        back_btn = QPushButton("< Back", self)
        GUIInterface.font_size(back_btn)
        back_btn.clicked.connect(self.prev_screen)
        next_btn = QPushButton("Next >", self)
        GUIInterface.font_size(next_btn)
        next_btn.clicked.connect(self.next_screen)

        self.wiz_btn_layout.addWidget(back_btn)
        self.wiz_btn_layout.addWidget(next_btn)

        self.wiz_layout.addWidget(desc)
        self.wiz_layout.addLayout(loc_txt_and_lbl_box_layout)
        self.wiz_layout.addLayout(self.wiz_btn_layout)

        self.setLayout(self.wiz_layout)

        self.show()

    def file_chooser_ui(self):

        self.text_scrape()
        self.clear_layout()

        desc = QLabel()
        desc.setText(self.FILE_CHOOSER_TXT_1 +
                    self.software_list[self.current_screen[1] - 2] +
                    self.FILE_CHOOSER_TXT_2)
        desc.setAlignment(Qt.AlignTop)
        desc.setWordWrap(True)

        file_chooser_hbox_layout = QHBoxLayout()

        self.fileloc_txt_box = QLineEdit()
        GUIInterface.font_size(self.fileloc_txt_box)

        browse_btn = QPushButton("Browse...", self)
        GUIInterface.font_size(browse_btn)
        browse_btn.clicked.connect(self.choose_file)

        file_chooser_hbox_layout.addWidget(self.fileloc_txt_box)
        file_chooser_hbox_layout.addWidget(browse_btn)
        file_chooser_hbox_layout.setAlignment(Qt.AlignTop)

        back_btn = QPushButton("< Back", self)
        GUIInterface.font_size(back_btn)
        back_btn.clicked.connect(self.prev_screen)
        next_btn = QPushButton("Next >", self)
        GUIInterface.font_size(next_btn)
        next_btn.clicked.connect(self.next_screen)

        self.wiz_btn_layout.addWidget(back_btn)
        self.wiz_btn_layout.addWidget(next_btn)

        self.wiz_layout.addWidget(desc)
        self.wiz_layout.addLayout(file_chooser_hbox_layout)
        self.wiz_layout.addLayout(self.wiz_btn_layout)

        self.setLayout(self.wiz_layout)

        self.show()

    def setup_complete_ui(self):

        self.text_scrape()
        JSONHandler.jsonify(self.FILENAME, self.default_location,
                            self.software_list, self.software_path_list)
        self.clear_layout()

        desc = QLabel()
        desc.setText(self.SETUP_COMPLETE_TXT)
        desc.setAlignment(Qt.AlignTop)
        desc.setWordWrap(True)

        finish_btn = QPushButton("Finish", self)
        GUIInterface.font_size(finish_btn)
        #finish_btn.setFixedWidth(100)
        finish_btn.clicked.connect(self.close)

        self.wiz_layout.addWidget(desc)
        self.wiz_layout.addWidget(finish_btn)

        self.setLayout(self.wiz_layout)

        self.show()

    def init_automator_ui(self):

        stuff = QLabel()
        stuff.setText("Things and stuff go here!!!")
        stuff.setAlignment(Qt.AlignTop)
        stuff.setWordWrap(True)

        self.auto_layout = QVBoxLayout()

        self.auto_layout.addWidget(stuff)

        self.setLayout(self.auto_layout)

        self.show()

    def next_screen(self):

        self.current_screen[1] += 1
        func = self.gui_switcher.get(self.current_screen[0]).get(self.current_screen[1])
        return func()

    def prev_screen(self):

        self.current_screen[1] -= 1
        func = self.gui_switcher.get(self.current_screen[0]).get(self.current_screen[1])
        return func()

    def text_scrape(self):

        cur_scr_ind = self.current_screen[1]

        if cur_scr_ind == 2:
            self.default_location = self.loc_txt_box.text()
            print("Default location set to {}".format(self.default_location))
        elif cur_scr_ind > 2 and cur_scr_ind < 6:
            modded_path = self.fileloc_txt_box.text()
            modded_path = "\"" + modded_path.replace("/", "\\") + "\""
            self.software_path_list.append(modded_path)
            print("{} is located in {}".format(self.software_list[cur_scr_ind - 3],
                 self.software_path_list[cur_scr_ind - 3]))

    def choose_file(self):

        options = QFileDialog.Options()
        file_path = QFileDialog.getOpenFileName(self, "Choose Install File",
                                "", "All Files (*);;Exe Files (*.exe)", options=options)
        self.fileloc_txt_box.setText(file_path[0])

    @staticmethod
    def font_size(cur_widget, size=10):

        font = cur_widget.font()
        font.setPointSize(size)
        cur_widget.setFont(font)
