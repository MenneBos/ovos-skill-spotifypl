from ovos_workshop.skills.ovos import OVOSSkill
from ovos_bus_client.message import Message
import os
import requests

class SpotifyPLSkill(OVOSSkill):
    def __init__(self):
        super().__init__("SpotifyPLSkill")

    def initialize(self):
        self.add_event('mycroft.spotifypl.play', self.handle_play_spotifypl)
        self.register_intent_file('PlaySpotifyPL.intent', self.handle_play_spotifypl)

    def handle_play_spotifypl(self, message: Message):
        url = f"http://192.168.1.45/api/manager/logic/webhook/Terre/?tag=SpotifyPL"
        data = requests.get(url)
        print(data.json())

def create_skill():
    return SpotifyPLSkill()
