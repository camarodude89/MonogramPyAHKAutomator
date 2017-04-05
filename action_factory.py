from actions import AHKAction

class ActionFactory():

    @staticmethod
    def create_action(action_type, **kwargs):

        #action construction logic
        if action_type == "AHKAction":
            return AHKAction(kwargs["AHK Filename"], kwargs["Exe Path"])
