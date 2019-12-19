import curses
import time

from screen import Screen
from state_machine import StateMachine
from global_context import GlobalContext
from hex_database import HexDatabase

def main(stdscr):
    # Settings
    stdscr.nodelay(True)
    curses.curs_set(0)

    SLEEP_TIME = 1./120.0
    RENDER_TIME = 1./60.0

    # Context for whole application
    global_context = GlobalContext()
    global_context.main_screen = Screen(stdscr)
    global_context.database = HexDatabase()
    global_context.database.db_init()
    global_context.state_machine = StateMachine(global_context)

    # Aliases
    state_machine = global_context.state_machine
    main_screen = global_context.main_screen

    gClose = False
    render_timer = 0. # 
    while (not gClose) and (not state_machine.is_empty()):
        time.sleep(SLEEP_TIME)
        render_timer += SLEEP_TIME

        # Input
        key = stdscr.getch()
        if key != -1:
            state_machine.on_input(key)

        # Update
        state_machine.on_update(SLEEP_TIME)

        # Render
        if render_timer >= RENDER_TIME:
            main_screen.clear()
            state_machine.on_render()
            main_screen.render()

            render_timer = 0.

# Run main APP
curses.wrapper(main)