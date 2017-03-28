from json_handler import JSONHandler
from action_factory import ActionFactory

class ActionScheduler():

    def __init__(self, file_name):

        file_locations = JSONHandler.dejsonify(file_name)
        action_dict = ActionFactory.create_actions(file_locations)
