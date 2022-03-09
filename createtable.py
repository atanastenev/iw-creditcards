#!/usr/bin/env python

# -----------------------------------------------------------------------
# createtable.py
# Author: Nasko Tenev
# -----------------------------------------------------------------------

import hashlib
from sys import argv, stderr, exit
from contextlib import closing
from psycopg2 import connect
import os

# APP_SALT = os.environ['APP_SALT']
# POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
# BETA_PASSWORD = os.environ['BETA_PASSWORD']
# DATABASE_URL = os.environ['DATABASE_URL']

# -----------------------------------------------------------------------

def main():

    if len(argv) != 1:
        print('Usage: python create.py', file=stderr)
        exit(1)

    try:
        with connect(DATABASE_URL) as connection:

            with closing(connection.cursor()) as cursor:
                # cursor.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

                # -------------------------------------------------------

                cursor.execute("DROP TABLE IF EXISTS creditcards;")
                cursor.execute("CREATE TABLE creditcards (name TEXT, bank TEXT,\
                 annualfee TEXT, recommendedcs TEXT, bonus TEXT, pros TEXT,\
                      cons TEXT, details TEXT, apply TEXT);")
                cursor.execute("insert into ambassadors (first, last, hs, state, email)\
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s);", 
                    ['Beta', 'Ambassador', 'Princeton High School', 'NJ',  'prefaceprojectdev@gmail.com'])

                # # -------------------------------------------------------



                connection.commit()

    except Exception as ex:
        print(ex, file=stderr)
        exit(1)


def encode_password(password):
    # https://docs.python.org/3.5/library/hashlib.html
    password_bytes = password.encode()
    salt_bytes = APP_SALT.encode()

    return hashlib.pbkdf2_hmac('sha256', password_bytes, salt_bytes, 100567)

# -----------------------------------------------------------------------


if __name__ == '__main__':
    main()