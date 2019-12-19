from states.state_main import StateMain
from states.state_setup import StateSetup
from states.state_input import StateInput
from states.state_show_players import StateShowPlayers
from states.state_dialog import StateDialog


class StateMachine:
    def __init__(self, context):
        self._context = context
        self._screen = context.main_screen
        self._states_stack = [StateMain(context)]
        self._stack_push_req = []

        self._state_builders = {
            'MAIN': StateMain,
            'SETUP': StateSetup,
            'INPUT': StateInput,
            'SHOW_PLAYERS': StateShowPlayers,
            'DIALOG': StateDialog
        }

    # Others
    def is_empty(self):
        return (len(self._states_stack) == 0)

    # Base
    def on_input(self, key_code):
        if not self.is_empty():
            self._states_stack[-1].on_input(key_code)

    def on_update(self, dt):
        if not self.is_empty():
            self._states_stack[-1].on_update(dt)

        # Pop state if flagged
        if self._states_stack[-1].is_pop():
            self._states_stack = self._states_stack[:-1]

        # Push requested states
        if self._stack_push_req:
            self._states_stack += self._stack_push_req
            self._stack_push_req = []

    def on_render(self):
        if not self.is_empty():
            self._states_stack[-1].on_render(self._screen)

    # Requests
    def req_push_state(self, string, *args):
        if not string in self._state_builders:
            raise Exception('There is no state builder under given name.')

        new_state = self._state_builders[string](self._context, *args)
        self._stack_push_req.append(new_state)