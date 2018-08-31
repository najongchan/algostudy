import re
def solution(dartResult):
    # 세트 나누기
    result = re.findall('[0-9]+[S|D|T][#|*]*', dartResult)

    # 점수|보너스 계산
    setPoint = []
    p = re.compile('\d+')
    for point in result:
        option = ''
        number = int(p.findall(point)[0])
        if point[-1] == '#' or point[-1] == '*':
            option = point[-1]
            if point[-2] == 'D':
                number = number**2
            elif point[-2] == 'T':
                number = number**3
        else:
            if point[-1] == 'D':
                number = number**2
            elif point[-1] == 'T':
                number = number**3
        temp = [number, option]
        setPoint.append(temp)

    for i in range(0, len(setPoint)):
        if setPoint[i][1] == '#':
            setPoint[i][0] = setPoint[i][0] * (-1)
        elif setPoint[i][1] == '*':
            setPoint[i][0] = setPoint[i][0] * 2
            if i != 0:
                setPoint[i-1][0] = setPoint[i-1][0] * 2

    answer = 0
    for i in range(0, len(setPoint)):
        answer = answer + setPoint[i][0]

    return answer

# EXAMPLE => ANSWER
# "1S2D*3T" => 37
# "1D2S#10S" => 9
# "1D2S0T" => 3
# "1S*2T*3S" => 23
# "1D#2S*3S" => 5
# "1T2D3D#" => -4
# "1D2S3T*" => 59
