from crawler import Crawler
from events import Events
from mood_detect import Mood
from article import Article

crawler = Crawler()

# 데이터 수집
weather_data = crawler.weather_fetch()
fine_dust_data = crawler.fine_dust_fetch("관악구")

print(weather_data)
print(fine_dust_data)

# 날씨 이벤트 처리
weather_events = Events(weather_data, Events.WEATHER)
weather_events.process_events()

# 미세먼지 이번트 처리
dust_events = Events(fine_dust_data, Events.FINE_DUST)
dust_events.process_events()

# 데이터 체크
print(weather_events.temp)
print(dust_events.dust_grade)


# Mood detection을 위한 날씨 정보 데이터 구축
weather_info = (weather_events.temp, dust_events.dust_value)
address = dust_events.location

# Mood decision
mood = Mood()
template = mood.decision(weather_info)
print(template)

# 기사 생성
article = Article(template, address, weather_events, dust_events)
print(article.generate())
