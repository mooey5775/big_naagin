import logging
import time

from big_naagin.naagin import Naagin

logging.basicConfig(level=logging.DEBUG)

naaginSwarm = []

def lockAll():
    for naagin in naaginSwarm:
        naagin.lock()


def unlockAll():
    for naagin in naaginSwarm:
        naagin.unlock()


def home():
    for naagin in naaginSwarm:
        naagin.pitch(0)
        naagin.yaw(0)


def driveAll(left_speed, right_speed):
    for naagin in naaginSwarm:
        naagin.tank(left_speed, right_speed)


def stop():
    for naagin in naaginSwarm:
        naagin.stop()
