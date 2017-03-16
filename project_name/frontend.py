from flask import Flask, request, render_template, g

# from core.models import Website, Page, Product

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return "hello world"