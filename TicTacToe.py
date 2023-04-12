import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", width=10, height=5,
                                   command=lambda i=i, j=j: self.button_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.label = tk.Label(self.window, text="Player X's turn", font=("Arial", 16))
        self.label.grid(row=3, column=0, columnspan=3)

    def button_click(self, i, j):
        if self.board[i][j] == "":
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)

            winner = self.check_winner()
            if winner is not None:
                self.label.config(text=f"Player {winner} wins!")
                for i in range(3):
                    for j in range(3):
                        self.buttons[i][j].config(state=tk.DISABLED)
            elif self.check_tie():
                self.label.config(text="It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]
        return None

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    game = TicTacToe()
    game.run()
