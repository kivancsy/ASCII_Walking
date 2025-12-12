import curses
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(50)

    player_x = 5
    player_y = 3

    while True:
        stdscr.clear()

        for y in range(10):
            row = ""
            for x in range(20):
                if x == player_x and y == player_y:
                    row += "@"
                else:
                    row += "."
            stdscr.addstr(y, 0, row)

        key = stdscr.getch()

        if key == ord('w'):
            player_y = max(0, player_y - 1)
        elif key == ord('s'):
            player_y = min(9, player_y + 1)
        elif key == ord('a'):
            player_x = max(0, player_x - 1)
        elif key == ord('d'):
            player_x = min(19, player_x + 1)
        elif key == ord('q'):
            break

        time.sleep(0.01)

curses.wrapper(main)
