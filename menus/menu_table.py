import itertools
from menus.menu_input_entry import MenuInputEntry
from menus.menu_entry import MenuEntry
from screen import Screen
from key_codes import KeyCodes


class MenuTable:
    # Actions
    ACTION_UP      = KeyCodes.ARROW_UP
    ACTION_DOWN    = KeyCodes.ARROW_DOWN
    ACTION_SELECT  = KeyCodes.RETURN

    def __init__(self, columns, data):
        # columns = [(name, width), ...]
        # data = [{col1: data1, ...}, ...]
        self.func_select = None

        self._pos = (0, 0)      # unlimited
        self._max_size = (0, 0) # unlimited

        self._columns = columns
        self._data = data

        self._entries = []
        self._curr_entry = 0
        self._curr_top = 0

        # Prerender layout
        self._header_size = 2
        self._str_head = ''
        self._str_head_sep = ''
        self._str_empty = ''
        self._str_end = ''

        self.__spawn_layout()
        
    # Accesors
    def get_current_data(self):
        return self._data[self._curr_entry]

    # Base
    def on_input(self, key_code):
        if key_code == MenuTable.ACTION_UP:
            self.__inc_curr()
        elif key_code == MenuTable.ACTION_DOWN:
            self.__dec_curr()
        elif key_code == MenuTable.ACTION_SELECT:
            self.__select()

    def on_render(self, screen):
        screen.put_string(self._pos[0], self._pos[1], self._str_head)
        screen.put_string(self._pos[0] + 1, self._pos[1], self._str_head_sep)
        screen.put_string(self._pos[0] + self._max_size[0], self._pos[1], self._str_end)

        for i in range(self._max_size[0] - self._header_size):
            curr_i = self._curr_top + i

            if curr_i >= len(self._entries):
                screen.put_string(self._pos[0] + self._header_size + i, self._pos[1], self._str_empty)
            else:
                color = Screen.COLOR_DEFAULT
                if self._curr_entry == curr_i:
                    color = Screen.COLOR_INVERTED

                item = self._entries[curr_i]
                screen.put_string(self._pos[0] + self._header_size + i, self._pos[1], item.get_string(), color)

    # Settings
    def set_position(self, rows, cols):
        self._pos = (rows, cols)

    def set_maxsize(self, rows, cols):
        self._max_size = (rows, cols)

    # Internal
    def __spawn_layout(self):
        # Frame
        self._str_head = self._str_empty = '│'
        self._str_head_sep = '├'
        self._str_end = '└'
        for col in self._columns:
            self._str_empty += (col[1] * ' ') + '│'
            self._str_head_sep += (col[1] * '─') + '┼'
            self._str_end += (col[1] * '─') + '┴'
            self._str_head += col[0].rjust(col[1]) + '│'
        self._str_head_sep = self._str_head_sep[:-1] + '┤'
        self._str_end = self._str_end[:-1] + '┘'

        # Entries
        for i, d in enumerate(self._data):
            field_list = list(d.values())
            label = '│'
            for j, col in enumerate(self._columns):
                field = str(field_list[j])[:col[1]]
                label += field.rjust(col[1]) + '│'

            self._entries.append(MenuEntry(label, self.__on_item_select, i))

    def __inc_curr(self):
        self._curr_entry -= 1
        self._curr_entry = max(0, min(self._curr_entry, len(self._entries)-1))

        if self._curr_top > self._curr_entry:
            self._curr_top -= 1

    def __dec_curr(self):
        self._curr_entry += 1
        self._curr_entry = max(0, min(self._curr_entry, len(self._entries)-1))

        if self._curr_top + self._max_size[0] - self._header_size - 1 < self._curr_entry:
            self._curr_top += 1

    def __select(self):
        func = self._entries[self._curr_entry].func
        if func:
            data = self._entries[self._curr_entry].data
            func(data)

    def __on_item_select(self, data):
        if self.func_select:
            self.func_select(data)