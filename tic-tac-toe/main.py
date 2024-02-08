import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
import os
import time


CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CELL_SIZE = 100

EMPTY_CELL = 0
CROSS_CELL = 1
CIRCLE_CELL = 2
TOTAL_CELLS = 9

current_path = os.path.abspath(__file__)

class MyApp:
    def __init__(self, app) -> None:
        self.app = app
        self.app.title("Tic-Tac-Toe")
        self.app["padx"] = 20
        self.app["pady"] = 20

        self.game_label = tkinter.Label(self.app, text="Let's play TIC-TAC-TOE")
        self.game_label.grid(row=0, column=1, padx=10, pady=10, columnspan=3)

        self.game_board_canvas = tkinter.Canvas(self.app, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.game_board_canvas.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

        self.row_selected_var = tkinter.StringVar()
        self.row_selected_combobox = ttk.Combobox(self.app, textvariable=self.row_selected_var)
        self.row_selected_combobox["values"] = ("Row 1", "Row 2", "Row 3")
        self.row_selected_combobox.set("Row 1")
        self.row_selected_combobox.grid(row=2, column=1, padx=10, pady=10)

        self.column_selected_var = tkinter.StringVar()
        self.column_selected_combobox = ttk.Combobox(self.app, textvariable=self.column_selected_var)
        self.column_selected_combobox["values"] = ("Column 1", "Column 2", "Column 3")
        self.column_selected_combobox.set("Column 1")
        self.column_selected_combobox.grid(row=2, column=3, padx=10, pady=10)

        self.player_1_select_button = tkinter.Button(self.app, text="Player 1", command=self.add_cross)
        self.player_1_select_button.grid(row=3, column=1, padx=10, pady=10)

        self.player_2_select_button = tkinter.Button(self.app, text="Player 2", command=self.add_circle)
        self.player_2_select_button.grid(row=3, column=3, padx=10, pady=10)

        self.cross_images = []
        self.circle_images = []
        self.board = [EMPTY_CELL] * TOTAL_CELLS
        self.is_player_1_turn = True

        self.init_game_board_canvas()

    def init_game_board_canvas(self):
        for row in range(1,3):
            self.game_board_canvas.create_line(row * CELL_SIZE, 10, row * CELL_SIZE, 290)
        for column in range(1,3):
            self.game_board_canvas.create_line(10, column * CELL_SIZE, 290, column * CELL_SIZE)

    def add_cross(self):
        if self.is_player_1_turn:
            row_selected = self.row_selected_combobox.current()
            column_selected = self.column_selected_combobox.current()

            if self.board[row_selected*3 + column_selected] == EMPTY_CELL:
                cross_image = Image.open("./tic-tac-toe/static/cross.png")
                cross_image = cross_image.resize((CELL_SIZE - 10, CELL_SIZE - 10), Image.Resampling.LANCZOS)

                cross_image = ImageTk.PhotoImage(cross_image)
                self.cross_images.append(cross_image)

                self.game_board_canvas.create_image(column_selected*CELL_SIZE + CELL_SIZE/2, row_selected*CELL_SIZE + CELL_SIZE/2, image=cross_image)
                self.board[row_selected*3 + column_selected] = CROSS_CELL

                self.is_player_1_turn = False
                self.check_winner()
            else:
                print("The selected cell is already full")
        else:
            print("It is Player 2's turn!")

    def add_circle(self):
        if not self.is_player_1_turn:
            row_selected = self.row_selected_combobox.current()
            column_selected = self.column_selected_combobox.current()

            if self.board[row_selected*3 + column_selected] == EMPTY_CELL:
                circle_image = Image.open("./tic-tac-toe/static/circle.png")
                circle_image = circle_image.resize((CELL_SIZE - 10, CELL_SIZE - 10), Image.Resampling.LANCZOS)

                circle_image = ImageTk.PhotoImage(circle_image)
                self.circle_images.append(circle_image)

                self.game_board_canvas.create_image(column_selected*CELL_SIZE + CELL_SIZE/2, row_selected*CELL_SIZE + CELL_SIZE/2, image=circle_image)
                self.board[row_selected*3 + column_selected] = CIRCLE_CELL

                self.is_player_1_turn = True
                self.check_winner()
            else:
                print("The selected cell is already full")
        else:
            print("It is Player 1's turn!")

    def check_winner(self):
        for i in range(3):
            if self.board[i*3] == self.board[i*3 + 1] == self.board[i*3 + 2] == CROSS_CELL:
                print("Player 1 wins!")
                self.player_1_select_button.config(state="disabled")
                self.player_2_select_button.config(state="disabled")
            elif self.board[i*3] == self.board[i*3 + 1] == self.board[i*3 + 2] == CIRCLE_CELL:
                print("Player 2 wins!")
                self.player_1_select_button.config(state="disabled")
                self.player_2_select_button.config(state="disabled")
            elif self.board[i] == self.board[i + 3] == self.board[i + 6] == CROSS_CELL:
                print("Player 1 wins!")
                self.player_1_select_button.config(state="disabled")
                self.player_2_select_button.config(state="disabled")
            elif self.board[i] == self.board[i + 3] == self.board[i + 6] == CIRCLE_CELL:
                print("Player 2 wins!")
                self.player_1_select_button.config(state="disabled")
                self.player_2_select_button.config(state="disabled")
        if self.board[0] == self.board[4] == self.board[8] == CROSS_CELL:
            print("Player 1 wins!")
            self.player_1_select_button.config(state="disabled")
            self.player_2_select_button.config(state="disabled")
        elif self.board[0] == self.board[4] == self.board[8] == CIRCLE_CELL:
            print("Player 2 wins!")
            self.player_1_select_button.config(state="disabled")
            self.player_2_select_button.config(state="disabled")
        elif self.board[2] == self.board[4] == self.board[6] == CROSS_CELL:
            print("Player 1 wins!")
            self.player_1_select_button.config(state="disabled")
            self.player_2_select_button.config(state="disabled")
        elif self.board[2] == self.board[4] == self.board[6] == CIRCLE_CELL:
            print("Player 2 wins!")
            self.player_1_select_button.config(state="disabled")
            self.player_2_select_button.config(state="disabled")


if __name__ == '__main__':
    gui = tkinter.Tk()
    my_app = MyApp(gui)

    gui.mainloop()