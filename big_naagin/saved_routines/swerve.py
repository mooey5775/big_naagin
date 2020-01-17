from commands import *

def run(swarm):
    naaginSwarm = swarm
    home()
    driveAll(50, 30)

    while naaginSwarm[-1].distance() > 45:
        pass

    driveAll(25, 25)
    naaginSwarm[-1].yaw(50)
    time.sleep(0.6)
    naaginSwarm[-2].yaw(50)
    time.sleep(0.6)
    naaginSwarm[-1].yaw(0)
    naaginSwarm[-3].yaw(50)
    time.sleep(0.6)
    naaginSwarm[-1].yaw(-60)
    naaginSwarm[-2].yaw(0)
    naaginSwarm[-4].yaw(50)
    time.sleep(0.6)
    naaginSwarm[-1].yaw(0)
    naaginSwarm[-2].yaw(-50)
    naaginSwarm[-3].yaw(0)
    time.sleep(0.6)
    naaginSwarm[-2].yaw(0)
    naaginSwarm[-3].yaw(-50)
    naaginSwarm[-4].yaw(0)
    time.sleep(0.6)
    naaginSwarm[-3].yaw(0)
    naaginSwarm[-4].yaw(-50)
    time.sleep(0.6)
    naaginSwarm[-4].yaw(0)
    home()
    stop()
    time.sleep(1)
