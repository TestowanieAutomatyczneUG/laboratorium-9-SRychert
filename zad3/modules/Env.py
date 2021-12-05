from datetime import datetime


class Env:
    def getTime(self):
        return datetime.now()

    def playWavFile(self, file) -> None:
        pass