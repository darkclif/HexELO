class MenuInputEntry:
    # Modes
    MODE_NUMBER         = 1
    MODE_ALPHANUMERIC   = 2

    def __init__(self, label, mode = MODE_ALPHANUMERIC, func = None, data = None, **kwargs):
        self.label = label
        self.func = func
        self.input = ''
        self.data = data
        self.mode = mode
        
        self._max_length = 20
        self._can_edit = True

        if 'value' in kwargs:
            self.input = kwargs.get('value')
    
        if 'edit' in kwargs:
            self._can_edit = kwargs.get('edit')
        
    def set_length(self, length):
        self._max_length = length

    def get_string(self):
        tmp = self.label + ': ' + str(self.input)
        return tmp + max(0, self._max_length - len(tmp)) * '_'

    def on_input(self, key_code):
        if not self._can_edit:
            return

        if self.mode == MenuInputEntry.MODE_NUMBER:
            if (47 < key_code < 58):
                self.input = int(str(self.input) + chr(key_code))
            elif key_code == 263:
                new_str = str(self.input)[:-1]
                if not new_str:
                    new_str = '0'
                self.input = int(new_str)
        elif self.mode == MenuInputEntry.MODE_ALPHANUMERIC:
            if (47 < key_code < 58) or (64 < key_code < 91) or (96 < key_code < 123) or (key_code == 32):
                self.input += chr(key_code)
            elif key_code == 263:
                self.input = self.input[:-1]
