#!/usr/bin/env python

#-----------------------------------------------------------------------
# credit.py
# Authors: Nasko Tenev
#-----------------------------------------------------------------------

from sys import stderr
from creditcard import CreditCard
from flask import Flask, request, make_response
from flask import render_template
# from database import searchcards, addcard
# from database import searchquery, searchdetails

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


@app.route('/creditable', methods=['GET'])
def credit_card_table():
    '''Runs databse of credit cards page.'''

    # name = session.get('name')
    # bank = session.get('bank')
    # annualfee = session.get('aunf')
    # rcs = session.get('rcs')
    # bonus = session.get('bonus')
    # pros = session.get('pros')
    # cons = session.get('cons')
    # details = session.get('details')
    # link = session.get('apply')
    # advice = session.get('advice')

    # if name != "" and bank != "" and annualfee != "" and rcs != "" and\
    #      bonus != "" and pros != "" and cons != "" and details != ""\
    #          and link != "" and advice != "":
    #     list = [name, bank, annualfee, rcs, bonus, pros, cons]
    #     list.append(details)
    #     list.append(link)
    #     list.append(advice)
    #     card = CreditCard(list)
    #     addcard(card)

    # try:
    #     cards = searchcards()
    # except Exception as excpetion:
    #     print(excpetion, file=stderr)
    #     html = render_template('error.html')
    #     response = make_response(html)
    #     return response


    html = render_template('creditable.html', title = "Beginner Friendly Credit Cards")
    response = make_response(html)
    return response
