from states.state import State
from menus.menu_table import MenuTable
from menus.menu_toolbar import MenuToolbar
from menus.menu_input_entry import MenuInputEntry
from states.state_dialog import StateDialog


class StateShowPlayers(State):
    def __init__(self, context):
        super(StateShowPlayers, self).__init__(context)

        # Menu
        self._menu = None
        self.spawn_menu_table()

        # Bottom toolbar
        layout = [
            [ord('a'), 'Add', self.on_player_add],
            [ord('d'), 'Delete', self.on_player_delete],
            [ord('e'), 'Edit', self.on_player_edit],
            [ord('q'), 'Exit', self.on_exit]
        ]

        self._toolbar = MenuToolbar(layout)
        self._toolbar.set_position(context.main_screen.get_maxsize()[0] - 1, 0)

    # Helpers
    def spawn_menu_table(self):
        columns = [('ID', 3), ('Nick', 12), ('Real name', 20), ('ELO', 6)]
        data = self._context.database.get_players()

        self._menu = MenuTable(columns, data)
        self._menu.set_position(0, 0)
        self._menu.set_maxsize(self._context.main_screen.get_maxsize()[0] - 2, 0)
        self._menu.func_select = self.on_player_select

    # Base
    def on_input(self, key_code):
        self._menu.on_input(key_code)
        self._toolbar.on_input(key_code)

    def on_update(self, dt):
        pass

    def on_render(self, screen):
        self._menu.on_render(screen)
        self._toolbar.on_render(screen)

    # Event handlers
    def on_player_select(self, data):
        pass

    def on_player_add(self):
        layout = {
            'title': 'Add new player', 
            'inputs':[
                MenuInputEntry('Nick'),
                MenuInputEntry('Real name'),
            ]
        }
        self._context.state_machine.req_push_state('INPUT', layout, self.add_player)

    def on_player_delete(self):
        layout = {
            'title': 'Are you sure?',
            'options': StateDialog.OPTION_OK_CANCEL
        }
        self._context.state_machine.req_push_state('DIALOG', layout, self.delete_player)

    def on_player_edit(self):
        data = self._menu.get_current_data()
        layout = {
            'title': 'Edit player', 
            'inputs':[
                MenuInputEntry('ID', value=data['id'], edit=False),
                MenuInputEntry('Nick', value=data['nick']),
                MenuInputEntry('Real name', value=data['real_name']),
                MenuInputEntry('ELO', MenuInputEntry.MODE_NUMBER, value=data['elo']),
            ]
        }
        self._context.state_machine.req_push_state('INPUT', layout, self.edit_player)

    def on_exit(self):
        self.pop_this_state()

    # Execute actions
    def delete_player(self, option):
        if option & StateDialog.OPTION_OK:
            player_id = self._menu.get_current_data()['id']
            self._context.database.delete_player(player_id)
            self.spawn_menu_table()

    def add_player(self, data):
        self._context.database.add_player(data)
        self.spawn_menu_table()

    def edit_player(self, data):
        self._context.database.edit_player(data)
        self.spawn_menu_table()