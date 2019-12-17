import itertools
from menu_input_entry import MenuInputEntry
from menu_entry import MenuEntry


class MenuInput:
    KEY_UP      = 259 # ARROW_UP
    KEY_DOWN    = 258 # ARROW_DOWN
    KEY_SELECT  = 10 # ENTER

    def __init__(self, layout, pos = (0, 0)):
        self.func_confirm = None
        self.func_cancel = None

        self._entries = []
        self._input_entries = []
        self._curr_entry = 0
        self._pos = pos

        self.__spawn_layout(layout)

    def get_input_data(self):
        return [ entry.input for entry in self._input_entries]

    def on_input(self, key_code):
        if key_code == MenuInput.KEY_UP:
            self.__inc_curr()
        elif key_code == MenuInput.KEY_DOWN:
            self.__dec_curr()
        elif key_code == MenuInput.KEY_SELECT:
            self.__select()
        else:
            self._entries[self._curr_entry].on_input(key_code)

    def on_render(self, screen):
        for i, item in enumerate(self._entries):
            selection = ' '
            if self._curr_entry == i:
                selection = '>'

            screen.put_string(self._pos[0] + i, self._pos[1] + 0, selection + item.get_string())

    # Event handlers
    def __on_cancel(self, data):
        if self.func_cancel:
            self.func_cancel(data)

    def __on_confirm(self, data):
        if self.func_confirm:
            self.func_confirm(data)

    # Internal
    def __spawn_layout(self, layout):
        # Data layout
        for entry in layout:
            new_entry = MenuInputEntry(*entry)
            self._input_entries.append(new_entry)
            self._entries.append(new_entry)

        # Utils entries
        self._entries.append(MenuEntry(''))
        self._entries.append(MenuEntry('Confirm', self.__on_confirm))
        self._entries.append(MenuEntry('Cancel', self.__on_cancel))

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
