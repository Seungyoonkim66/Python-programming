# https://wikidocs.net/7022


#21 문자열 인덱싱
letters = 'python'
print(letters[0], letters[2])

#22 문자열 슬라이싱
license = "24가 2210"
print(license[-4:])
# 음수 값은 문자열 뒤에서부터 인덱싱, 생략하면 0 이나 문자열 끝을 의미한다. 

#23 문자열 인덱싱
string = "홀짝홀짝홀짝"
print(string[0::2])
# 문자열[시작인덱스:끝인덱스:오프셋]

#24 뒤집어 출력하기 
string = "PYTHON"
print(string[::-1])

#25 문자열 치환
phone = "010-1111-2222"
p = phone.replace("-", " ")
print(p)

#26 
p2 = phone.replace("-", "")
print(p2)

#27 
url = "http://sharebook.kr"
p = url.split(".")
print(p[1])

#28 문자열은 immutable 
# lang = 'python'
# lang[0] = "P"
# print(lang)  # >> 문자열은 수정할 수 없어서 에러 발생 

#29 replace 매서드 
string = 'abcdfe2a354a32a'
s = string.replace('a', 'A')
print(s)

#30
string = 'abcd'
string.replace('b', 'B')
print(string)
# >> abcd / 문자열은 수정할 수 없기 때문에 원본 그대로를 변경할 수 없다. 

#31
a = "3"
b = "4"
print(a+b)
# >> 34

#32
print("Hi"*3)
# >> HiHiHi

#33 화면에 '-'를 80개 출력하세요.
print("-" * 80)

#34
t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

#35 
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" %(name1, age1))
print("이름: %s 나이: %d" %(name2, age2))

#36
print("이름: {} 나이: {}" .format(name1, age1))
print("이름: {} 나이: {}" .format(name2, age2))

#37
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

#38
상장주식수 = "5,969,782,550"
변환값 = int(상장주식수.replace(",", ""))
print(변환값)

#39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

#40
data = "   삼성전자   "
data1 = data.replace(" ", "")
print(data1)
data2 = data.strip()
print(data2)

#41
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)

#42
ticker2 = ticker1.lower()
print(ticker2)

#43
str = "hello"
str2 = str.capitalize()
print(str2)

#44
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))
# >> True

#45
print(file_name.endswith(("xlsx", "xls"))) 
# >> True

#46
file_name2 = "2020_보고서.xlsx"
print(file_name2.startswith('2020'))
# >> True

#47
a1 = "hello world"
print(a1.split())
# >> ['hello', 'world']

#48
ticker4 = "stc_krw"
ticker5 = ticker4.split('_')
print(ticker5[0])
# >>stc

#49
date = "2020-05-01"
date_s = date.split('-')
year = date_s[0]
mon = date_s[1]
day = date_s[2]
print(f"{year}년 {mon}월 {day}일")

#50
data3 = "039490     "
print(data3.rstrip())
