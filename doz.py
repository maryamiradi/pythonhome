import random
import tkinter as tk
from tkinter import messagebox, simpledialog

class User:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

class Computer:
    def __init__(self, shape):
        self.shape = shape

class Table:
    def __init__(self, user, computer):
        self.l = [[0, 0, 0] for _ in range(3)]
        self.user = user
        self.computer = computer

    def fill_user(self, row, column):
        if self.l[row][column] == 0:
            self.l[row][column] = self.user.shape
            return True
        return False

    def fill_computer(self):
        choose = [(a, b) for a in range(3) for b in range(3) if self.l[a][b] == 0]
        if choose:
            row, column = random.choice(choose)
            self.l[row][column] = self.computer.shape

class Game:
    def __init__(self, master):
        self.master = master
        self.table = None
        self.buttons = [[None, None, None] for _ in range(3)]
        self.start_game()

    def start_game(self):
        name = simpledialog.askstring("Input", "Enter your name:")
        shape = self.choose_shape()

        if shape is None:
            return

        vshape = 'O' if shape == 'X' else 'X'
        computer = Computer(vshape)
        user = User(name, shape)
        self.table = Table(user, computer)

        self.create_buttons()

    def choose_shape(self):
        shape_window = tk.Toplevel(self.master)
        shape_window.title("Choose Your Shape")
        tk.Label(shape_window, text="Choose your shape:", font='Arial 16').pack()

        x_button = tk.Button(shape_window, text='X', font='Arial 30',bg='#F3CCF3', command=lambda: self.set_shape(shape_window, 'X'))
        o_button = tk.Button(shape_window, text='O', font='Arial 30',bg='#F3CCF3', command=lambda: self.set_shape(shape_window, 'O'))

        x_button.pack(side='left', padx=30 , pady=30)
        o_button.pack(side='right', padx=30 , pady=30)

        shape_window.wait_window(shape_window)  
        return self.selected_shape


    def set_shape(self, window, shape):
        self.selected_shape = shape
        window.destroy()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text='', font='Arial 30', width=5, height=2,
                                                command=lambda row=i, col=j: self.user_move(row, col),
                                                bg='black', fg='red')
                self.buttons[i][j].grid(row=i, column=j)

    def user_move(self, row, column):
        if self.table.fill_user(row, column):
            self.update_buttons()
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", winner)
                self.highlight_winner(winner)
                self.ask_restart()
            else:
                self.master.after(1000, self.computer_move)

    def computer_move(self):
        self.table.fill_computer()
        self.update_buttons()
        winner = self.check_winner()
        if winner:
            messagebox.showinfo("Game Over", winner)
            self.highlight_winner(winner)
            self.ask_restart()

    def update_buttons(self):
        for i in range(3):
            for j in range(3):
                if self.table.l[i][j] != 0:
                    self.buttons[i][j].config(text=self.table.l[i][j], state='disabled', bg='black')
                    if self.table.l[i][j] == 'X':
                        self.buttons[i][j].config(fg='red', font='Arial 30 bold')
                    else:
                        self.buttons[i][j].config(fg='red', font='Arial 30 bold')


    def highlight_winner(self, winner):
        for i in range(3):
            for j in range(3):
                if self.table.l[i][j] != 0 and self.table.l[i][j] == winner[0]: 
                    self.buttons[i][j].config(bg='#F3CCF3')


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

        if all(cell != 0 for row in self.table.l for cell in row):
            return 'Game is over and no one won.'
        return None

    def ask_restart(self):
        response = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if response:
            self.reset_game()
        else:
            self.master.destroy()

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state='normal', bg='black', fg='#F3CCF3', font='Arial 30')
        self.table = Table(self.table.user, self.table.computer)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic Tac Toe")
    game = Game(root)
    root.mainloop()
