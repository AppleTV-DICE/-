'''
import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, rows, cols, mines):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = set()
        self.buttons = []
        self.squares = [[0 for _ in range(cols)] for _ in range(rows)]

        for _ in range(mines):
            while True:
                row = random.randint(0, rows - 1)
                col = random.randint(0, cols - 1)
                if (row, col) not in self.mines:
                    self.mines.add((row, col))
                    break

        for row in range(rows):
            button_row = []
            for col in range(cols):
                button = tk.Button(
                    master,
                    width=2,
                    height=1,
                    relief=tk.RAISED,  # 변경된 부분
                    command=lambda r=row, c=col: self.click(r, c),
                )
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def click(self, row, col):
        if (row, col) in self.mines:
            self.buttons[row][col].config(text="*", state=tk.DISABLED)
            self.show_all_mines()
        else:
            self.reveal(row, col)

    def count_adjacent_mines(self, row, col):
        count = 0
        for r in range(max(0, row - 1), min(self.rows, row + 2)):
            for c in range(max(0, col - 1), min(self.cols, col + 2)):
                if (r, c) in self.mines:
                    count += 1
        return count

    def reveal(self, row, col):
        if self.squares[row][col] == 1:
            return
        mine_count = self.count_adjacent_mines(row, col)
        self.squares[row][col] = 1
        self.buttons[row][col].config(
            text=str(mine_count) if mine_count > 0 else "",
            relief=tk.SUNKEN  # 변경된 부분
        )
        if mine_count == 0:
            for r in range(max(0, row - 1), min(self.rows, row + 2)):
                for c in range(max(0, col - 1), min(self.cols, col + 2)):
                    self.reveal(r, c)

    def show_all_mines(self):
        for row, col in self.mines:
            self.buttons[row][col].config(text="*", state=tk.DISABLED)

def main():
    root = tk.Tk()
    root.title("Minesweeper")
    rows = 14
    cols = 20
    mines = 30
    Minesweeper(root, rows, cols, mines)
    root.mainloop()

if __name__ == "__main__":
    main()
'''
import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, rows, cols, mines):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.total_mines = mines
        self.mines = set()
        self.buttons = []
        self.squares = [[0 for _ in range(cols)] for _ in range(rows)]
        self.game_over = False

        for _ in range(mines):
            while True:
                row = random.randint(0, rows - 1)
                col = random.randint(0, cols - 1)
                if (row, col) not in self.mines:
                    self.mines.add((row, col))
                    break

        tk.Label(master, text=f"Total Mines: {self.total_mines}").grid(row=rows, columnspan=cols)

        for row in range(rows):
            button_row = []
            for col in range(cols):
                button = tk.Button(
                    master,
                    width=2,
                    height=1,
                    relief=tk.RAISED,
                )
                button.grid(row=row, column=col)
                button.bind('<Button-1>', lambda event, r=row, c=col: self.left_click(event, r, c))
                button.bind('<Button-3>', lambda event, r=row, c=col: self.right_click(event, r, c))
                button_row.append(button)
            self.buttons.append(button_row)

    def left_click(self, event, row, col):
        if self.game_over:
            self.restart_game()
        elif (row, col) in self.mines:
            self.buttons[row][col].config(text="*", state=tk.DISABLED)
            self.show_all_mines()
            self.game_over = True
        else:
            self.reveal(row, col)

    def right_click(self, event, row, col):
        if self.game_over:
            return
        if self.buttons[row][col]['text'] == '':
            self.buttons[row][col].config(text="X")
        elif self.buttons[row][col]['text'] == 'X':
            self.buttons[row][col].config(text='')

    def count_adjacent_mines(self, row, col):
        count = 0
        for r in range(max(0, row - 1), min(self.rows, row + 2)):
            for c in range(max(0, col - 1), min(self.cols, col + 2)):
                if (r, c) in self.mines:
                    count += 1
        return count

    def reveal(self, row, col):
        if self.squares[row][col] == 1:
            return
        mine_count = self.count_adjacent_mines(row, col)
        self.squares[row][col] = 1
        self.buttons[row][col].config(
            text=str(mine_count) if mine_count > 0 else "",
            relief=tk.SUNKEN
        )
        if mine_count == 0:
            for r in range(max(0, row - 1), min(self.rows, row + 2)):
                for c in range(max(0, col - 1), min(self.cols, col + 2)):
                    self.reveal(r, c)

    def show_all_mines(self):
        for row, col in self.mines:
            self.buttons[row][col].config(text="*", state=tk.DISABLED)


    def restart_game(self):
        self.master.destroy()
        root = tk.Tk()
        root.title("Minesweeper")
        Minesweeper(root, self.rows, self.cols, self.total_mines)
        root.mainloop()

def main():
    root = tk.Tk()
    root.title("지뢰찾기")
    rows = 1
    cols = 50
    mines = 5
    Minesweeper(root, rows, cols, mines)
    root.mainloop()

if __name__ == "__main__":
    main()