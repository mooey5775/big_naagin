from .commands import *

def run(swarm):
    naaginSwarm = swarm
    home()
    time.sleep(2)
    driveAll(100, 90)
    time.sleep(10)
    stop()
    time.sleep(1)
