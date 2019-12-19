class KeyCodes:
    # Key codes
    ESCAPE      = 27
    BACKSPACE   = 263
    RETURN      = 10
    SPACE       = 32

    ARROW_UP    = 259 
    ARROW_DOWN  = 258 
    ARROW_LEFT  = 260
    ARROW_RIGHT = 261

    # Key ASCII
    DICT = {
        # Arrows
        ARROW_UP:       '↑',
        ARROW_DOWN:     '↓',
        ARROW_RIGHT:    '→',
        ARROW_LEFT:     '←',

        SPACE:          'SPACE',
        BACKSPACE:      'BCK',
        ESCAPE:         'ESC',
        RETURN:         'RET'
    }

    @staticmethod
    def get_keycode_string(key_code):
        if (47 < key_code < 58) or (64 < key_code < 91) or (96 < key_code < 123):
            return chr(key_code).upper()
        elif key_code in KeyCodes.DICT.keys():
            return KeyCodes.DICT[key_code]
        else:
            return '?'
            
