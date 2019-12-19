from states.state import State
from menus.menu_input import MenuInput
from menus.menu_toolbar import MenuToolbar
from key_codes import KeyCodes


class StateInput(State):
    def __init__(self, context, layout, func):
        super(StateInput, self).__init__(context)
        # layout = {
        #   'title': str,
        #   'inputs': [
        #       [label, mode, func, data, value = ''],
        #       ...
        #   ]
        # } 

        # Settings
        self._size = (context.main_screen.get_maxsize()[0] - 1, 40)

        # Outside function to handle input data on confirm
        self._return_handler_func = func

        # Menu
        self._menu = MenuInput(layout['inputs'], (10, self._size[1]))
        self._menu.set_position(3, 0)

        # Bottom toolbar
        toolbar_layout = [
            [KeyCodes.RETURN, 'Accept', self.__on_confirm],
            [KeyCodes.ESCAPE, 'Cancel', self.__on_cancel]
        ]

        self._toolbar = MenuToolbar(toolbar_layout)
        self._toolbar.set_position(context.main_screen.get_maxsize()[0] - 1, 0)

        # Setup
        self._header = ['', '', '']
        self.__spawn_layout(layout)

    # Base
    def on_input(self, key_code):
        self._menu.on_input(key_code)
        self._toolbar.on_input(key_code)

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

        # Menu & Toolbar
        self._menu.on_render(screen)
        self._toolbar.on_render(screen)

    # Event handlers
    def __on_cancel(self):
        self.pop_this_state()
    
    def __on_confirm(self):
        self.pop_this_state()

        if self._return_handler_func:
            menu_data = self._menu.get_input_data()
            self._return_handler_func(menu_data)

    def __spawn_layout(self, layout):
        # table = [ '│', '─', '┌', '┬', '┐','├', '┼', '┤','└', '┴', '┘']
        self._header[0] = '│ {} │'.format(layout['title'].ljust(self._size[1] - 4))
        self._header[1] = '├' + ('─' * (self._size[1] - 2)) + '┤'
        self._header[2] = '└' + ('─' * (self._size[1] - 2)) + '┘'