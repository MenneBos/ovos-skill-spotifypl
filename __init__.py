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
        self.play_audio("/home/ovos/.venvs/ovos/lib/python3.11/site-packages/skill_ovos_melody/soundbytes/As_You_Wish.mp3", False) 

def create_skill():
    return SpotifyPLSkill()
