from states.state import State
from menus.menu import Menu

class StateMain(State):
    def __init__(self, context):
        super(StateMain, self).__init__(context)

        self._menu = Menu()
        self._menu.add_entry("Show ranking", self.on_show_ranking)
        self._menu.add_entry("Show games", self.on_show_games)
        self._menu.add_entry("Show players", self.on_show_players)
        self._menu.add_entry("Add players", self.on_add_player)
        self._menu.add_entry("")
        self._menu.add_entry("Quit", self.on_quit)

    # Base
    def on_input(self, key_code):
        self._menu.on_input(key_code)

    def on_update(self, dt):
        pass

    def on_render(self, screen):
        self._menu.on_render(screen)

    # Event handlers
    def on_show_ranking(self, data):
        self._context.main_screen.put_string(2, 10, 'X')

    def on_add_player(self, data):
        pass
    
    def on_show_games(self, data):
        pass

    def on_show_players(self, data):
        self._context.state_machine.req_push_state('SHOW_PLAYERS')

    def on_quit(self, data):
        self.pop_this_state()
