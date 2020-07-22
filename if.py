# https://wikidocs.net/7028 : 101~110
# https://wikidocs.net/7030 : 111~120
# https://wikidocs.net/7031 : 121~130

#101
# bool = True / False

#102
print(3==5)
# >> False

#103
print(3<5)
# >>True

#104
x = 4
print(1 < x < 5)
# >> True

#105
print((3 == 3)and(4 != 3))
# 1 and 1 >> True

#106
# => 는 지원하지 않는 연산자이다. 

#107
if 4<3:
    print("Hello World")

#108
if 4 < 3:
    print("Hello world")
else :
    print("Hi, there.")
# >> Hi, there.

#109
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
# >> 1 2 4

#110
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
# >> 3 5

#111
#a = input()
a = "안녕하세요"
print(a+a)

#112
#b = int(input("숫자를 입력하세요:"))
b = 30
print(b +10)

#113
#c = int(input("숫자를 입력하세요: "))
c = 30
if c%2==0:
    print("짝수")
else:
    print("홀수")

#114
#d = int(input("입력값: "))
d = 240
e = d+20
if e > 255:
    print(255)
else:
    print(e)

#115
#f = int(input("입력값: "))
f = 280
g = f-20
if g < 0:
    print("출력값: ", 0)
elif g > 255:
    print("출력값: ", 255)
else:
    print("출력값: ", g)

#116
#time = input("현재시간: ")
time = "03:00"
if time[-2:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")

#117
fruit = ['사과', '포도', '홍시']
#h = input("좋아하는 과일은? ")
h = "레몬"
if h in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

#118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
#i = input("종목명: ")
i = "커피베이"
if i in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

#119
fruit = {'봄':'딸기', '여름':'토마토', '가을':'사과'}
#j = input("제일 좋아하는 계절은 ")
j = "봄"
season = list(fruit.keys())
if j in season :
    print("정답입니다.")
else:
    print("오답입니다.")

#120
k = "한라봉"
season = list(fruit.values())
if k in season :
    print("정답입니다.")
else:
    print("오답입니다.")

#121
#a2 = input("")
a2 = "a"
if a2.islower():
    print(a2.upper())
else:
    print(a2)

#122
score = 83
print("grade is ", end = "")
if 0 <= score <21 :
    print("E")
elif 21 <= score <41:
    print("D")
elif 41 <= score <61:
    print("C")
elif 61 <= score <81:
    print("B")
else:
    print("A")

#123
dollars = "100 엔"
sp = dollars.split(" ")
if sp[1] == "달러":
    print(int(sp[0])*1167, '원')
elif sp[1] == "엔":
    print(int(sp[0])*1096, '원')
elif sp[1] == "유로":
    print(int(sp[0])*1268, '원')
elif sp[1] == "위안":
    print(int(sp[0])*171, '원')
else:
    print('알 수 없습니다.')

#124 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
n1, n2, n3 = 10, 9, 20
if n1 > n2 and n1 > n3 :
    print(n1)
elif n2 > n1 and n2 > n3 :
    print(n2)
else:
    print(n3)

#125 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
#number = input("휴대전화 번호 입력: ")
number = "011-345-1922"
num = number.split("-")[0]
if num == "011":
    com = "SKT"
elif num == "016":
    com = "KT"
elif num == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")

#126
post_num = "01400"
post = int(post_num[2])
if post == 0 or post == 1 or post == 2:
    print("강북구")
elif post == 3 or post == 4 or post == 5:
    print("도봉구")
elif post == 6 or post == 7 or post == 8 or post == 9:
    print("노원구")

#127 
주민번호 = "821010-1635210"
리스트 = list(주민번호.split('-'))
ch = int(리스트[1][0])
if ch == 1:
    print("남자")
else:
    print("여자")

#128
ch2 = int(리스트[1][1:3])
if 0 <= ch2 <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")

#129
num = "821010-1635210"
계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
        int(num[11])* 4 + int(num[12]) * 5
계산2 = 11 - (계산1 % 11)
계산3 = str(계산2)

if num[-1] == 계산3[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

#130

