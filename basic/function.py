# https://wikidocs.net/23906 : 201~210
# https://wikidocs.net/23907 : 211~220
# https://wikidocs.net/7039 : 221~230
# https://wikidocs.net/78556 : 231~240

# #201
# def print_coin():
#     print("비트코인")

# #202
# print_coin()

# #203
# for i in range(100):
#     print_coin()

#204
def print_coins():
    for i in range(100):
        print("비트코인")

#205
#함수가 정의되기 전에 호출될 수 없다. 

#206
def message() :
    print("A")
    print("B")
message()
print("C")
message()
# >> A B C A B

#207
print("A")
def message() :
    print("B")
print("C")
message()
# >> A C B

#208
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()
# >> A C B E D

#209
def message1():
    print("A")
def message2():
    print("B")
    message1()
message2()
# >> B A

#210
def message1():
    print("A")
def message2():
    print("B")
def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()
message3()
# >>B C B C B C A

#211
def 함수(문자열) :
    print(문자열)
함수("안녕")
함수("Hi")
# >> 안녕 Hi

#212
def 함수(a, b) :
    print(a + b)
함수(3, 4)
함수(7, 8)
# >> 7 15

#213
#매개변수가 있는 함수는 매개변수와 함께 호출해야 한다. 

#214
#함수 호출시 매개변수의 자료형을 정의한 것과 일치시켜야 한다. 

#215
def print_with_smile(str):
    print(str+":D")

#216
print_with_smile("안녕하세요")

#217
def print_upper_price(cur):
    print(cur*1.3)
print_upper_price(3000) # >> 3900.0

#218
def print_sum(a, b):
    print(a+b)
print_sum(3,4) # >> 7

#219
def print_arithmetic_operation(a,b):
    print("%d + %d = " %(a, b), a+b)
    print("%d - %d = " %(a, b), a-b)
    print("%d * %d = " %(a, b), a*b)
    print("%d / %d = " %(a, b), a/b)
print_arithmetic_operation(3,4)

#220
def print_max(a,b,c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else :
        print(c)
print_max(6,2,8)

#221
def print_reverse(str):
    for i in str[::-1]:
        print(i, end="")
print_reverse("python")
print("")

#222
def print_score(scores):
    print(sum(scores)/len(scores))
print_score ([1, 2, 3])

#223
def print_even(numbers):
    for i in numbers:
        if i%2==0:
            print(i)
print_even ([1, 3, 2, 10, 12, 11, 15])

#224
def print_keys(dic):
    key = dic.keys()
    for i in key:
        print(i)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})

#225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key(md, key):
    print(md[key])
print_value_by_key  (my_dict, "10/26")

#226 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
def print_5xn (sentence):
    chunk = int(len(sentence)/5)
    for i in range(chunk+1):
        print(sentence[i * 5: i * 5 + 5])
print_5xn("아이엠어보이유알어걸")

#227 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
def print_mxn(sentence, k):
    chunk = int(len(sentence)/k)
    for i in range(chunk+1):
        print(sentence[i*k : i*k+k])
print_mxn("아이엠어보이유알어걸", 3)

#228
def calc_monthly_salary(annual_salary):
    month_salary = annual_salary/12
    tra = month_salary%10
    print(month_salary-tra)
calc_monthly_salary(12000000)

#229
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)
my_print(a=100, b=200)
# >> 왼쪽 : 100  오른쪽 : 200

#230 
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)
my_print(b=100, a=200)
# >> 왼쪽 : 200  오른쪽 : 100

#231
# def n_plus_1 (n) :
#     result = n + 1
# n_plus_1(3)
# print (result)
# >> result는 n_plus_1 함수 내에서 정의되었기 때문에 함수 밖에서 사용할 수 없다. 


#232
def make_url(company):
    print("www.%s.com" %(company))
make_url("naver")

#233
def make_list(str1):
    리스트 = list(str1)
    print(리스트)
make_list("abcd")

#234
def pickup_even(nums):
    res = []
    for i in nums:
        if i%2==0:
            res.append(i)
    print(res)
pickup_even([3, 4, 5, 6, 7, 8])

#235
def convert_int(numsrt):
    num1 = numsrt.replace(",", "")
    print(int(num1))
convert_int("1,234,567")

#236
def 함수(num) :
    return num + 4
a = 함수(10)    #14
b = 함수(a)     #18
c = 함수(b)     #22
print(c)
# >> 22

#237
def 함수(num) :
    return num + 4
c = 함수(함수(함수(10)))
print(c)
# >> 22

#238
def 함수1(num) :
    return num + 4
def 함수2(num) :
    return num * 10
a = 함수1(10)   # 14
c = 함수2(a)
print(c)
# >> 140

#239
def 함수1(num) :
    return num + 4
def 함수2(num) :
    num = num + 2
    return 함수1(num)
c = 함수2(10)
print(c)
# >> 16

#240
def 함수0(num) :
    return num * 2
def 함수1(num) :
    return 함수0(num + 2)
def 함수2(num) :
    num = num + 10
    return 함수1(num)
c = 함수2(2)
print(c)
# >> 28




