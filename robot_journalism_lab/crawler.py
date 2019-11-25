# -*- coding: utf-8 -*-
import urllib.request
from urllib import parse
import json

class Crawler(object):

    def __init__(self, city="Seoul", region=None):
        self.city = city      # e.g. 서울
        self.county = region    # e.g. 강남구

    def weather_fetch(self, city="Seoul"):
        self.city = city

        app_key = "781da3bc7b2aeb07cebe04999a760842"
        loc = self.city
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(loc, app_key)

        with urllib.request.urlopen(url) as response:
            self.weather_data = json.loads(response.read().decode("utf-8"))

        return self.weather_data

    def fine_dust_fetch(self, region=None):
        self.county = region

        app_key = "781da3bc7b2aeb07cebe04999a760842"
        loc = self.county
        url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName={}&dataTerm=month&pageNo=1&numOfRows=1&ServiceKey={}&ver=1.3&_returnType=json".format(
            parse.quote(loc), app_key)
        # print(url) # check REST url

        with urllib.request.urlopen(url) as response:
            self.fine_dust_data = json.loads(response.read().decode("utf-8"))

        return self.fine_dust_data

