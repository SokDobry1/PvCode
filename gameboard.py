from tkinter import *
from draw_images import *

class Tile:
    def update_tile(self, status):
        statuses = {"clear": clear_tile}
        if status != self.status:
            if self.number != None:
                c.delete(self.number)
            self.status = status
            self.number = statuses[status](self.c, self.x0, self.y0, self.size)

    def __init__(self, c, x0, y0, size):
        self.x0 = x0; self.y0 = y0; self.size = size
        self.c = c
        self.status = None
        self.number = None
        self.update_tile("clear")


class Board:
    def create_board(self):
        _size = (self.x1 - self.x0) / (self.k_tiles + (self.k_tiles + 1) * 0.1)
        _indent = _size * 0.1
        self.board_objects = []
        for i in range(self.k_tiles):
            _line = []
            for j in range(self.k_tiles):
                pos_x = self.x0 + _indent + (_size + _indent) * j
                pos_y = self.y0 + _indent + (_size + _indent) * i
                _line += [Tile(self.c, pos_x, pos_y, _size)]
            self.board_objects += [_line]

    
    def __init__(self, c, k_tiles, 
                screen_width, screen_height):
        self.x0, self.y0, self.x1, self.y1  = 0,0,0,0
        self.k_tiles = k_tiles; self.c = c
        if screen_height < screen_width:
            self.x0 = (screen_width - screen_height) // 2; self.y0 = 0
            self.x1 = (screen_width - screen_height) // 2 + screen_height; self.y1 = screen_height
        else:
            self.y0 = (screen_height - screen_width) // 2; self.x0 = 0
            self.y1 = (screen_height - screen_width) // 2 + screen_width; self.x1 = screen_width

        c.create_rectangle(self.x0, self.y0, self.x1, self.y1, 
                           fill = "lawn green", outline = "white", width=5)

        _delta = 3
        self.x0 += _delta; self.y0 += _delta; self.x1 -= _delta; self.y1 -= _delta
        
        self.create_board()


def main():


    k_tiles = 15
    screen_width = 1080; screen_height = 768

    window = Tk() #Создаем канвас
    window.title("PvCode")
    c = Canvas(window, width = screen_width, height = screen_height, bg = 'green')
    c.pack()

    board = Board(c, k_tiles, screen_width, screen_height)

    window.mainloop()

main()
