#!/usr/bin/env python3

from flask import Flask
def app():
  return "My app!"

@app.route('/')
def index():
    return '<h1>Welcome to my app!</h1>'
app = Flask(__name__)
