from states.state import State
from menus.menu_input import MenuInput
from menus.menu_toolbar import MenuToolbar
from key_codes import KeyCodes


class StateInput(State):
    def __init__(self, context, title, layout, func):
        super(StateInput, self).__init__(context)

        # Outside function to handle input data on confirm
        self._return_handler_func = func

        # Title
        self._title = title 

        # Menu
        self._menu = MenuInput(layout)
        self._menu.set_position(2, 0)

        # Bottom toolbar
        layout = [
            [KeyCodes.RETURN, 'Accept', self.on_confirm],
            [KeyCodes.ESCAPE, 'Cancel', self.on_cancel]
        ]

        self._toolbar = MenuToolbar(layout)
        self._toolbar.set_position(context.main_screen.get_maxsize()[0] - 1, 0)


    # Base
    def on_input(self, key_code):
        self._menu.on_input(key_code)
        self._toolbar.on_input(key_code)

    def on_update(self, dt):
        pass

    def on_render(self, screen):
        screen.put_string(0, 0, self._title)
        self._menu.on_render(screen)
        self._toolbar.on_render(screen)

    # Event handlers
    def on_cancel(self):
        self.pop_this_state()
    
    def on_confirm(self):
        self.pop_this_state()

        if self._return_handler_func:
            menu_data = self._menu.get_input_data()
            self._return_handler_func(menu_data)
    