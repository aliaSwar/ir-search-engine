from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html', hello='Hello World!')
