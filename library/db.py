import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from dotenv import load_dotenv
import os

class DBUtil:
    def __init__(self):
        self.__connection = None
        self.db_config = {
            "dbname":os.getenv("DBNAME"),
            "user":os.getenv("DB_USER"),
            "password":os.getenv("DB_PASSWORD"),
            "host":os.getenv("DB_HOST"),
            "port":os.getenv("DB_PORT"),
        }

    def connect(self):
        try:
            if self.__connection is None or self.__connection.closed != 0:
                self.__connection = psycopg2.connect(**self.db_config)
            return self.__connection
        except psycopg2.Error as e:
            print(e)
            raise

    def close_connection(self):
        if self.__connection is not None and self.__connection.closed == 0:
            self.__connection.close()
            self.__connection = None
def execute_query(query, params = None, fetch_one = False, fetch_all = False):
    db = DBUtil()
    connection = db.connect()
    try:
        cursor = connection.cursor(cursor_factory = RealDictCursor)
        cursor.execute(query, params or ())

        if query.strip().upper().startswith(('UPDATE','DELETE','INSERT')):
            connection.commit()

        if fetch_one:
            return cursor.fetchone()
        
        if fetch_all:
            return cursor.fetchall()
        
        return None
    except Exception as e:
        connection.rollback()
        print('DB connection failed',e)
        raise
    finally:
        db.close_connection()           

def insert(table_name, data):
    keys = data.keys()
    params = tuple(data.values())

    query = f"""
        INSERT INTO {table_name} ({', '.join(keys)}, created_at)
        VALUES ({', '.join(['%s'] * len(params))}, CURRENT_TIMESTAMP)
        RETURNING * 
    """

    return execute_query(query, params, fetch_one = True)