from Bili.Task import Task
from Bili.BilibliInfo import BilibliInfo


class BiliBaseTask(Task):
    def __init__(self, bili: BilibliInfo):
        self.bili = bili
        pass
