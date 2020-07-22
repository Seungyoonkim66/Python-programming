# https://wikidocs.net/7040 : 241~250

import datetime 
import time
import os

#241
now = datetime.datetime.now()
print(now)

#242
print(type(now)) #>> <class 'datetime.datetime'>

#244
for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)

#245
print(now.strftime("%H:%M:%S"))

#246
day = "2020-05-04"
res = datetime.datetime.strptime(day, "%Y-%m-%d")
print(res)

#246 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.
# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

# 247

# 248
print(os.getcwd())

#249
# os.rename("기존 파일", "새로운 파일 이름")

#250
# numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.
# import numpy
# for i in numpy.arange(0, 5, 0.1):
#     print(i)
