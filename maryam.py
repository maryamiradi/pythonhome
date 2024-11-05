#من امدم اینجا یک جدول ساحتم که شامل ستون و ردیف هستن و با استفاده از حلقه اینو تعیین کردم بعد امدم برای هر کدوم یه تابع ساختم تا در صورت برنده شدن بتونم شرط ها رو درست کنم الان باید برم سراغ برنده شدن و بعد پر کردن خونه ها توسط
# کامپیوتر وو یوزر و اگر بتونم در مرحله بعد 2 تا یوزر داشته باشم
    
import random


class User:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        
        
class Computer:
    def __init__(self, shape):
        self.shape = shape
        
    
class Table:
    def __init__(self, user, computer):
        self.l = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        self.user = user
        self.computer = computer
        
        
    def fill_user(self):
        while True:
            try:
                row = int(input("Enter your row (1-3): ")) - 1
                column = int(input("Enter your column (1-3): ")) - 1
                if self.l[row][column] == 0:
                    self.l[row][column] = self.user.shape
                    break
                else:
                    print('You can\'t fill this position.')
            except (ValueError, IndexError):
                print('Choose a valid position in range (1-3).')
       
       
                
    def fill_computer(self):
        choose = [(a, b) for a in range(3) for b in range(3) if self.l[a][b] == 0]
        if choose:
            row, column = random.choice(choose)
            self.l[row][column] = self.computer.shape
        
        
        
class Game:
    def __init__(self):
        self.table = None
        
        
    def show_table(self):
        for i in self.table.l:
            print(i)
         
            
    def check_winner(self):
        for i in range(3):
            if self.table.l[i][0] == self.table.l[i][1] == self.table.l[i][2] != 0:
                return f'{self.table.l[i][0]} is the winner!' 
                
            elif self.table.l[0][i] == self.table.l[1][i] == self.table.l[2][i] != 0:
                return f'{self.table.l[0][i]} is the winner!'

        if self.table.l[0][0] == self.table.l[1][1] == self.table.l[2][2] != 0:
            return f'{self.table.l[0][0]} is the winner!'
        elif self.table.l[0][2] == self.table.l[1][1] == self.table.l[2][0] != 0:
            return f'{self.table.l[1][1]} is the winner!'

        return None
        
            
    def check_fill(self):
        for row in self.table.l:
            for cell in row:
                if cell == 0:
                    return None
        return 'Game is over and no one won.'
       
            
    def start_game(self):
        name = input('Enter your name: ')
        shape = input('Enter your shape (X or O): ').upper()
        
        if shape not in ['X', 'O']:
            print("Please choose either 'X' or 'O'.")
            return
            
        vshape = 'O' if shape == 'X' else 'X'
        computer = Computer(vshape)            
        user = User(name, shape)
        self.table = Table(user, computer)
        
        while True:
            self.show_table()
            git
            
            
            self.table.fill_user()
            winner = self.check_winner()
            if winner:
                self.show_table()
                print(winner)
                break
            
            if self.check_fill():
                self.show_table()
                print(self.check_fill())
                break

            self.table.fill_computer()
            winner = self.check_winner()
            if winner:
                self.show_table()
                print(winner)
                break

            if self.check_fill():
                self.show_table()
                print(self.check_fill())
                break

if __name__ == "__main__":
    game = Game()
    game.start_game()
