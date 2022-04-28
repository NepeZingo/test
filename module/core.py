from flask import Flask, request, redirect, url_for, Response
from werkzeug import serving
from flask_httpauth import HTTPBasicAuth
import logging
from logging.handlers import RotatingFileHandler
import ssl
import json
import os
import datetime

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username and password :
        if username == "jonathan" :
            return True
        else:
            return False
    else:
        return False

@app.route('/hello', methods=['GET'])
@auth.login_required
def hola_mundo():
    return Response('{"status": "OK", "message":"Hola Mundo!"}', mimetype = 'application/json')


if __name__ == '__main__':
    logging.basicConfig(filename='webservice.log',level=logging.DEBUG,format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
    serving.run_simple("0.0.0.0", 3000, app, ssl_context='adhoc', threaded=True)
