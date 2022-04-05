#!/usr/bin/env python

#-----------------------------------------------------------------------
# credit.py
# Authors: Nasko Tenev
#-----------------------------------------------------------------------

from sys import stderr
from flask import Flask, request, make_response
from flask import render_template
from database import searchcards
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

    # name = session.get('')
    
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
