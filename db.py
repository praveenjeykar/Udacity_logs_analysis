from contextlib import contextmanager
import psycopg2

@contextmanager
def db_session_context(db_name):
    """
    Context manager that yields a db connection and
    ensures it is properly closed when out of scope
    """
    try:
        db = psycopg2.connect(database=db_name)
        yield db
    finally:
        db.close()
