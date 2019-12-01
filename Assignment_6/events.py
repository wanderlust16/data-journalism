import json
from datetime import datetime

class Events(object):

    WEATHER   = 1
    FINE_DUST = 2
    SUNTIME   = 3

    def __init__(self, data, event_type):
        self.data = data
        self.event_type = event_type

    def process_events(self):
        if self.event_type == self.WEATHER: 
            self.time_observation = datetime.fromtimestamp(self.data["dt"])
            self.temp = self.data["main"]["temp"] 
            self.temp_max = self.data["main"]["temp_max"]
            self.temp_min = self.data["main"]["temp_min"]
            self.humidity = self.data["main"]["humidity"]
            self.cloud = self.data["clouds"]["all"]

        if self.event_type == self.FINE_DUST:
            self.time_observation = datetime.strptime(self.data["list"][0]["dataTime"], "%Y-%m-%d %H:%M")
            self.dust_grade = self.data["list"][0]['pm10Grade']
            self.dust_value = self.data["list"][0]['pm10Value']
            self.location = self.data["parm"]["stationName"]

        if self.event_type == self.SUNTIME:
            self.time_observation = datetime.strptime(self.data["response"]["body"]["items"]["item"]["locdate"], "%Y%m%d")
            # self.time_observation = self.data["response"]["body"]["items"]["item"]["locdate"]
            self.sunrise = datetime.strptime(self.data["response"]["body"]["items"]["item"]["sunrise"], "%H%M").strftime("%H시 %M분")
            self.sunset = datetime.strptime(self.data["response"]["body"]["items"]["item"]["sunset"], "%H%M").strftime("%H시 %M분")

