from flask import Flask, render_template
import threading

from .naagin import Naagin
app = Flask(__name__)

naagin_swarm = {}

@app.route("/")
def controls():
    return render_template("controls.html")

@app.route("/programs")
def programs():
    return render_template("programs.html", programList=["forward", "leftTurn", "rightTurn", "climb", "swerve", "obstacle"])

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
        elif command == "straightPitch":
            naaginBot.pitch(0)
        elif command == "down":
            naaginBot.pitch(-45)
        elif command == "leftYaw":
            naaginBot.yaw(-60)
        elif command == "straightYaw":
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

@app.route("/programs/<programName>")
def executeProgram(programName):    
    func = None
    if programName == "forward":
        pass
    elif programName == "leftTurn":
        pass
    elif programName == "rightTurn":
        pass
    elif programName == "climb":
        pass
    elif programName == "swerve":
        pass
    elif programName == "obstacle":
        pass
    # thread the function call
    if func is not None:
        t1 = threading.Thread(target=func, args=#naaginChain)
        t1.start()
    return "Ran program" + programName

def setup_app():
    for i in range(4):
        try:
            naagin_swarm[i] = Naagin(i)
        except ValueError:
            naagin_swarm[i] = None
            print(f"Naagin {i} is not working")