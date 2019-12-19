import itertools
from menus.menu_input_entry import MenuInputEntry
from menus.menu_entry import MenuEntry
from key_codes import KeyCodes


class MenuInput:
    # Actions
    ACTION_UP      = KeyCodes.ARROW_UP
    ACTION_DOWN    = KeyCodes.ARROW_DOWN
    ACTION_SELECT  = KeyCodes.RETURN

    def __init__(self, layout):
        self._pos = (0, 0)      # unlimited
        self._max_size = (0, 0) # unlimited

        self._entries = []
        self._input_entries = []
        self._curr_entry = 0
        
        self.__spawn_layout(layout)

    # Settings
    def set_position(self, rows, cols):
        self._pos = (rows, cols)

    def set_maxsize(self, rows, cols):
        self._max_size = (rows, cols)

    def get_input_data(self):
        return [ entry.input for entry in self._input_entries]

    # Base
    def on_input(self, key_code):
        if key_code == MenuInput.ACTION_UP:
            self.__inc_curr()
        elif key_code == MenuInput.ACTION_DOWN:
            self.__dec_curr()
        elif key_code == MenuInput.ACTION_SELECT:
            self.__select()
        else:
            self._entries[self._curr_entry].on_input(key_code)

    def on_render(self, screen):
        for i, item in enumerate(self._entries):
            selection = ' '
            if self._curr_entry == i:
                selection = '>'

            screen.put_string(self._pos[0] + i, self._pos[1] + 0, selection + item.get_string())

    # Internal
    def __spawn_layout(self, layout):
        # Data layout
        for entry in layout:
            new_entry = MenuInputEntry(*entry)
            self._input_entries.append(new_entry)
            self._entries.append(new_entry)

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
