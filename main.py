from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return '<h1>Olá Flask!</h1>'

app.run()
