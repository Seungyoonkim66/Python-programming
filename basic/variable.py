# https://wikidocs.net/7021

#11 변수 사용하기 
삼성전자  = 50000
총평가금액 = 삼성전자 * 10
print("총 평가금액", 총평가금액, "원")

#12
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, 현재가, PER)

#13
s = "hello"
t = "python"
print(s+"!", t)
# +를 하면 공백 없이 연결하여 출력 가능

#14
print(2+2*3) 
# >> 8

#15
a = 128
print(type(a))  # >> <class 'int'>
a = "132"
print(type(a))  # >> <class 'str'>

#16
num_str = "720"
print(type(int(num_str)))  # >> <class 'int'>

#17
num = 100
print(type(str(num)))  # >> <class 'str'>

#18
str= "15.79"
print(type(float(str)))  # >> <class 'float'>

#19
#정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year = "2020"
y = int(year)
print(y, y-1, y-2)

#20
#에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
총금액 = 48584 * 36 
print(총금액, '원')