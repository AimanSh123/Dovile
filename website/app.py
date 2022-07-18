from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pandas as pd

df = pd.read_csv('dataset.csv')
df2 = pd.read_csv('dataset.csv')

def filter_data(df, col, value):
    return df[df[col] == value]

#create a flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/male')
def male():
    global df2
    global df
    df2 = filter_data(df,"gender", "Men")
    return render_template("male.html")

@app.route('/female')
def female():
    global df2
    global df
    df2 = filter_data(df,"gender", "Women")
    return render_template("female.html")

@app.route('/Mapparel')
def Mapparel():
    global df2
    global df
    df2 = filter_data(df,"masterCategory", "Apparel")
    return render_template("Mapparel.html")

@app.route('/Mfootwear')
def Mfootwear():
    global df2
    global df
    df2 = filter_data(df,"masterCategory", "Footwear")
    return render_template("Mapparel.html")

@app.route('/Maccessories')
def Maccessories():
    global df2
    global df
    df2 = filter_data(df,"masterCategory", "Accessories")
    return render_template("Mapparel.html")

@app.route('/Fapparel')
def Fapparel():
    global df2
    global df
    df2 = filter_data(df,"masterCategory", "Apparel")
    return render_template("Fapparel.html")

@app.route('/Ffootwear')
def Ffootwear():
    global df2
    global df
    df2 = filter_data(df,"masterCategory", "Footwear")
    return render_template("Fapparel.html")

@app.route('/Faccessories')
def Faccessories():
    global df2
    global df
    df2 = filter_data(df,"masterCategory", "Accessories")
    return render_template("Fapparel.html")

@app.route('/socks')
def socks():
    global df2
    global df
    df2 = filter_data(df,"subCategory", "Socks")
    return render_template("socks.html")

@app.route('/wallets')
def wallets():
    global df2
    global df
    df2 = filter_data(df,"subCategory", "Wallets")
    return render_template("wallets.html")

@app.route('/bags')
def bags():
    global df2
    global df
    df2 = filter_data(df,"subCategory", "Bags")
    return render_template("bags.html")

#main
if __name__ == '__main__':
    app.run(debug=True)
    app.run()

