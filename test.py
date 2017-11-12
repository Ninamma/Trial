from flask import Flask,
app = Flask("MyApp")

@app.route("/")
def home():
    return '<h1>will this finaly work??</h1>'

app.run(debug = True)
