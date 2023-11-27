import unittest
import src.user


user = src.user.User(1234567890, "Test", "User", "Test User")


class TestUser(unittest.TestCase):
    def test_answer_start(self):
        self.assertEqual(user.message_process("/start"), "There should be a welcome message here")

    def test_answer_help(self):
        self.assertEqual(user.message_process("/help"), "There should be a text explaining how to use the bot")

    def test_answer_unknown(self):
        self.assertEqual(user.message_process("jkhgfjgfwe"), "There should be a text explaining how to use the bot")
