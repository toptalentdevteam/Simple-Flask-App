from os import system
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    title = "Query Customer IP Addresses"
    return render_template("index.html", title=title)

@app.route('/currentaddresses', methods=["POST"])
def currentaddresses():
    customername = request.form.get("systemid")
    title = "Customer IP Addresses"
    if customername == '':
        return render_template("nocustomer.html", title=title, customername=customername, error='You must provide a valid customername.')
    else:
        ###
        ### Code to login to firewall to get addresses
        ###
        
        ### This addresslist is a list of what I will eventually parse to
        addresslist = ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4']
        
        return render_template("currentaddresses.html", title=title, customername=customername, addresslist=addresslist)