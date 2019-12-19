import os.path
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class HexDatabase:
    def __init__(self):
        self._db_path = './neuroshimahex.db'
        self._connection = None

    # Init
    def db_init(self):
        if not os.path.isfile(self._db_path):
            self.__create_new()
        else:
            self._connection = sqlite3.connect(self._db_path)

    def __create_new(self):
        self._connection = sqlite3.connect(self._db_path)
        conn = self._connection

        # Creaete new tables

        # PLAYERS
        # (id, nick, real_name, elo)
        conn.execute('''
            CREATE TABLE players (id, nick, real_name, elo)
        ''')

        # GAMES
        # (id, date, notes)
        conn.execute('''
            CREATE TABLE games (id, date, notes)
        ''')
        
        # PLAYERS_GAMES
        # (game_id, player_id, army_id, team_number, position, elo_after)
        conn.execute('''
            CREATE TABLE players_games (game_id, player_id, army_id, team_number, position, elo_after)
        ''')

        # ARMIES
        # (id, name)
        conn.execute('''
            CREATE TABLE armies (id, name)
        ''')

        conn.execute('''INSERT INTO armies VALUES 
            (1, 'Moloch'),
            (2, 'Borgo'),
            (3, 'Posterunek'),
            (4, 'Hegemonia')
        ''')

        conn.commit()

    # Interface

    ################################# PLAYERS
    def get_players(self):
        conn = self._connection
        conn.row_factory = dict_factory

        cur = conn.cursor()
        cur.execute('''SELECT * FROM players''')

        return [row for row in cur]

    def delete_player(self, player_id):
        conn = self._connection

        conn.execute('''DELETE FROM players WHERE id = ?''', (player_id,))
        conn.commit()

        return True

    def add_player(self, player):
        # player = [nick, real_name]
        conn = self._connection

        new_id = list(conn.execute('''SELECT MAX(id) as max_id FROM players'''))[0]['max_id'] + 1
        conn.execute('''INSERT INTO players VALUES (?, ?, ?, ?)''', (new_id, player[0], player[1], 1000))
        conn.commit()

        return True