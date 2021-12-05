from unittest import TestCase
from assertpy import assert_that
from unittest.mock import *
from datetime import datetime
from modules.Checker import Checker
from modules.Env import Env


class TestChecker(TestCase):
    @patch.object(Env, 'getTime')
    def test_reminder_before_17(self, mock_method) -> None:
        mock_method.return_value = datetime(2021, 5, 12, 12, 30, 0, 0)
        checker = Checker()
        checker.resetWav()
        checker.reminder()
        assert_that(checker.was_played).is_false()

    @patch.object(Env, 'getTime')
    def test_reminder_after_17(self, mock_method) -> None:
        mock_method.return_value = datetime(2021, 5, 12, 18, 30, 0, 0)
        checker = Checker()
        checker.resetWav()
        checker.reminder()
        assert_that(checker.was_played).is_true()
