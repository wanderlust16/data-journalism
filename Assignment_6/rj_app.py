# -*- coding: utf-8 -*-
from crawler import Crawler
from events import Events
from mood_detect import Mood
from article import Article

crawler = Crawler()
# 데이터 수집
weather_data = crawler.weather_fetch()
fine_dust_data = crawler.fine_dust_fetch("관악구")
suntime_data = crawler.suntime_fetch()

# print(weather_data)
# print(fine_dust_data)
# print(suntime_data)

# 날씨 이벤트 처리
weather_events = Events(weather_data, Events.WEATHER) # weather_data를 Event에 파라미터로 던져줌
weather_events.process_events()

# 미세먼지 이번트 처리
dust_events = Events(fine_dust_data, Events.FINE_DUST) # fine_dust_data를 Event에 파라미터로 던져줌
dust_events.process_events()

# 일출일몰 이벤트 처리
suntime_events = Events(suntime_data, Events.SUNTIME)
suntime_events.process_events()

# 데이터 체크
# print(weather_events.temp)
# print(weather_events.cloud)
# print(dust_events.dust_grade)
# print(suntime_events.sunrise)


# Mood detection을 위한 날씨 정보 데이터 구축
weather_info = (weather_events.temp, dust_events.dust_value, weather_events.cloud)
address = dust_events.location

# Mood decision
mood = Mood()
template = mood.decision(weather_info)
# print(template)

# 기사 생성
article = Article(template, address, weather_events, dust_events, suntime_events)
print(article.generate())
