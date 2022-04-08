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

    # if name is not None and bank is not None  and annualfee is not None \
    #     and rcs is not None and bonus is not None and pros is not None \
    #         and cons is not None and details is not None \
    #          and link is not None  and advice is not None:
    #     list = [name, bank, annualfee, rcs, bonus, pros, cons]
    #     list.append(details)
    #     list.append(link)
    #     list.append(advice)
    #     card = CreditCard(list)
    #     addcard(card)

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


@app.route('/addcreditcard', methods=['GET', 'POST'])
def credit_card_table():

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
        line = [name, bank, annualfee, rcs, bonus, pros, cons, details, link, advice]
        try:
            card = CreditCard(line)
        except Exception as excpetion:
            print(excpetion, file=stderr)
            html = render_template('error.html')
            response = make_response(html)
            return response

    return make_response(redirect('/creditable'))
