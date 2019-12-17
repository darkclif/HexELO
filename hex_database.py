import os.path
import sqlite3

class DataPlayer:
    def __init__(self, id, nick, real_name, elo):
        self.id = id
        self.nick = nick
        self.real_name = real_name
        self.elo = elo

    @classmethod
    def factory(cls, cursor, row):
        return cls(*row)

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
    def get_players(self):
        conn = self._connection
        conn.row_factory = DataPlayer.factory

        cur = conn.cursor()
        cur.execute('''SELECT * FROM players''')

        return [row for row in cur]

        