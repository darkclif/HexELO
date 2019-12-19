import itertools
from menus.menu_input_entry import MenuInputEntry
from menus.menu_entry import MenuEntry
from screen import Screen
from key_codes import KeyCodes


class MenuToolbar:
    def __init__(self, layout):
        self._pos = (0, 0)      # unlimited
        self._max_size = (0, 0) # unlimited

        # Assign callbacks
        self._callbacks = {}
        self.__assign_callback(layout)

        # Prerender layout
        self._str_toolbar = ''
        self.__spawn_layout(layout)
        
    # Base
    def on_input(self, key_code):
        if key_code in self._callbacks.keys():
            self._callbacks[key_code]()

    def on_render(self, screen):
        screen.put_string(self._pos[0], self._pos[1], self._str_toolbar)

    # Settings
    def set_position(self, rows, cols):
        self._pos = (rows, cols)

    def set_maxsize(self, rows, cols):
        self._max_size = (rows, cols)

    # Internal
    def __spawn_layout(self, layout):
        # row = [key_code, name, func]
        for entry in layout:
            self._str_toolbar += '[{}] {}  '.format(KeyCodes.get_keycode_string(entry[0]), entry[1])

    def __assign_callback(self, layout):
        for entry in layout:
            self._callbacks[entry[0]] = entry[2]