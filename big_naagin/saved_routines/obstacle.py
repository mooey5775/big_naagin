from .commands import *

def run(swarm):
    naaginSwarm = swarm
    setup_swarm(swarm)

    home()
    driveAll(50, 30)
    while naaginSwarm[-1].distance() > 45:
        pass
    naaginSwarm[-1].pitch(60)
    time.sleep(1)

    if naaginSwarm[-1].distance() < 100: # tall obstacle, swerve
        pass
    else: # short obstacle, climb
        driveAll(100, 90)