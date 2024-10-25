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
        
    def fill_user(self, column, row):
        while True:
            try:
                row = int(input("enter your row: ")) - 1
                column = int(input("enter your column: ")) - 1
                if self.l[row][column] == 0:
                    self.l[row][column] = self.user.shape
                    break
                else:
                    print('you cant fill it home')
            except (ValueError, IndexError):
                print('choose in range(1,3)')
                
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
                print('you are winner', self.table.l[i][0]) 
                
            elif self.table.l[0][i] == self.table.l[1][i] == self.table.l[2][i] != 0:
                print('you are winner', self.table.l[0][i])
            
        if self.table.l[0][0] == self.table.l[1][1] == self.table.l[2][2] != 0:
            print('you are winner', self.table.l[0][0])
        elif self.table.l[0][2] == self.table.l[1][1] == self.table.l[2][0] != 0:
            print('you are winner', self.table.l[1][1])
        
        return None            
    
    def check_fill(self):
         for row in self.table.l:
             for cell in row:
                if cell == 0:
                    return None 
   
            
    def start_game(self):
        name = input('enter your name: ')
        shape = input('enter your shape: ')
        if shape == 'x':
            vshape = '0'
        else:
            vshape = 'x'
        computer = Computer(vshape)            
        user = User(name, shape)
        self.table = Table(user, computer)
        
        while True:
            self.show_table()
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
        
    

 
 
