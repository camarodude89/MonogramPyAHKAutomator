import abc

class Action(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self):
        #executes the action

class AHKAction(Action):
    pass
