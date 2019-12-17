import itertools
from menu_entry import MenuEntry


class Menu:
    KEY_UP = 259 #ord('w')
    KEY_DOWN = 258 #ord('s')
    KEY_SELECT = 10

    def __init__(self, pos = (0, 0)):
        self._entries = []
        self._curr_entry = 0
        self._pos = pos

    def on_input(self, key_code):
        if key_code == Menu.KEY_UP:
            self.__inc_curr()

        if key_code == Menu.KEY_DOWN:
            self.__dec_curr()

        if key_code == Menu.KEY_SELECT:
            self.__select()

    def add_entry(self, label, func = None):
        self._entries.append(MenuEntry(label, func))

    def on_render(self, screen):
        for i, item in enumerate(self._entries):
            selection = ' '
            if self._curr_entry == i:
                selection = '>'

            screen.put_string(self._pos[0] + i, self._pos[1] + 0, selection + item.get_string())

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
