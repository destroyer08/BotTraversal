import unittest
from BotTraversal import Bot

class TestBot(unittest.TestCase):
    def test_testcase0(self):
        grid = []
        grid.append(["46B", "E59", "EA", "C1F", "45E", "63"])
        grid.append(["899", "FFF", "926", "7AD", "C4E", "FFF"])
        grid.append(["E2E", "323", "6D2", "976", "83F", "C96"])
        grid.append(["9E9", "A8B", "9C1", "461", "F74", "D05"])
        grid.append(["EDD", "E94", "5F4", "D1D", "D03", "DE3"])
        grid.append(["89", "925", "CF9", "CA0", "F18", "4D2"])
        self.assertEqual(Bot(grid).traverse(), "5a72", "Testcase 0 Failed")

    def test_testcase1(self):
        grid = []
        grid.append(["0", "0", "0"])
        grid.append(["0", "0", "0"])
        self.assertEqual(Bot(grid).traverse(), "0", "Testcase 1 Failed")

    def test_testcase2(self):
        grid = []
        grid.append(["D1D", "D03"])
        grid.append(["461", "F74"])
        grid.append(["DE2", "D05"])
        self.assertEqual(Bot(grid).traverse(), "2c65", "Testcase 2 Failed")


if __name__ == '__main__':
    unittest.main()