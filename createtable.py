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
                cursor.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

                # -------------------------------------------------------

                cursor.execute("DROP TABLE IF EXISTS creditcards;")
                cursor.execute("CREATE TABLE creditcards (name TEXT, bank TEXT,\
                 annualfee TEXT, recommendedcs TEXT, bonus TEXT, pros TEXT,\
                      cons TEXT, details TEXT, apply TEXT);")
                cursor.execute("insert into ambassadors (first, last, hs, state, email)\
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s);", 
                    ['Beta', 'Ambassador', 'Princeton High School', 'NJ',  'prefaceprojectdev@gmail.com'])

                # # -------------------------------------------------------

                # cursor.execute("DROP TABLE IF EXISTS appointments;")
                # cursor.execute("create table appointments\
                # (studentid NUMERIC, hsemail TEXT, apptdate TEXT, appttime \
                #     TIMESTAMP WITH TIME ZONE, weekday TEXT, meetinglink TEXT, selected BOOL,\
                #     cancelled BOOL, id uuid DEFAULT uuid_generate_v4 (), eventid TEXT);")

                # # -------------------------------------------------------

                # cursor.execute("DROP TABLE IF EXISTS students;")
                # cursor.execute("create table students\
                # (id NUMERIC, name TEXT, schoolid NUMERIC, hsemail TEXT);")

                # # -------------------------------------------------------

                # cursor.execute("DROP TABLE IF EXISTS schools;")
                # cursor.execute("create table schools\
                # (name TEXT, city TEXT, state TEXT, wkdays TEXT[], \
                #    timebegin TIMESTAMP WITH TIME ZONE, \
                #    timeend TIMESTAMP WITH TIME ZONE, id NUMERIC);")
                # cursor.execute("insert into schools (name, city, state, wkdays, timebegin, timeend, id)\
                #     values (%s, %s, %s, %s, %s, %s, %s);",
                #                ['Beta School', 'Princeton', 'NJ', [], None, None, '1234567'])

                # # -------------------------------------------------------

                # cursor.execute("DROP TABLE IF EXISTS liaisons;")
                # cursor.execute("create table liaisons\
                # (lfirst TEXT, llast TEXT, email TEXT, schoolid NUMERIC);")
                # cursor.execute("insert into liaisons (lfirst, llast, email, schoolid)\
                #     values (%s, %s, %s, %s);", ['Beta', 'Liaison', 'prefaceprojectdev@gmail.com',
                #                                 '1234567'])

                # # -------------------------------------------------------
                # cursor.execute("DROP TABLE IF EXISTS admins;")
                # cursor.execute("create table admins\
                #     (email TEXT, adminfirst TEXT, adminlast TEXT);")
                # cursor.execute("insert into admins (email, adminfirst, adminlast)\
                #     values (%s, %s, %s);", ['prefaceprojectdev@gmail.com', 'Beta',
                #                             'Admin'])

                # # -------------------------------------------------------
                # cursor.execute("DROP TABLE IF EXISTS ambassadorlogininfo;")
                # cursor.execute("create table ambassadorlogininfo\
                #     (email TEXT, pass BYTEA, code TEXT, created BOOL, date TEXT);")
                # cursor.execute("insert into ambassadorlogininfo (email, pass, code, created, date)\
                #     values (%s, %s, %s, %s, %s);", ['prefaceprojectdev@gmail.com', encode_password(BETA_PASSWORD),
                #                                     None, 'true', ''])

                # # -------------------------------------------------------
                # cursor.execute("DROP TABLE IF EXISTS liaisonlogininfo;")
                # cursor.execute("create table liaisonlogininfo\
                #     (email TEXT, pass BYTEA, code TEXT, created BOOL, date TEXT);")

                # # add initial liaison user
                # cursor.execute("insert into liaisonlogininfo (email, pass, code, created, date)\
                #     values (%s, %s, %s, %s, %s);", ['prefaceprojectdev@gmail.com', encode_password(BETA_PASSWORD),
                #                                     None, 'true', ''])

                # # -------------------------------------------------------

                # cursor.execute("DROP TABLE IF EXISTS adminlogininfo;")
                # cursor.execute("create table adminlogininfo\
                #     (email TEXT, pass BYTEA, code TEXT, created BOOL, date TEXT);")
                # # add initial admin user
                # cursor.execute("insert into adminlogininfo (email, pass, code, created, date)\
                #     values (%s, %s, %s, %s, %s);", ['prefaceprojectdev@gmail.com', encode_password(BETA_PASSWORD),
                #                                     None, 'true', ''])
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