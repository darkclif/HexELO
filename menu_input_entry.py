class MenuInputEntry:
    MODE_NUMBER = 1
    MODE_ALPHANUMERIC = 2

    def __init__(self, label, mode = MODE_ALPHANUMERIC, func = None, data = None):
        self.label = label
        self.func = func
        self.input = ''
        self.data = data
        self.mode = mode

    def get_string(self):
        return self.label + ': ' + self.input

    def on_input(self, key_code):
        if key_code == 263:
            self.input = self.input[:-1]
            return

        if self.mode == MenuInputEntry.MODE_NUMBER:
            if (47 < key_code < 58):
                self.input += chr(key_code) 
        elif self.mode == MenuInputEntry.MODE_ALPHANUMERIC:
            if (47 < key_code < 58) or (64 < key_code < 91) or (96 < key_code < 123) or (key_code == 32):
                self.input += chr(key_code)
