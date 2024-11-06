import unittest
from unittest.mock import MagicMock, patch
import random
from tkinter import Tk, simpledialog, messagebox
from doz import User, Table, Game, Computer

class UserTest(unittest.TestCase):
    
    def setUp(self):
        self.newuser = User('maryam', 'o')
    
    def test_user_name_shape(self):
        self.assertEqual(self.newuser.name, 'maryam')
        self.assertEqual(self.newuser.shape, 'o')
    
class ComputerTest(unittest.TestCase):

    def setUp(self):
        self.computer = Computer('X') 
        
    def test_computer_shape(self):
        self.assertEqual(self.computer.shape, 'X')
        
class TableTest(unittest.TestCase):
    def setUp(self):
        self.user=User('maryam','o')
        self.computer=Computer('x')
        self.table=Table(self.user,self.computer)
        
    def test_fiill_user(self):
        self.assertEqual(self.table.l[0][0],0)
        self.assertTrue(self.table.fill_user(0,0))
        self.assertEqual(self.table.l[0][0],'o')
        self.assertFalse(self.table.fill_user(0,0))
        
    def tset_fill_computer(self):
        self.assertEqual(self.table.l[1][1],0)
        self.assertTrue(self.table.fill_computer(1,1))
        self.assertEqual(self.table.l[1],[1],'x')
        self.assertFalse(self.table.fill_computer(1,1))
        
class GameStartTest(unittest.TestCase):
    
    @patch('tkinter.simpledialog.askstring')
    @patch('doz.Game.choose_shape')
    def test_start_game(self, mock_choose_shape, mock_askstring):
        mock_askstring.return_value = "Player1"  
        mock_choose_shape.return_value = "X" 
        root = Tk()
        game = Game(root)
        self.assertEqual(game.table.user.name, "Player1")
        self.assertEqual(game.table.user.shape, "X")
        self.assertEqual(game.table.computer.shape, "O")
        
class ChooseShapeTest(unittest.TestCase):
    
    @patch('tkinter.simpledialog.askstring', return_value="Player1")  
    @patch('doz.Game.choose_shape', return_value="X")  
    @patch('tkinter.messagebox.showinfo')  
    def test_choose_shape(self, mock_showinfo, mock_choose_shape, mock_askstring):
       
        root = Tk()
        game = Game(root)

        self.assertEqual(game.table.user.shape, "X")
        self.assertEqual(game.table.computer.shape, "O")  
        

        
                    
class UserMoveTest(unittest.TestCase):
    
    def test_user_move(self):
        user = User("Player1", "X")
        computer = Computer("O")
        table = Table(user, computer)
        table.fill_user(0, 0)  
        self.assertEqual(table.l[0][0], "X")


class ComputerMoveTest(unittest.TestCase):
    
    def test_computer_move(self):
        user = User("Player1", "X")
        computer = Computer("O")
        table = Table(user, computer)
        table.fill_computer()

        self.assertTrue(any(cell == 'O' for row in table.l for cell in row), "Computer didn't make a move.")


                
class UpdateButtonsTest(unittest.TestCase):

    @patch('tkinter.simpledialog.askstring', return_value="Player1")  
    @patch('doz.Game.choose_shape', return_value='X')  
    @patch('tkinter.messagebox.showinfo')  
    def test_update_buttons(self, mock_showinfo, mock_choose_shape, mock_askstring):
        root = Tk()
        game = Game(root)

        
        game.table.fill_user(0, 0)  
        game.update_buttons()  

        self.assertEqual(game.buttons[0][0].cget("text"), "X")
        self.assertEqual(game.buttons[0][0].cget("state"), "disabled")

        
        game.table.fill_computer()  
        game.update_buttons()

        
        self.assertTrue(any(game.buttons[i][j].cget("text") == 'O' for i in range(3) for j in range(3)))

class CheckWinnerTest(unittest.TestCase):
    
    @patch('tkinter.simpledialog.askstring', return_value="Player1")  
    @patch('doz.Game.choose_shape', return_value='X')  
    @patch('tkinter.messagebox.showinfo') 
    def test_check_winner_radif(self, mock_showinfo, mock_choose_shape, mock_askstring):
        root = Tk()
        game = Game(root) 

        game.table.l[0][0] = "X"
        game.table.l[0][1] = "X"
        game.table.l[0][2] = "X"

        winner = game.check_winner()  
        self.assertEqual(winner, 'X is the winner!')
        
        
        
class HighlightWinnerTest(unittest.TestCase):

    @patch('tkinter.simpledialog.askstring', return_value="Player1")  
    @patch('doz.Game.choose_shape', return_value='X') 
    @patch('tkinter.messagebox.showinfo')  
    def test_highlight_winner(self, mock_showinfo, mock_choose_shape, mock_askstring):
        root = Tk()
        game = Game(root)

        game.table.l[0][0] = "X"
        game.table.l[0][1] = "X"
        game.table.l[0][2] = "X"

        winner = game.check_winner()
        self.assertEqual(winner, "X is the winner!")

        game.highlight_winner("X")
        self.assertEqual(game.buttons[0][0].cget("bg"), "#F3CCF3")
        self.assertEqual(game.buttons[0][1].cget("bg"), "#F3CCF3")
        self.assertEqual(game.buttons[0][2].cget("bg"), "#F3CCF3")


class ResetGameTest(unittest.TestCase):

    @patch('tkinter.simpledialog.askstring', return_value="Player1")  
    @patch('doz.Game.choose_shape', return_value='X')  
    @patch('tkinter.messagebox.showinfo')  
    def test_reset_game(self, mock_showinfo, mock_choose_shape, mock_askstring):
        root = Tk()
        game = Game(root)

        game.table.l[0][0] = "X"
        game.table.l[0][1] = "O"
        game.update_buttons()
        self.assertEqual(game.buttons[0][0].cget("text"), "X")
        self.assertEqual(game.buttons[0][1].cget("text"), "O")
        game.reset_game()

        for i in range(3):
            for j in range(3):
                self.assertEqual(game.buttons[i][j].cget("text"), '')
                self.assertEqual(game.buttons[i][j].cget("state"), "normal")
                self.assertEqual(game.buttons[i][j].cget("bg"), "black")

if __name__ == "__main__":
    unittest.main()



# class CreateButtonsTest(unittest.TestCase):
    
#     def test_create_buttons(self):
        
#         root = Tk()
#         game = Game(root)
#         game.create_buttons()
#         self.assertEqual(len(game.buttons), 3) 
#         self.assertEqual(len(game.buttons[0]), 3)  
        
       
#         self.assertEqual(game.buttons[0][0].cget("text"), '') 
#         self.assertEqual(game.buttons[1][1].cget("text"), '') 
#         self.assertEqual(game.buttons[2][2].cget("text"), '')  
    


    

        
    
    
    
        
        
        
        
        
        
