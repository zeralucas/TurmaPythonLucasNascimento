from flask import Flask, render_template, request, redirect


app = Flask(__name__)
@app.route("/")
def Inicio():
    return render_template("trabalho.html")

app.run()