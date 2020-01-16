import paho.mqtt.client as mqtt
from threading import Event
import logging

BROKER_ADDRESS = '35.243.178.248'

class PayloadContainer:
    def __init__(self):
        self.payload = None

class NaaginMqttClient:
    def __init__(self, address):
        self.callbacks = {}
        self.address = address

        self.client = mqtt.Client("big_naagin")
        self.client.on_message = self._create_message_callback()
        self.client.connect(self.address)
        self.client.subscribe('robot_return/#')
        self.client.loop_start()

    def _create_message_callback(self):
        def on_message(client, userdata, message):
            logging.debug('Received message')
            logging.debug(f'Topic: {message.topic}')
            logging.debug(message.payload.decode('utf-8'))

            try:
                naagin_id = int(message.topic.split('/')[1])

                for event, payload in self.callbacks[naagin_id]:
                    payload.payload = message.payload.decode('utf-8')
                    event.set()

                self.callbacks[naagin_id] = []
            except (ValueError, KeyError):
                pass

        return on_message

    def _register_callback(self, naagin_id, callback):
        self.callbacks.setdefault(naagin_id, []).append(callback)

    def command(self, naagin_id, cmd, message=''):
        logging.debug("Published message")
        logging.debug(f"Topic: robot_cmd/{naagin_id}/{cmd}")
        logging.debug(message)

        self.client.publish(f'robot_cmd/{naagin_id}/{cmd}',
                            str(message))

    def command_with_response(self, naagin_id, cmd, message=''):
        event = Event()
        payload = PayloadContainer()

        self._register_callback(naagin_id, (event, payload))
        self.command(naagin_id, cmd, message)
        event.wait()

        return payload.payload

naagin_client = NaaginMqttClient(BROKER_ADDRESS)
