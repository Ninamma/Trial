from flask import Flask, render_template, request
from APIs import Adapter
app = Flask("MyApp")

@app.route("/")
def home():
    return render_template("northamerica.html", entries = Adapter.final_adapter('assets AND "north america"'))
    #return render_template("index.html")

#@app.route("/northamerica")
#def northamerica():
#    return render_template("northamerica.html", entries = Adapter.final_adapter('assets AND "north america"'))

#@app.route("/southamerica")
#def southamerica():
#    return render_template("southamerica.html", entries = Adapter.final_adapter('assets AND "south america"'))

#@app.route("/europe")
#def europe():
#    return render_template("europe.html", entries = Adapter.final_adapter('assets AND europe'))

#@app.route("/africa")
#def africa():
#    return render_template("africa.html", entries = Adapter.final_adapter('assets AND africa'))

#@app.route("/asia")
#def asia():
#    return render_template("asia.html", entries = Adapter.final_adapter('assets AND asia'))

#@app.route("/australia")
#def australia():
#    return render_template("australia.html", entries = Adapter.final_adapter('assets AND australia'))


if __name__ == '__main__':
    app.run(debug = True)
