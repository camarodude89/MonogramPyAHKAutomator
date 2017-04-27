import subprocess
import requests
import shutil

class AHKAction():

    def __init__(self, ahk_filename, executable_path):

        #The file name is originally a dict key with a space
        #The space is removed to match the ahk file name
        self.parent_folder = ahk_filename.replace(" ", "_")
        self.ahk_filename = ahk_filename.replace(" ", "")
        self.ahk_filename = self.parent_folder + "\\" + self.ahk_filename + "Automator.ahk"
        self.executable_path = executable_path

    def run(self):

        subprocess.run(self.ahk_filename + " " + self.executable_path,
                       shell=True)

class URLInstallAction(AHKAction):

    BAT_EXE_LOC = "\"C:\\Users\\Administrator\\Downloads\\"
    DOWNLOAD_LOC = "C:/User/Administrator/Downloads/"

    def __init__(self, ahk_filename, url, executable_path=None):

        self.down_file_name = ahk_filename.replace(" ", "") + ".exe"
        self.url = url
        if executable_path == None:
            executable_path = self.BAT_EXE_LOC + self.down_file_name + "\""
        super.__init__(ahk_filename, executable_path)

    def download_setup_file(self):
        pass

    def run(self):

        self.download_setup_file()
        super.run()
