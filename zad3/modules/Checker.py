from modules.Env import Env


class Checker:
    def __init__(self) -> None:
        self._env = Env()
        self._was_played = False

    @property
    def was_played(self):
        return self._was_played

    def wavWasPlayed(self) -> None:
        self._was_played = True

    def resetWav(self) -> None:
        self._was_played = False

    def reminder(self) -> None:
        current_hour = self._env.getTime().hour
        if current_hour >= 17:
            self._env.playWavFile("some_file")
            self.wavWasPlayed()
