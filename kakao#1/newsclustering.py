import re


def solution(str1, str2):
	# 대문자화
	str1 = str1.upper()
	str2 = str2.upper()

	# exception : divided by 0
	if str1 == str2:
		return 65536

	# 문자열 슬라이스
	a = []
	b = []
	p = re.compile('(.*)[^a-zA-Z](.*)')
	for i in range(0, len(str1) - 1):
		if (p.match(str1[i:i + 2])):    #특수문자 제외
			pass
		else:
			a.append(str1[i:i + 2])
	for j in range(0, len(str2) - 1):
		if (p.match(str2[j:j + 2])):    #특수문자 제외
			pass
		else:
			b.append(str2[j:j + 2])

	# 전체 원소 종류 집합
	seta = set(a)
	setb = set(b)
	unionset = seta | setb
	unredundant = list(unionset)

	# 최대|최소 갯수 구하기
	minnum = 0
	maxnum = 0
	for i in range(0, len(unredundant)):
		counta = a.count(unredundant[i])
		countb = b.count(unredundant[i])
		minnum = minnum + min(counta, countb)
		maxnum = maxnum + max(counta, countb)

	answer = (minnum / maxnum) * 65536
	return int(answer)

# str1      str2    answer
# FRANCE	french	16384
# handshake	shake hands	65536
# aa1+aa2	AAAA12	43690
# E=M*C^2	e=m*c^2	65536
