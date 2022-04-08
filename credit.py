#!/usr/bin/env python

#-----------------------------------------------------------------------
# credit.py
# Authors: Nasko Tenev
#-----------------------------------------------------------------------

from sys import stderr
from creditcard import CreditCard
from flask import Flask, redirect, session
from flask import render_template, make_response
from database import searchcards, addcard

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')

#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    '''Runs orgin page.'''
    print (index.__doc__)

    html = render_template('index.html', title = "IW09 - Learn All About Credit Cards")
    response = make_response(html)
    return response


@app.route('/creditable', methods=['GET', 'POST'])
def credit_card_table():
    '''Runs databse of credit cards page.'''

    adminpass = "AdminCreditPost"

    name = session.get('name')
    bank = session.get('bank')
    annualfee = session.get('aunf')
    rcs = session.get('rcs')
    bonus = session.get('bonus')
    pros = session.get('pros')
    cons = session.get('cons')
    details = session.get('details')
    link = session.get('apply')
    advice = session.get('advice')
    key = session.get('key')

    if key is adminpass:
        print("key is correct")
        line = [name, bank, annualfee, rcs, bonus, pros, cons, details, link, advice]
        try:
            print("about to add card")
            card = CreditCard(line)
            addcard(card)
        except Exception as excpetion:
            print(excpetion, file=stderr)
            html = render_template('error.html')
            response = make_response(html)
            return response

    try:
        cards = searchcards()
    except Exception as excpetion:
        print(excpetion, file=stderr)
        html = render_template('error.html')
        response = make_response(html)
        return response


    html = render_template('creditable.html', cards=cards, title = "Beginner Friendly Credit Cards")
    response = make_response(html)
    return response


# @app.route('/addcreditcard', methods=['POST'])
# def add_credit_card():

#     adminpass = "AdminCreditPost"

#     name = session.get('name')
#     bank = session.get('bank')
#     annualfee = session.get('aunf')
#     rcs = session.get('rcs')
#     bonus = session.get('bonus')
#     pros = session.get('pros')
#     cons = session.get('cons')
#     details = session.get('details')
#     link = session.get('apply')
#     advice = session.get('advice')
#     key = session.get('key')

#     if key is adminpass:
#         print("key is correct")
#         line = [name, bank, annualfee, rcs, bonus, pros, cons, details, link, advice]
#         try:
#             print("about to add card")
#             card = CreditCard(line)
#             addcard(card)
#         except Exception as excpetion:
#             print(excpetion, file=stderr)
#             html = render_template('error.html')
#             response = make_response(html)
#             return response

#     return make_response(redirect('/creditable'))
