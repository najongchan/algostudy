def solution(cacheSize, cities):
	cache = [''] * cacheSize
	time = 0

	try:
		for city in cities:
			city = city.upper()
			if cache.count(city) == 0:  # miss
				cache.pop()
				time += 5
			else:  # hit
				cache.remove(city)
				time += 1
			cache.insert(0, city)
	except:  # 캐시사이즈 = 0 or cities =  0
		time = len(cities) * 5
	answer = time
	return answer

# cachesize input   answer
# 3	[Jeju, Pangyo, Seoul, NewYork, LA, Jeju, Pangyo, Seoul, NewYork, LA]	50
# 3	[Jeju, Pangyo, Seoul, Jeju, Pangyo, Seoul, Jeju, Pangyo, Seoul]	21
# 2	[Jeju, Pangyo, Seoul, NewYork, LA, SanFrancisco, Seoul, Rome, Paris, Jeju, NewYork, Rome]	60
# 5	[Jeju, Pangyo, Seoul, NewYork, LA, SanFrancisco, Seoul, Rome, Paris, Jeju, NewYork, Rome]	52
# 2	[Jeju, Pangyo, NewYork, newyork]	16
# 0	[Jeju, Pangyo, Seoul, NewYork, LA]  25
