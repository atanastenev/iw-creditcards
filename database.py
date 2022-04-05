
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
import os

#-----------------------------------------------------------------------

#DATABASE_URL = os.environ['DATABASE_URL']

#-----------------------------------------------------------------------

def searchcards():
    '''Returns a list of all cards.'''
    try:
        with connect(DATABASE_URL) as connection:
            with closing(connection.cursor()) as cursor:

                # the string used to call the SQL commands
                # to extract specific elements from the database
                stmt_str="SELECT name, bank, annualfee, recommendedsc, "
                stmt_str+="bonus, pros, cons, details, apply, advice "
                stmt_str+="FROM creditcards "

                cursor.execute(stmt_str)
                line = cursor.fetchone()
                cards = []
                while line is not None:
                    card = CreditCard(line)
                    cards.append(card)
                    line = cursor.fetchone()
                return cards

    except Exception as ex:
        print(str(sys.argv[0]) + ": " + str(ex), file=stderr)
        exit(1)



def addcard(card):
    '''Inserts a new credit card into the database'''
    try:
        with connect(DATABASE_URL) as connection:
            with closing(connection.cursor()) as cursor:

                # the string used to call the SQL commands
                # to extract specific elements from the database
                stmt_str="INSERT INTO creditcards (name, bank,\
                 annualfee, recomcs, bonus, pros,\
                      cons, details, apply, advice) values \
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                credicard_values = [card.get_name(),card.get_bank()]
                credicard_values += [card.get_afee(),card.get_creditscore()]
                credicard_values += [card.get_bonus(),card.get_pros(),card.get_cons()]
                credicard_values += [card.get_details(), card.get_link(), card.get_advice()]
                
                cursor.execute(stmt_str, credicard_values)
                line = cursor.fetchone()
                cards = []
                while line is not None:
                    card = CreditCard(line)
                    cards.append(card)
                    line = cursor.fetchone()
                return cards

    except Exception as ex:
        print(str(sys.argv[0]) + ": " + str(ex), file=stderr)
        exit(1)