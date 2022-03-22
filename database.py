
#!/usr/bin/env python

# -----------------------------------------------------------------------
# database.py
# Author: Nasko Tenev
# -----------------------------------------------------------------------

import sys
from sys import exit, stderr
from contextlib import closing
from sqlite3 import connect
from creditcard import CreditCard

from creditcard import CreditCard

#-----------------------------------------------------------------------

DATABASE_URL = 'file:reg.sqlite?mode=ro'

#-----------------------------------------------------------------------

def searchcards():
    '''Returns a list of all cards.'''
    print (searchquery.__doc__)
    try:
        with connect(DATABASE_URL, uri=True) as connection:
            cursor = connection.cursor()
            with closing(connection.cursor()) as cursor:

                # the string used to call the SQL commands
                # to extract specific elements from the database
                stmt_str="SELECT name, bank, annualfee, recommendedsc, "
                stmt_str+="bonus, pros, cons, details, apply "
                stmt_str+="FROM creditcards "
                # param = []

                stmt_str+="ORDER BY dept ASC, coursenum ASC, "
                stmt_str+="classid ASC "

                cursor.execute(stmt_str)
                line = cursor.fetchone()
                cards = []
                while line is not None:
                    card = CreditCard(line)
                    cards.append(card)
                    line = cursor.fetchone()
                return cards

    except Exception as ex:
        print(str(sys.argv[0]) + ": " + ex, file=stderr)
        exit(1)



def addcard():
    '''Inserts a new credit card into the database'''
    print (searchquery.__doc__)
    try:
        with connect(DATABASE_URL, uri=True) as connection:
            cursor = connection.cursor()
            with closing(connection.cursor()) as cursor:

                # the string used to call the SQL commands
                # to extract specific elements from the database
                stmt_str="INSERT INTO  "
                stmt_str+="bonus, pros, cons, details, apply "
                stmt_str+="FROM creditcards "
                # param = []

                stmt_str+="ORDER BY dept ASC, coursenum ASC, "
                stmt_str+="classid ASC "

                cursor.execute(stmt_str)
                line = cursor.fetchone()
                cards = []
                while line is not None:
                    card = CreditCard(line)
                    cards.append(card)
                    line = cursor.fetchone()
                return cards

    except Exception as ex:
        print(str(sys.argv[0]) + ": " + ex, file=stderr)
        exit(1)