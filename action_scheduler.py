from json_handler import JSONHandler

class ActionScheduler():

    def __init__(self, file_name):
        self.file_locations = JSONHandler.dejsonify(file_name)
