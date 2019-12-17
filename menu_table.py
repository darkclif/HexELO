import itertools
from menu_input_entry import MenuInputEntry
from menu_entry import MenuEntry
from screen import Screen

class MenuTable:
    KEY_UP      = 259 # ARROW_UP
    KEY_DOWN    = 258 # ARROW_DOWN
    KEY_SELECT  = 10 # ENTER

    def __init__(self, columns, data):
        self._columns = columns
        self._data = data
        self._entries = []
        self._curr_entry = 0

        # Prerender layout
        self._str_head = ''
        self._str_head_sep = ''

        self.__spawn_layout()
        
    def __spawn_layout(self):
        for col in self._columns:
            self._str_head += col[0].rjust(col[1]) + '|'
            self._str_head_sep += (col[1] * '─') + '┼'

        for i, d in enumerate(self._data):
            field_list = [str(v) for v in d.values()]
            label = ''
            for j, col in enumerate(self._columns):
                label += field_list[j].rjust(col[1]) + '|'

            self._entries.append(MenuEntry(label, None, i)) 

    def on_input(self, key_code):
        if key_code == MenuTable.KEY_UP:
            self.__inc_curr()
        elif key_code == MenuTable.KEY_DOWN:
            self.__dec_curr()
        elif key_code == MenuTable.KEY_SELECT:
            self.__select()

    def on_render(self, screen):
        screen.put_string(0, 0, self._str_head)
        screen.put_string(1, 0, self._str_head_sep)

        for i, item in enumerate(self._entries):
            color = Screen.COLOR_DEFAULT
            if self._curr_entry == i:
                color = Screen.COLOR_INVERTED

            screen.put_string(2 + i, 0, item.get_string(), color)

    # Internal
    def __inc_curr(self):
        self._curr_entry -= 1
        self._curr_entry = max(0, min(self._curr_entry, len(self._entries)-1))

    def __dec_curr(self):
        self._curr_entry += 1
        self._curr_entry = max(0, min(self._curr_entry, len(self._entries)-1))

    def __select(self):
        func = self._entries[self._curr_entry].func
        if func:
            data = self._entries[self._curr_entry].data
            func(data)
