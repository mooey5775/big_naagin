from flask import Flask, render_template

import threading

from collections import deque
import time
import logging

from .naagin import Naagin

from .saved_routines import climb
from .saved_routines import commands
from .saved_routines import forward
from .saved_routines import obstacle
from .saved_routines import swerve
from .saved_routines import turnleft
from .saved_routines import turnright

app = Flask(__name__)

naagin_swarm = {}
current_order = [0, 1, 2, 3]
last_locks = deque(maxlen=3)
last_lock_time = 0

@app.route("/")
def controls():
    return render_template("controls.html")

def make_naagin_list():
    global current_order
    global naagin_swarm

    return [naagin_swarm[i] for i in current_order]

@app.route("/programs")
def programs():
    return render_template("programs.html", programList=["forward", "leftTurn", "rightTurn", "climb", "swerve", "obstacle"])

def run_lock(naaginId):
    global last_lock_time
    global current_order
    global last_locks
    if time.time() - last_lock_time > 60:
        last_locks.clear()

    last_lock_time = time.time()
    if naaginId in last_locks:
        return

    last_locks.append(naaginId)
    if len(last_locks) == 3:
        current_order = list(reversed(list(last_locks))) + [6 - sum(last_locks)]
    
    logging.debug(last_locks)
    logging.info(current_order)

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
            run_lock(naaginId)
            naaginBot.lock()
        elif command == "unlock":
            if naaginId in last_locks:
                last_locks.remove(naaginId)
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
        func = forward.run
    elif programName == "leftTurn":
        func = turnleft.run
    elif programName == "rightTurn":
        func = turnright.run
    elif programName == "climb":
        func = climb.run
    elif programName == "swerve":
        func = swerve.run
    elif programName == "obstacle":
        func = obstacle.run
    # thread the function call
    if func is not None:
        t1 = threading.Thread(target=func, args=(make_naagin_list(),))
        t1.start()
    return "Ran program" + programName

def setup_app():
    for i in range(4):
        try:
            naagin_swarm[i] = Naagin(i)
        except ValueError:
            naagin_swarm[i] = None
            print(f"Naagin {i} timed out on connection")
