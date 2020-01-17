from .commands import *

def run(swarm):
    naaginSwarm = swarm
    setup_swarm(swarm)
    for naagin in naaginSwarm:
        naagin.pitch(0)
        naagin.yaw(55)
    time.sleep(2)
    driveAll(100, 100)
    time.sleep(10)
    stop()
    time.sleep(1)
