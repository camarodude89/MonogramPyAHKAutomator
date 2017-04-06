from json_handler import JSONHandler
from action_factory import ActionFactory

class ActionScheduler():

    _URLFILENAME = 'URLs.json'

    def __init__(self, filename, phys_location):

        urls = JSONHandler.dejsonify(self._URLFILENAME)
        file_locations = JSONHandler.dejsonify(filename)

        #action list creation should happen here
        self.action_list = list()

        #add URLInstallActions to action_list
        for name,url in urls.items():

            kwargs = {"AHK Filename":name, "URL":url}
            self.action_list.append(ActionFactory.create_action(
                action_type="URLInstallAction", **kwargs))

        #add AHKActions to action_list
        for name,path in file_locations[phys_location].items():

            kwargs = {"AHK Filename":name, "Exe Path":path}
            self.action_list.append(ActionFactory.create_action(action_type="AHKAction",
                               **kwargs))
    def run(self):

        for action in self.action_list:
            action.run()
