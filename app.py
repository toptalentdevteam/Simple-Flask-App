from flask import Flask, render_template, redirect, request, session
import requests
import json

app = Flask(__name__)
app.secret_key = "abc"  

@app.route('/')
def index():
    title = "Query Customer IP Addresses"
    return render_template("index.html", title=title)

@app.route('/currentaddresses', methods=["POST"])
def currentaddresses():
    customername = request.form.get("customername")
    title = "Customer IP Addresses"

    if customername == '':
        return render_template("nocustomer.html", title=title, customername=customername, error='You must provide a valid customername.')
    else:
        
        session['name'] = customername

        if customername == "perso1":
            addresslist = ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4']
        elif customername == "perso2":
            addresslist = ['5.5.5.5', '6.6.6.6', '7.7.7.7', '8.8.8.8']
        
        return render_template("currentaddresses.html", title=title, customername=customername, addresses=addresslist)

@app.route('/removeaddress', methods=['POST'])
def removeaddress():
    name = session['name']
    addressestoremove = []

    if name == 'perso1':
        addresslist = ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4']
    elif name == 'perso2':
        addresslist = ['5.5.5.5', '6.6.6.6', '7.7.7.7', '8.8.8.8']

    for i in addresslist:
        check = request.form.get('existing_' + i)

        if check != None:
            addressestoremove.append(i)

    print(name, addressestoremove)
    
    title = "Query Customer IP Addresses"
    return render_template('index.html')

@app.route('/additems', methods=["POST"])
def additems():
    name = session['name']
    addressestoadd = []

    for i in range(5):
        add = request.form.get('address' + str(i + 1))
        
        if add != '':
            addressestoadd.append(add)

    print(name, addressestoadd)   

    title = "Query Customer IP Addresses"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)