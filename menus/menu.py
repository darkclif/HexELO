import itertools
from menus.menu_entry import MenuEntry
from key_codes import KeyCodes
from screen import Screen


class Menu:
    # Actions
    ACTION_UP      = KeyCodes.ARROW_UP
    ACTION_DOWN    = KeyCodes.ARROW_DOWN
    ACTION_SELECT  = KeyCodes.RETURN

    def __init__(self):
        self._pos = (0, 0)      # unlimited
        self._max_size = (0, 0) # unlimited

        self._entries = []
        self._curr_entry = 0

    # Settings
    def set_position(self, rows, cols):
        self._pos = (rows, cols)

    def set_maxsize(self, rows, cols):
        self._max_size = (rows, cols)

    def on_input(self, key_code):
        if key_code == Menu.ACTION_UP:
            self.__inc_curr()

        if key_code == Menu.ACTION_DOWN:
            self.__dec_curr()

        if key_code == Menu.ACTION_SELECT:
            self.__select()

    def add_entry(self, label, func = None, data = None):
        self._entries.append(MenuEntry(label, func, data))

    def on_render(self, screen):
        for i, item in enumerate(self._entries):
            color = Screen.COLOR_DEFAULT
            if self._curr_entry == i:
                color = Screen.COLOR_INVERTED

            screen.put_string(self._pos[0] + i, self._pos[1] + 0, item.get_string(), color)

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
