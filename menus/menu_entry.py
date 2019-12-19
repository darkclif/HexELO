class MenuEntry:
    def __init__(self, label, func = None, data = None):
        self.label = label
        self.func = func
        self.data = data

    def get_string(self):
        return self.label

    def on_input(self, key_code):
        pass
