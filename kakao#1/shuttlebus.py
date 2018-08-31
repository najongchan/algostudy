def solution(n, t, m, timetable):
	minutes = []
	first = 540  # 첫차시간
	con = 0
	for time in timetable:  # 분단위 계산
		a = time.split(':')
		minute = int(a[0]) * 60 + int(a[1])
		minutes.append(minute)
	minutes.sort()  # 대기자 정렬

	for i in range(0, n):  # 버스 운행
		count = 0  # 다음차 대기자 수
		for j in range(0, len(minutes)):  # 대기자수 계산
			if minutes[j] <= (first + (i * t)):
				count += 1
				if count == m:
					break

		if i == n - 1:  # 막차
			if count >= m:
				con = minutes[m - 1] - 1  # 막차마지막탑승
			else:
				con = first + (i * t)  # 막차시간탑승
			break
		else:  # 앞차 대기자 탑승
			if count >= m:
				minutes[:m] = []  # 정원 채워서 보내기
			else:
				minutes[:count] = []  # 대기자수 만큼 보내기

	hour = str(con // 60).zfill(2)  # hh
	minute = str(con % 60).zfill(2)  # MM

	answer = hour + ':' + minute
	return answer

# n : 운행횟수
# t : 배차간격
# m : 버스정원
# n t   m   timetable                    answer
# 1	1	5	[08:00, 08:01, 08:02, 08:03]	09:00
# 2	10	2	[09:10, 09:09, 08:00]	09:09
# 2	1	2	[09:00, 09:00, 09:00, 09:00]	08:59
# 1	1	5	[00:01, 00:01, 00:01, 00:01, 00:01]	00:00
# 1	1	1	[23:59]	09:00
# 10	60	45	[23:59,23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59, 23:59]	18:00
