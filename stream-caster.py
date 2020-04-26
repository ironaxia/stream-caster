import os
import time
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

# -------------------------------------------------------

def get_content(url):
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    return soup

def check_internet():
    url = 'http://www.google.com/'
    timeout = 5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No Internet connexion.")
    return False

# app=Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("home.html")

# @app.route('/about/')
# def about():
#     return render_template("about.html")

# @app.route('/contact/')
# def contact():
#     return render_template("contact.html")

# @app.route('/success/<name>/<score>')
# def success(name, score):
#     return render_template("success.html")

# @app.route('/login', methods = ['POST'])
# def login():
#     return render_template("login.html")


if __name__ == "__main__":
    # app.run(debug=True)
