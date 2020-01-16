from .client import naagin_client

# tank, left, right, pitch, yaw, home, distance, air

class Naagin:
    def __init__(self, naagin_id):
        self.id = naagin_id
        self.aqs_present = (naagin_client.command_with_response(self.id, 'air') != 'nc')

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
        resp = naagin_client.command_with_response(self.id, 'distance')
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
