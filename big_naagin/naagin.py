import time
from threading import Timer

from .client import naagin_client

# tank, left, right, pitch, yaw, home, distance, air

class Watchdog(Exception):
    def __init__(self, timeout, naagin_id, userHandler=None):  # timeout in seconds
        self.timeout = timeout
        self.naagin_id = naagin_id
        self.handler = userHandler if userHandler is not None else self.defaultHandler
        self.timer = Timer(self.timeout, self.handler)
        self.timer.start()

    def reset(self):
        self.timer.cancel()
        self.timer = Timer(self.timeout, self.handler)
        self.timer.start()

    def stop(self):
        self.timer.cancel()

    def defaultHandler(self):
        naagin_client.cancel_callback(self.naagin_id)

class Naagin:
    def __init__(self, naagin_id):
        self.id = naagin_id
        wdt = Watchdog(2, self.id)
        resp = naagin_client.command_with_response(self.id, 'air')
        self.aqs_present = (resp != 'nc')
        wdt.stop()

        if resp == 'cancelled':
            raise ValueError("Naagin failed to connect!")

        self.last_time = 0
        self.last_dist = 0

    def stop(self):
        naagin_client.command(self.id, 'tank', '0 0')

    def home(self):
        naagin_client.command(self.id, 'home')

    def lock(self):
        naagin_client.command(self.id, 'lock', '1')

    def unlock(self):
        naagin_client.command(self.id, 'lock', '0')

    def pitch(self, angle):
        if angle > 90 or angle < -45:
            raise ValueError("Invalid angle. Angle should be between -45 and 90")

        naagin_client.command(self.id, 'pitch', angle)

    def yaw(self, angle):
        if angle > 60 or angle < -60:
            raise ValueError("Invalid angle. Angle should be between -60 and 60")

        naagin_client.command(self.id, 'yaw', angle)

    def tank(self, left_speed, right_speed):
        if max(left_speed, right_speed) > 100 or min(left_speed, right_speed) < -100:
            raise ValueError("Invalid speed. Speed should be between -100 and 100")

        naagin_client.command(self.id, 'tank', f"{left_speed} {right_speed}")

    def left(self, speed):
        if speed > 100 or speed < -100:
            raise ValueError("Invalid speed. Speed should be between -100 and 100")

        naagin_client.command(self.id, 'left', speed)

    def right(self, speed):
        if speed > 100 or speed < -100:
            raise ValueError("Invalid speed. Speed should be between -100 and 100")

        naagin_client.command(self.id, 'left', speed)

    def distance(self):
        if time.time() - self.last_time < 0.25:
            # whoa! slow down!
            return self.last_dist

        resp = naagin_client.command_with_response(self.id, 'distance')
        self.last_dist = int(resp)
        self.last_time = time.time()
        return int(resp)

    def air_quality(self):
        if not self.aqs_present:
            raise TypeError("Air quality sensor not present on this Naagin!")

        resp = naagin_client.command_with_response(self.id, 'air')
        try:
            co2, tvoc = resp.split(' ')
            co2 = int(co2)
            tvoc = int(tvoc)
        except ValueError:
            raise ValueError("Air quality sensor data unavailable")

        return {'co2': co2, 'tvoc': tvoc}
