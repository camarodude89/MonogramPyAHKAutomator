import subprocess

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

    DOWNLOAD_LOC = "\"C:\\Users\\Administrator\\Downloads\\"

    def __init__(self, ahk_filename, executable_path, url):
        super.__init__(ahk_filename, executable_path)
        self.url = url
