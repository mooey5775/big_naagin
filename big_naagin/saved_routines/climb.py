from commands import *

def run(swarm):
    naaginSwarm = swarm
    home()
    driveAll(100, 90)

    while naaginSwarm[-1].distance() > 45:
        pass

    naaginSwarm[-1].pitch(60) # nose up
    time.sleep(1)
    naaginSwarm[-1].pitch(-40) # clear nubs one at a time
    naaginSwarm[-2].pitch(40)
    time.sleep(1)
    naaginSwarm[-1].pitch(0)
    naaginSwarm[-2].pitch(-40)
    naaginSwarm[-3].pitch(40)
    time.sleep(1)
    naaginSwarm[-2].pitch(0)
    naaginSwarm[-3].pitch(-40)
    naaginSwarm[-4].pitch(40)
    time.sleep(1)
    naaginSwarm[-1].pitch(30) # pitch up to keep the nose off the ground
    naaginSwarm[-3].pitch(0)
    naaginSwarm[-4].pitch(-40)
    time.sleep(1)
    naaginSwarm[-1].pitch(0)
    naaginSwarm[-4].pitch(0)
    time.sleep(1)
    stop()
    time.sleep(1)
