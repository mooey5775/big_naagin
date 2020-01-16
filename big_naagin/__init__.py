from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def controls():
    return render_template("controls.html")

@app.route("/programs")
def programs():
    return "KJ has to do this"

@app.route("/<naaginId>/<command>")
def executeCommand(naaginId, command):
    try:
        naaginId = int(naaginId)
        
    except:
        return "Error"
    return "Okay"