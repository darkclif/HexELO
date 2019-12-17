import curses


class Pixel:
    def __init__(self, char = ' ', color_id = 0):
        self.char = char
        self.color_id = color_id


class Screen:
    # Colors
    COLOR_DEFAULT = 0
    COLOR_INVERTED = 1
    COLOR_SELECTION = COLOR_INVERTED

    def __init__(self, stdscr):
        # Curses
        self._rows, self._cols = stdscr.getmaxyx()
        self._stdscr = stdscr

        # Color
        curses.init_pair(Screen.COLOR_INVERTED, 0, 7)

        # Redraw flag
        self._redraw = True

        # Create buffers
        self._old_buffer = [[Pixel() for _ in range(self._cols)] for _ in range(self._rows)]
        self._new_buffer = [[Pixel() for _ in range(self._cols)] for _ in range(self._rows)]
        
    def put_string(self, i, j, string, color = COLOR_DEFAULT):
        tmp_i = i % self._rows
        for k, c in enumerate(string):
            tmp_j = (j + k) % self._cols
            self._new_buffer[tmp_i][tmp_j].char = c
            self._new_buffer[tmp_i][tmp_j].color_id = color
        self._redraw = True

    def clear(self):
        self._new_buffer = [[Pixel() for _ in range(self._cols)] for _ in range(self._rows)]
        self._redraw = True

    def render(self):
        # Nothing to draw
        if not self._redraw:
            return

        for i in range(self._rows):
            for j in range(self._cols):
                if (
                    (self._new_buffer[i][j].char !=  self._old_buffer[i][j].char) 
                    or (self._new_buffer[i][j].color_id !=  self._old_buffer[i][j].color_id)
                ):
                    new_char = self._new_buffer[i][j].char
                    new_color = self._new_buffer[i][j].color_id
                    self._stdscr.addstr(i, j, new_char, curses.color_pair(new_color))

        self._old_buffer = [row[:] for row in self._new_buffer]
        self._redraw = False

        # Show
        self._stdscr.refresh()