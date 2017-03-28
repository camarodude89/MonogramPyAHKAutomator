from json_handler import JSONHandler
from action_factory import ActionFactory

class ActionScheduler():

    def __init__(self, filename, phys_location):

        file_locations = JSONHandler.dejsonify(filename)
        #action list creation should happen here
        action_list = []

        #add AHKActions to action_list
        for name,path in file_locations[phys_location]:

            action_list.append(ActionFactory.create_action("AHKAction",
                               "AHK Filename":name, "Exe Path":path))
