from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

def execute_query(query, params = None, fetch_one = False, fetch_all = False):
    try:
        result = db.session.execute(text(query), params or ())
        db.session.commit()

        if query.strip().upper().startswith(('UPDATE','DELETE')):
            return result.rowcount

        if fetch_one:
            return result.fetchone()
        
        if fetch_all:
            return result.fetchall()
        
        return result
    
    except Exception as e:
        db.session.rollback()
        raise e