from flask import Flask, render_template

from .naagin import Naagin
app = Flask(__name__)

naagin_swarm = {}

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
        naaginBot = naagin_swarm[naaginId]
        if command == "forwards":
            naaginBot.tank(50, 50)
        elif command == "left":
            naaginBot.tank(-75, 125)
        elif command == "right":
            naaginBot.tank(125, -75)
        elif command == "backwards":
            naaginBot.tank(-50, -50)
        elif command == "lock":
            naaginBot.lock()
        elif command == "unlock":
            naaginBot.unlock()
        elif command == "up":
            naaginBot.pitch(45)
        elif command == "down":
            naaginBot.pitch(-45)
        elif command == "leftYaw":
            naaginBot.yaw(-60)
        elif command == "straight":
            naaginBot.yaw(0)
        elif command == "rightYaw":
            naaginBot.yaw(60)
        elif command == "home":
            naaginBot.home()
        else:
            naaginBot.stop()
    except:
        return "Error"
    return "Okay"

def setup_app():
    for i in range(4):
        try:
            naagin_swarm[i] = Naagin(i)
        except ValueError:
            naagin_swarm[i] = None