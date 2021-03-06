#!/usr/bin/env python

# -----------------------------------------------------------------------
# createtable.py
# Author: Nasko Tenev
# -----------------------------------------------------------------------

from sys import argv, stderr, exit
from contextlib import closing
from psycopg2 import connect
import os

# APP_SALT = os.environ['APP_SALT']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
BETA_PASSWORD = os.environ['BETA_PASSWORD']
DATABASE_URL = os.environ['DATABASE_URL']

# -----------------------------------------------------------------------

def main():

    if len(argv) != 1:
        print('Usage: python create.py', file=stderr)
        exit(1)
    print("call too database")
    try:
        with connect(DATABASE_URL) as connection:

            with closing(connection.cursor()) as cursor:
                # cursor.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
                print("connect database")
                # -------------------------------------------------------

                pros = "No annual fee; Qualify with limited/bad credit;\n \
                    Bonus categories; Intro APR period; \
                        Reports to the three major credit bureaus"
                cons = "complicated awards"

                details = "0\%\ intro APR on Purchases for 6 months and 10.99\%\ intro APR on Balance Transfers for 6 months"

                link = "https://www.discover.com/products/student-it-af.html?sc=RJUK&cmpgnid=ls-dca-ir-student-it-RJUK-dtop-980&irgwc=1&gclid=_srytbrlzfokf63ubmv30kbtmsv2xtliknf3jh9zp00&sid=04664157&pid=170911&aid=568217&source=Affiliates&sku=110"

                cursor.execute("DROP TABLE IF EXISTS creditcards;")
                cursor.execute("CREATE TABLE creditcards (name TEXT, bank TEXT,\
                 annualfee TEXT, recomcs TEXT, bonus TEXT, pros TEXT,\
                      cons TEXT, details TEXT, apply TEXT, advice TEXT);")
                print("database created?")
                
                cursor.execute("insert into creditcards (name, bank, annualfee, recomcs, bonus,\
                    pros, cons, details, apply, advice)\
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", 
                    ['Sample Name', 'Sample Bank', '$0', '0-600',  'Sample Bonus', 
                        'No pros', 'No cons', 'No details', 'No link', 'Sample advice'])
                print("first card added")
                cursor.execute("insert into creditcards (name, bank, annualfee, recomcs, bonus,\
                    pros, cons, details, apply, advice)\
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", 
                    ['DiscoverIt', 'Discover', '0', '630-689',  'Cashback Match, 5\%\ cashback, etc.', 
                        pros, cons, details, link, 'Make sure to put a realistic income when applying for this card'])
                print("new cards added")
                stmt_str="SELECT name, bank, annualfee, recomcs, "
                stmt_str+="bonus, pros, cons, details, apply, advice "
                stmt_str+="FROM creditcards "

                cursor.execute(stmt_str)
                line = cursor.fetchone()
                print(line)
                connection.commit()
                print("after commit")

    except Exception as ex:
        print(ex, file=stderr)
        exit(1)


# def encode_password(password):
#     # https://docs.python.org/3.5/library/hashlib.html
#     password_bytes = password.encode()
#     salt_bytes = APP_SALT.encode()

#     return hashlib.pbkdf2_hmac('sha256', password_bytes, salt_bytes, 100567)

# -----------------------------------------------------------------------


if __name__ == '__main__':
    main()