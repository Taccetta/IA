from TP1_taccetta import BotPuzzle
import unittest
from parameterized import parameterized

class TestBot(unittest.TestCase):
    
    
    @parameterized.expand([([1, 2], [(0, 2), (2, 2), (1, 1)], 3, [[1, 2, 3], [4, 5, 0], [7, 8, 6]]),
                        ([1, 0], [(0, 0), (1, 1)], 2, [[1, 2], [0, 3]])])
    def test_check_moves(self, position, result, colrow, board):
        bot = BotPuzzle()
        bot.board = board
        bot.hole_position = position
        bot.column_and_row = colrow
        bot.check_moves()
        self.assertEqual(bot.possible_moves, result)


if __name__ == '__main__':
    unittest.main()