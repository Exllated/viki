import formatting
import extra_utils

TEXT_LIST = ['']

CARET_POS = (0, 0)

CARET_SHIFT_DICT = {
    'ArrowRight': (0, 1),
    'ArrowLeft': (0, -1),
    'ArrowDown': (1, 0),
    'ArrowUp': (-1, 0)
}


def key_pressed(key):
    global TEXT_LIST
    global CARET_POS

    if len(key) == 1:
        add_text(key)
        move_caret((0, 1))
    elif key == 'Enter':
        TEXT_LIST.insert(CARET_POS[0] + 1, '')
        move_caret((1, 0))
    elif key.startswith('Arrow'):
        move_caret(CARET_SHIFT_DICT[key])
    pass


def move_caret(shift):
    global CARET_POS
    line_pos = max(min(CARET_POS[0] + shift[0], len(TEXT_LIST) - 1), 0)
    char_pos = max(min(CARET_POS[1] + shift[1], len(TEXT_LIST[line_pos])), 0)
    CARET_POS = (line_pos, char_pos)
    pass


def add_text(text):
    global CARET_POS
    global TEXT_LIST
    TEXT_LIST[CARET_POS[0]] = extra_utils.insert_in_string(TEXT_LIST[CARET_POS[0]], text, CARET_POS[1])
    pass
