import unittest
from io import StringIO
from unittest.mock import patch
from maryam import Game, User, Computer, Table



class TestTicTacToe(unittest.TestCase):
    
    def setUp(self):
        self.user = User("TestUser", "X")
        self.computer = Computer("O")
        self.table = Table(self.user, self.computer)
        self.game = Game()
        self.game.table = self.table

    def test_initial_board(self):
        expected_board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(self.table.l, expected_board)

    @patch('builtins.input', side_effect=['1', '1'])  # Mock input to simulate user placing 'X' at (1,1)
    def test_user_move(self, mock_input):
        self.table.fill_user()
        self.assertEqual(self.table.l[0][0], 'X')

    def test_computer_move(self):
        self.table.fill_computer()
        computer_moves = sum([row.count('O') for row in self.table.l])
        self.assertEqual(computer_moves, 1)

    def test_winner_row(self):
        self.table.l[0] = ['X', 'X', 'X']
        winner = self.game.check_winner()
        self.assertEqual(winner, 'X is the winner!')

    def test_winner_column(self):
        self.table.l[0][0] = self.table.l[1][0] = self.table.l[2][0] = 'O'
        winner = self.game.check_winner()
        self.assertEqual(winner, 'O is the winner!')

    def test_winner_diagonal(self):
        self.table.l[0][0] = self.table.l[1][1] = self.table.l[2][2] = 'X'
        winner = self.game.check_winner()
        self.assertEqual(winner, 'X is the winner!')

    def test_no_winner(self):
        self.table.l[0] = ['X', 'O', 0]
        self.table.l[1] = ['O', 'X', 0]
        self.table.l[2] = [0, 0, 'X']
        winner = self.game.check_winner()
        self.assertIsNone(winner)

    def test_game_over(self):
        self.table.l = [
            ['X', 'O', 'X'],
            ['X', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        game_status = self.game.check_fill()
        self.assertEqual(game_status, 'Game is over and no one won.')

    @patch('builtins.input', side_effect=['1', 'X'])  # Mock input to simulate user starting game
    def test_game_start(self, mock_input):
        self.game.start_game()
        self.assertEqual(self.table.l[0][0], 'X')

if __name__ == '__main__':
    unittest.main()
