import subprocess

class AHKAction(Action):

    def __init__(self, ahk_filename, executable_path):

        #The file name is originally a dict key with a space
        #The underscore is needed to match the ahk file name
        self.ahk_filename = ahk_filename.replace(" ", "_")
        self.ahk_filename += ".ahk"
        self.executable_path = executable_path

    def run(self):

        subprocess.run(self.ahk_filename + " " + self.executable_path,
                       shell=True)
