from state import State
from menu_table import MenuTable

class StateShowPlayers(State):
    def __init__(self, context):
        super(StateShowPlayers, self).__init__(context)

        columns = [('a', 12), ('a', 12), ('a', 12)]
        data = context.database.get_players()
        self._menu = MenuTable(columns, data)

    # Base
    def on_input(self, key_code):
        self._menu.on_input(key_code)

    def on_update(self, dt):
        pass

    def on_render(self, screen):
        self._menu.on_render(screen)

    # Event handlers
