class Screen:
    def __init__(self, stdscr):
        # Curses
        self._rows, self._cols = stdscr.getmaxyx()
        self._stdscr = stdscr

        # Redraw flag
        self._redraw = True

        # Create buffers
        self._old_buffer = [[' ' for _ in range(self._cols)] for _ in range(self._rows)]
        self._new_buffer = [[' ' for _ in range(self._cols)] for _ in range(self._rows)]
        
    def put_string(self, i, j, string):
        for k, c in enumerate(string):
            tmp_i = i % self._rows
            tmp_j = (j + k) % self._cols
            self._new_buffer[tmp_i][tmp_j] = c
        self._redraw = True

    def clear(self):
        self._new_buffer = [[' ' for _ in range(self._cols)] for _ in range(self._rows)]
        self._redraw = True

    def render(self):
        # Nothing to draw
        if not self._redraw:
            return

        for i in range(self._rows):
            for j in range(self._cols):
                if self._new_buffer[i][j] !=  self._old_buffer[i][j]:
                    new_char = self._new_buffer[i][j]
                    self._stdscr.addstr(i, j, new_char)

        self._old_buffer = [row[:] for row in self._new_buffer]
        self._redraw = False

        # Show
        self._stdscr.refresh()