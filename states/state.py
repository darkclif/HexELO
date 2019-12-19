class State:
    def __init__(self, context):
        self._is_pop = False
        
        self._context = context

    # Others
    def is_pop(self):
        return self._is_pop

    def pop_this_state(self):
        self._is_pop = True

    # Base
    def on_input(self, key_code):
        pass # To override

    def on_update(self, dt):
        pass # To override

    def on_render(self, screen):
        pass # To override
