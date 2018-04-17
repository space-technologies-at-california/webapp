import random, sys
from functools import wraps
from hashlib import sha256
import database
from flask import *

def generate_salt():
    return '{:030x}'.format(random.randrange(16**30))

def generate_session_id():
    return '{:090x}'.format(random.randrange(16**90))

def check_login(username, password):
    username = database.escape(username)
    res = database.fetchone("SELECT hash, salt FROM users WHERE username='{}';".format(username))
    if res is None: return False
    correct_hash, salt = res
    hashed_password = sha256("{}{}".format(salt, password).encode()).hexdigest()
    return correct_hash == hashed_password

def is_valid_username(username):
    username = database.escape(username)
    return bool(database.fetchone("SELECT 1 FROM users WHERE username='{}';".format(username)))

def get_username_from_session():
    session = request.cookies.get('SESSION_ID', '')
    session = database.escape(session)
    found_session = database.fetchone("SELECT username FROM sessions WHERE id='{}';".format(session))
    username = found_session[0] if found_session else None
    return username

def get_username(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        username = get_username_from_session()
        return f(username, *args, **kwargs)
    return decorated_function

# Assume for the actual site, this is replaced by the actual URL.
SERVER_NAME = ['127.0.0.1:5000/', 'stac.berkeley.edu']

def csrf_protect(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        referer = request.headers.get('Referer')
        if referer:
            if SERVER_NAME[0] not in referer and SERVER_NAME[1] not in referer:
                print('Potential CSRF blocked', file=sys.stderr)
                return 'Potential CSRF blocked', 403
        return f(*args, **kwargs)
    return decorated_function
