from json_handler import JSONHandler
from action_factory import ActionFactory

class ActionScheduler():

    def __init__(self, filename, phys_location):

        file_locations = JSONHandler.dejsonify(filename)

        #action list creation should happen here
        self.action_list = list()

        #add AHKActions to action_list
        for name,path in file_locations[phys_location].items():

            kwargs = {"AHK Filename":name, "Exe Path":path}
            self.action_list.append(ActionFactory.create_action(action_type="AHKAction",
                               **kwargs))
