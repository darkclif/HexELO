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

    def __init__(self, context, title, options, callback):
        super(StateDialog, self).__init__(context)

        # Outside function to handle input data on confirm
        self._return_handler_func = callback

        # Title
        self._title = title 

        # Menu
        self._menu = Menu()
        self._menu.set_position(2, 0)

        if options & StateDialog.OPTION_OK:
            self._menu.add_entry('OK', self.on_option_selected, StateDialog.OPTION_OK)
        if options & StateDialog.OPTION_CANCEL:
            self._menu.add_entry('Cancel', self.on_option_selected, StateDialog.OPTION_CANCEL)

    # Base
    def on_input(self, key_code):
        self._menu.on_input(key_code)

    def on_update(self, dt):
        pass

    def on_render(self, screen):
        screen.put_string(0, 0, self._title)
        self._menu.on_render(screen)

    # On event
    def on_option_selected(self, option):
        self.pop_this_state()
        self._return_handler_func(option)
    