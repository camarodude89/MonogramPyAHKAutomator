from actions import AHKAction, URLInstallAction

class ActionFactory():

    @staticmethod
    def create_action(action_type, **kwargs):

        #action construction logic
        if action_type == "AHKAction":
            return AHKAction(kwargs["AHK Filename"], kwargs["Exe Path"])

        if action_type == "URLInstallAction":
            return URLInstallAction(kwargs["AHK Filename"], url=kwargs["URL"])
