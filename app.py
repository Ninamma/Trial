from flask import Flask
app = Flask("MyApp")

@app.route("/")
def home():
    return '<h1>will this finaly work??</h1>'

if __name__ == '__main__':
    app.run(debug = True)
