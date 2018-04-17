import sqlite3
import sys
from functools import wraps
import os

real_root_path = os.path.dirname(os.path.realpath(__file__)) + "/"

DATABASE_FILE = real_root_path + 'db'
# DATABASE_FILE = ':memory:'
conn = sqlite3.connect(DATABASE_FILE)

# def query_logger(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         print("Executing query", *args, file=sys.stderr)
#         try:
#             return f(*args, **kwargs)
#         except sqlite3.Error as e:
#             print("SQL Error Occurred:", e.args[0], file=sys.stderr)
#     return decorated_function

# @query_logger
def execute(query):
    with conn:
        conn.executescript(query)

# @query_logger
def fetchone(query):
    with conn:
        return conn.execute(query).fetchone()

# @query_logger
def fetchall(query):
    with conn:
        return conn.execute(query).fetchall()

def make_escaper(replacements):
    def escaper(inp):
        for old, new in replacements.items():
            inp = inp.replace(old, new)
        return inp
    return escaper

escape_sql = make_escaper({
    ';': '\;',
    "'": "''",
    '--': '&ndash;',
    '*': '&#42;',
})

escape_html = make_escaper({
    '<': '&lt;',
    '>': '&gt;'
})

def escape(v):
    return escape_html(escape_sql(v))


