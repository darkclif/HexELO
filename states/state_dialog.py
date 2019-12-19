from states.state import State
from menus.menu import Menu
from menus.menu_toolbar import MenuToolbar
from key_codes import KeyCodes
from functools import partial


class StateDialog(State):
    # Options
    OPTION_OK       = 1
    OPTION_CANCEL   = 1 << 1

    OPTION_OK_CANCEL = OPTION_OK | OPTION_CANCEL

    def __init__(self, context, layout, callback):
        super(StateDialog, self).__init__(context)

        # Settings
        self._size = (context.main_screen.get_maxsize()[0] - 1, 40)

        # Outside function to handle input data on confirm
        self._return_handler_func = callback

        # Menu
        self._menu = Menu()
        self._menu.set_position(2, 2)

        if layout['options'] & StateDialog.OPTION_OK:
            self._menu.add_entry('OK', self.on_option_selected, StateDialog.OPTION_OK)
        if layout['options'] & StateDialog.OPTION_CANCEL:
            self._menu.add_entry('Cancel', self.on_option_selected, StateDialog.OPTION_CANCEL)
        
        # Setup
        self._header = ['', '', '']
        self.__spawn_layout(layout)

    # Base
    def on_input(self, key_code):
        self._menu.on_input(key_code)

    def on_update(self, dt):
        pass

    def on_render(self, screen):
        # Frame
        screen.put_string(0, 0, self._header[0])
        screen.put_string(1, 0, self._header[1])
        screen.put_string(self._size[0] - 1, 0, self._header[2])

        for i in range(2, self._size[0] - 1):
            screen.put_string(i, 0, '│')
            screen.put_string(i, self._size[1] - 1, '│')

        # Menu
        self._menu.on_render(screen)

    # On event
    def on_option_selected(self, option):
        self.pop_this_state()
        self._return_handler_func(option)

    def __spawn_layout(self, layout):
        self._header[0] = '│ {} │'.format(layout['title'].ljust(self._size[1] - 4))
        self._header[1] = '├' + ('─' * (self._size[1] - 2)) + '┤'
        self._header[2] = '└' + ('─' * (self._size[1] - 2)) + '┘'
    
    