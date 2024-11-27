import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from dotenv import load_dotenv
import os

class DBUtil:
    def __init__(self):
         DBUtil.__connection = None
         DBUtil.db_config = {
            "dbname":"prod_cat",
            "user":os.getenv("DB_USER"),
            "password":os.getenv("DB_PASSWORD"),
            "host":os.getenv("DB_HOST"),
            "port":os.getenv("DB_PORT"),
        }

    def connect(self):
        try:
            if  self.__connection is None or  self.__connection.closed != 0:
                self.__connection = psycopg2.connect(** self.db_config)

            cursor = self.__connection.cursor()
            print(self.db_config['dbname'])
            cursor.execute("SELECT current_database();")
            db_name = cursor.fetchone()[0]
            print(f"Connected to database: {db_name}")
            cursor.close()
            return  self.__connection
        except psycopg2.Error as e:
            print(e)
            raise

    def close_connection(self):
        if  DBUtil.__connection is not None and  DBUtil.__connection.closed == 0:
             DBUtil.__connection.close()
             DBUtil.__connection = None
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
    print(query)

    return execute_query(query, params, fetch_one = True)