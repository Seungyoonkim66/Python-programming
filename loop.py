# https://wikidocs.net/78562 : 131~140
# https://wikidocs.net/7020 : 141~150
# https://wikidocs.net/78768 : 151~160
# https://wikidocs.net/7033 : 161~170
# https://wikidocs.net/25315 : 171~180
# https://wikidocs.net/78564 : 181~190
# https://wikidocs.net/78565 : 191~200

#131
과일 = ["사과", "귤", "수박"]
for i in 과일 :
    print(i)

#132
for i in 과일 :
    print("####")

#133
for 변수 in ["A", "B", "C"]:
  print(변수)

#134
print("출력: A")
print("출력: B")
print("출력: C")

#135
# for 변수 in ["A", "B", "C"]:
#   b = 변수.lower()
#   print("변환:", b)
print("변환: a")
print("변환: b")
print("변환: c")

#136
for i in [10, 20, 30]:
    print("변수: ", i)

#137
for i in [10,20,30]:
    print(i)

#138
for i in [10,20,30]:
    print(i)
    print("--------")

#139
print("++++")
for i in [10,20,30]:
    print(i)

#140
for i in range(1,5):
    print("------")

#141
리스트 =  [100,200,300]
for i in 리스트:
    print(i)

#142
리스트2 = ["김밥", "라면", "튀김"]
for i in 리스트2:
    print("오늘의 메뉴:", i)

#143
리스트3 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트3:
    print(len(i))

#144
리스트4 = ['dog', 'cat', 'parrot']
for i in 리스트4:
    print(i, len(i))

#145
for i in 리스트4:
    print(i[0])

#146
리스트5 = [1, 2, 3]
for i in 리스트5:
    print("3 x", i)

#147
for i in 리스트5:
    print("3 x", i,"=", 3*i)

#148
리스트6 = ["가", "나", "다", "라"]
for i in 리스트6[1:4]:
    print(i)

#149
for i in 리스트6[::2]:
    print(i)

#150
for i in 리스트6[::-1]:
    print(i)

#151
리스트7 = [3, -20, -3, 44]
for i in 리스트7:
    if i<0:
        print(i)
    else:
        pass

#152
리스트k = [3, 100, 23, 44]
for 변수 in 리스트k:
  if 변수 % 3 == 0:
    print(변수)

#153
리스트8 = [13, 21, 12, 14, 30, 18]
for i in 리스트8:
    if i%3==0 and i<20:
        print(i)
    
#154
리스트9 = ["I", "study", "python", "language", "!"]
for i in 리스트9:
    if len(i)>=3:
        print(i)

#155
리스트10 = ["A", "b", "c", "D"]
for i in 리스트10:
    if i.isupper():
        print(i)
    
#156
for i in 리스트10:
    if i.islower():
        print(i)

#157
리스트11 = ['dog', 'cat', 'parrot']
for i in 리스트11:
    j = i.capitalize()
    print(j)

#158
리스트12 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in 리스트12:
    j = i.split('.')
    print(j[0])

#159
리스트13 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트13:
    j = i.split('.')
    if j[1] == 'h':
        print(i)

#160
for i in 리스트13:
    j = i.split('.')
    if j[1] == 'h' or j[1] == 'c':
        print(i)

161
for i in range(0,100):
    print(i)

#162
for i in range(2002,2051,4):
    print(i)

#163
for i in range(1,31):
    if i%3==0:
        print(i)

#164
for i in range(10):
    print(f"0.{i}")

#166
for i in range(1,10):
    print(f"3x{i}={3*i}")

#167
for i in range(1,10,2):
    print(f"3x{i}={3*i}")

#168
sum = 0
for i in range(1,11):
    sum += i
print(sum)

#169
sum2 = 0
for i in range(1,11,2):
    sum2 += i
print(sum2)

#170
sum3 = 1
for i in range(1,11):
    sum3 *= i
print(sum3)

#171
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

#172
j = 0
for i in range(len(price_list)):
    print(j, price_list[i])
    j += 1

#173
j = len(price_list)-1
for i in range(len(price_list)):
    print(j, price_list[i])
    j -= 1

#174
j = 100
for i in range(1,4):
    print(j, price_list[i])
    j += 10

#175
my_list = ['가', '나', '다', '라']
for i in range(3):
    print(my_list[i], my_list[i+1])

#176
my_list2 = ["가", "나", "다", "라", "마"]
for i in range(len(my_list2)-2):
    print(my_list2[i], my_list2[i+1], my_list2[i+2])

#177
n = len(my_list)
for i in range(n-1, 0, -1):
    print(my_list[i], my_list[i-1])

#178
my_list3 = [100, 200, 400, 800]
for i in range(len(my_list3)-1):
    print(my_list3[i+1] - my_list3[i])

#179
my_list4 = [100, 200, 400, 800, 1000, 1300]
for i in range(len(my_list4)-2):
    avg = (my_list4[i]+my_list4[i+1]+my_list4[i+2])/3
    print(avg)

#180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):
    volatility.append(high_prices[i]-low_prices[i])
print(volatility)

#181
apart = [ ["101호", "102호"], ["201호", "202호"], ["301호", "302호"] ]

#182
stock = [['시가',100,200,300], ["증가", 80,210,330]]

#183
stock1 = {"시가": [100, 200, 300], "종가": [80, 210, 330] }

#184
stock2 = {"10/10":[80,110,70,90], "10/11":[210,230,190,200]}

#185
for i in apart:
    print(i[0])
    print(i[1])
print(" ")

#186
for i in apart[::-1]:
    print(i[0])
    print(i[1])
print(" ")

#187
for i in apart[::-1]:
    print(i[1])
    print(i[0])
print(" ")

#188
for i in apart:
    print(i[0])
    print("------")
    print(i[1])
    print("------")
print(" ")

#189
for i in apart:
    print(i[0])
    print(i[1])
    print("------")
print(" ")

#190
for i in apart:
    print(i[0])
    print(i[1])
print("------")

#191 data에는 매수한 종목들의 OHLC (open/high/low/close) 가격 정보가 바인딩 되어있다.
# 수수료를 0.014 %로 가정할 때, 각 가격에 수수료를 포함한 가격을 한라인에 하나씩 출력하라.
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data:
    for j in range(len(i)):
        print(i[j] + i[j]*0.00014)

#192
for i in data:
    for j in range(len(i)):
        print(i[j] + i[j]*0.00014)
    print("-----")

#193
result = []
for i in data:
    for j in range(len(i)):
        result.append(i[j] + i[j]*0.00014)
print(result)

#194
result1 = []
for i in data:
    sub = []
    for j in range(len(i)):
        sub.append(i[j] + i[j]*0.00014)
    result1.append(sub)
print(result1)

#195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:4]:
    print(i[3])

#196
for i in ohlc[1:4]:
    if i[3]>150:
        print(i[3])

#197
for i in ohlc[1:4]:
    if i[0] >= i[3]:
        print(i[3])

#198
vol = []
for i in ohlc[1:]:
    vol.append(i[1]-i[2])
print(vol)

#199
for i in ohlc[1:]:
    if i[3]>i[0]:
        print(i[1]-i[2])

#200
sum = 0
for i in ohlc[1:]:
    sum += i[3]-i[0]
print(sum)




