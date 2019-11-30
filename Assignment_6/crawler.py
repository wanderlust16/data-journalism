# -*- coding: utf-8 -*-
import urllib.request
from urllib import parse
import xmltodict
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

        app_key = "8lIGqoS22kKzjgQfH6bZ7%2BwPTDBseufM2JRTbACt760ve%2BUAlMVkbhB1Qs9CgifiTKsAllvBikUfw9L5umSp7g%3D%3D"
        loc = self.county
        url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName={}&dataTerm=month&pageNo=1&numOfRows=1&ServiceKey={}&ver=1.3&_returnType=json".format(
            parse.quote(loc), app_key)
        # print(url) # check REST url

        with urllib.request.urlopen(url) as response:
            self.fine_dust_data = json.loads(response.read().decode("utf-8"))

        return self.fine_dust_data

    def suntime_fetch(self, city="서울", date="20191129"):
        self.city = city
        self.date = date

        app_key  = "8lIGqoS22kKzjgQfH6bZ7%2BwPTDBseufM2JRTbACt760ve%2BUAlMVkbhB1Qs9CgifiTKsAllvBikUfw9L5umSp7g%3D%3D"
        loc      = "서울"
        date     = "20191129"
        base_url = "http://apis.data.go.kr/B090041/openapi/service/RiseSetInfoService/getAreaRiseSetInfo?location={}&locdate={}&ServiceKey={}".format(parse.quote(loc), date, app_key).encode('utf-8')

        with urllib.request.urlopen(base_url.decode('ASCII')) as response:
            raw_data = response.read()
            json_data = json.dumps(xmltodict.parse(raw_data), indent=4)
            self.suntime_data = json.loads(json_data)

        return self.suntime_data