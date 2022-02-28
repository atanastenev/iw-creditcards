#!/usr/bin/env python

#-----------------------------------------------------------------------
# runserver.py
# Authors: Ari Riggins and Nasko Tenev
#-----------------------------------------------------------------------

import argparse
from sys import argv, exit, stderr
# from classsearch import app

#-----------------------------------------------------------------------

# adding a new argparse argument for the port argument
parser = argparse.ArgumentParser(description=
  'Server for the registrar application', allow_abbrev = False)
parser.add_argument('port', type = int,
  help = 'the port at which the server should listen')
args = parser.parse_args()

#-----------------------------------------------------------------------

def main():

    if len(argv) != 2:
        print('Usage: ' + argv[0] + ' port', file=stderr)
        exit(2)

    try:
        port = int(argv[1])
    except Exception:
        print('Port must be an integer.', file=stderr)
        exit(2)


    try: # app is a funciton that does the website programming
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as ex:
        print(ex, file = stderr) # fix this error see what it has to be?
        exit(2)

if __name__ == '__main__':
    main()