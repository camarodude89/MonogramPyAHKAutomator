from actions import AHKAction

class ActionFactory():

    @staticmethod
    def create_action(action_type, **kwargs):

        #action construction logic
        if action_type == "AHKAction":
            return AHKAction(action_type, kwargs["AHK Filename"],
                             kwargs["Exe Path"])
