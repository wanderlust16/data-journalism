class Article(object):

    GENERIC   = 1
    HIGH_TEMP = 2
    LOW_TEMP  = 3
    HIGH_DUST = 4
    LOW_DUST  = 5
    CLOUDY    = 6

    def __init__(self, template, address, w_events, d_events, suntime):
        self.template = template
        self.address = address
        self.weather = w_events
        self.dust = d_events
        self.suntime = suntime

    def generate(self):
        if self.template == self.HIGH_TEMP:
            article = "오늘은 날씨가 덥겠습니다. {}시 현재 {}의 온도는 섭씨 {}도, 습도는 {}% 입니다. 미세먼지 수준은 {}(pm10={})입니다.".format(self.weather.time_observation.hour,
                                    self.address,
                                    self.weather.temp,
                                    self.weather.humidity,
                                    self.dust.dust_grade,
                                    self.dust.dust_value)
        elif self.template == self.LOW_TEMP:
            article = "{}월 {}일 {}시 현재, {}의 온도는 섭씨 {}도로 영하권의 추운 날씨가 계속되고 있습니다. 미세먼지 수준은 {}입니다.".format(self.weather.time_observation.month,
                                    self.weather.time_observation.day,
                                    self.weather.time_observation.hour,
                                    self.address,
                                    self.weather.temp,
                                    self.dust.dust_grade)
        elif self.template == self.HIGH_DUST:
            article = "오늘 미세먼지의 농도는 {}로 매우 높습니다. 불필요한 외출을 삼가하시기 바랍니다. 일출 시간은 {}, 일몰 시간은 {}입니다. 그러나 미세먼지 탓에 잘 안 보이겠네요! {}시 현재 {}의 온도는 섭씨 {}도입니다.".format(self.dust.dust_value,
                                    self.suntime.sunrise,
                                    self.suntime.sunset,
                                    self.weather.time_observation.hour,
                                    self.address,
                                    self.weather.temp)
        elif self.template == self.LOW_DUST:
            article = "{}월 {}일 {}시 현재, {}에서 측정한 미세먼지의 농도는 {}으로 '{}'수준입니다. 외출을 하시려면 반드시 마스크를 착용하세요. 일출 시간은 {}, 일몰 시간은 {}입니다. 그러나 미세먼지 탓에 잘 안 보이겠네요! 온도는 섭씨 {}도, 습도는 {}를 기록하고 있습니다.".format(self.weather.time_observation.month,
                                    self.weather.time_observation.day,
                                    self.weather.time_observation.hour,
                                    self.dust.location,
                                    self.dust.dust_value,
                                    self.dust.dust_grade,
                                    self.suntime.sunrise,
                                    self.suntime.sunset,
                                    self.weather.temp,
                                    self.weather.humidity)
        elif self.template == self.CLOUDY:
            article = "오늘의 구름량 {}%로 하늘이 흐리겠습니다. 일출 시간은 {}, 일몰 시간은 {}이지만, 짙은 구름 탓에 보기는 어렵겠네요!".format(self.weather.cloud,
                                    self.suntime.sunrise,
                                    self.suntime.sunset,)
        else: #GENERIC
            article = "{}월 {}일 {}시 현재, {}의 온도는 섭씨 {}도, 습도는 {}%, 미세먼지 수준은 {}(pm10={})입니다. 일출 시간은 {}, 일몰 시간은 {}입니다.".format(self.weather.time_observation.month,
                                    self.weather.time_observation.day,
                                    self.weather.time_observation.hour,
                                    self.address,
                                    self.weather.temp,
                                    self.weather.humidity,
                                    self.dust.dust_grade,
                                    self.dust.dust_value,
                                    self.suntime.sunrise,
                                    self.suntime.sunset)
        return article
