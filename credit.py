#!/usr/bin/env python

#-----------------------------------------------------------------------
# credit.py
# Authors: Nasko Tenev
#-----------------------------------------------------------------------

from sys import stderr
from flask import Flask, request, make_response
from flask import render_template
# from database import searchquery, searchdetails

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')

#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    '''Runs orgin page.'''
    print (index.__doc__)

    html = render_template('index.html')
    response = make_response(html)
    return response
