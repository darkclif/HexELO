from state import State
from menu_input import MenuInput


class StateInput(State):
    def __init__(self, context, layout, func):
        super(StateInput, self).__init__(context)

        self._menu = MenuInput(layout)
        self._menu.func_cancel = self.on_cancel
        self._menu.func_confirm = self.on_confirm

        # Outside function to handle input data on confirm
        self._return_handler_func = func

    # Base
    def on_input(self, key_code):
        self._menu.on_input(key_code)

    def on_update(self, dt):
        pass

    def on_render(self, screen):
        self._menu.on_render(screen)

    # Event handlers
    def on_cancel(self, data):
        self.pop_this_state()
    
    def on_confirm(self, data):
        self.pop_this_state()

        if self._return_handler_func:
            menu_data = self._menu.get_input_data()
            self._return_handler_func(menu_data)
    