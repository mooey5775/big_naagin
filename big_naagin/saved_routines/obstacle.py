from .commands import *

def run(swarm):
    naaginSwarm = swarm

    home()
    driveAll(50, 30)
    while naaginSwarm[-1].distance() > 45:
        pass
    naaginSwarm[-1].pitch(60)
    time.sleep(1)

    if naaginSwarm[-1].distance() < 100: # tall obstacle, swerve
        naaginSwarm[-1].pitch(0) # keep

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

    else: # short obstacle, climb
        driveAll(100, 90) # keep

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

if __name__ == "__main__":
    naagins = []
    for i in range(4):
        naagins.append(Naagin(i))

    run(naagins)