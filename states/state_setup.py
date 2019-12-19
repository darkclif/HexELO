from states.state import State
from menus.menu import Menu
from hex_database import HexDatabase


class StateSetup(State):
    def __init__(self, context):
        super(StateSetup, self).__init__(context)

        players = context.database.get_players()

        self._menu = Menu()
        self._menu.add_entry("Show ranking", self.on_show_ranking)

        for p in players:
            self._menu.add_entry(str(p.id) + p.nick)

    # Base
    def on_input(self, key_code):
        self._menu.on_input(key_code)

    def on_update(self, dt):
        pass

    def on_render(self, screen):
        self._menu.on_render(screen)

    # Event handlers
    def on_show_ranking(self, data):
        pass

    def on_add_player(self, data):
        pass

    def on_show_games(self, data):
        pass

    def on_quit(self, data):
        self.pop_this_state()