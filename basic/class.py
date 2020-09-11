# https://wikidocs.net/7035 : 251~260
# https://wikidocs.net/7036 : 261~270
# https://wikidocs.net/7037 : 271~280
# https://wikidocs.net/7041 : 281~290

#251, 252, 253
class Human:
    def __init__(self):
        print("응애응애")
areum = Human()

#255
class Human2:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

seungyoon = Human2("승윤", 23, "여자")
print(seungyoon.name)

#256
jo = Human2("조아름", 25, "여자")
print("이름: %s 나이: %d 성별: %s" %(jo.name, jo.age, jo.gender))

#257, 258, 259
class Human3:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):
        print("나의 죽음을 알리지마라")

    def who(self):
        print("이름: %s 나이: %d 성별: %s" %(self.name, self.age, self.gender))
    
    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

jo = Human3("조아름", 25, "여자")
jo.who()
jo.setInfo("조아름", 26, "여자")
jo.who()
del(jo)

# 261~270
class Stock:
    def __init__(self, name, code, per, pbr, prof):
        self.name = name
        self.code = code
        self.per = per
        self.PBR = pbr
        self.prof = prof

    def set_name(self, name):
        self.name = name
    
    def set_code(self, code):
        self.code = code
    
    def set_per(self, per):
        self.per = per
    
    def set_pbr(self, pbr):
        self.pbr = pbr
    
    def set_prof(self, prof):
        self.prof = prof

    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

# 삼성 = Stock("삼성전자", "005930")
# print(삼성.name)
# print(삼성.code)

# a = Stock(None, None)
# a.set_name("삼성전자")
# a.set_code("005930")
# print(a.name)
# print(a.code)

# print(삼성.get_name())
# print(삼성.get_code())

객체1 = Stock("삼성전자", "005930", 15.79, 1.33,2.83)
print(객체1.prof)
객체1.set_per(12.75)
print(객체1.per)

객체2 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
객체3 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

주식 = [객체1, 객체2, 객체3]
for i in 주식:
    print(i.per)

#271
import random 

class Account:
    count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "sc은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        self.deposit_num = 0
        Account.count +=1
    
    def get_account_num(self):
        print(Account.count)

    def deposit(self, balance):
        if balance >= 1:
            self.balance += balance
            self.deposit_num += 1
            if self.deposit_num%5 == 0:
                self.balance += self.balance*0.01
        else :
            print("입금은 1원이상부터 가능합니다.")
    
    def withdraw(self, w):
        if w <= self.balance:
            self.balance -= w
        else:
            print("잔액보다 큰 금액은 인출할 수 없습니다.")

    def display_info(self):
        
        print("은행이름:" , self.bank)
        print("예금주:" , self.name)
        print("계좌번호:", self.account_number)
        print("잔고:", self.balance)

kim = Account("김민수", 100)
# print(kim.name)
# print(kim.balance)
# print(kim.bank)
# print(kim.account_number)

#272
print(Account.count)
Lee = Account("이민수", 200)
print(Account.count)

#273
Lee.get_account_num()

#274
Lee.deposit(400)
print(Lee.balance)

#275
Lee.withdraw(100)
print(Lee.balance)

#276
p = Account("파이썬", 10000)
p.display_info()

#277
p = Account("파이썬", 10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(5000)
p.deposit(5000)
print(p.balance)

#278
acc1 = Account("김승윤", 20000000)
acc2 = Account("김기윤", 2000)
acc3 = Account("이진하", 3000)
accs = [acc1, acc2, acc3]

#279
for i in accs:
    if i.balance >= 1000000:
        print(i.name)

#280

#281
class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price
    
    def get_info(self):
        print("바퀴수", self.wheel)
        print("가격", self.price)

c1 = Car(4, 1000)
print(c1.wheel)
print(c1.price)

#282~284, 287
class Bicar(Car):
    def __init__(self, wheel, price, name):
        super(). __init__(wheel,price)
        self.name = name

    def get_info(self):
        super().get_info()
        print("구동계", self.name)

c2 = Bicar(2, 100, "시마노")
print(c2.wheel)
print(c2.price)
print(c2.name)

#285
class Focar(Car):
    def __init__(self, wheel, price):
        super(). __init__(wheel, price)

c3 = Focar(4, 1000)
c3.get_info()

#286
c2.get_info()

#288
class 부모:
  def 호출(self):
    print("부모호출")

class 자식(부모):
  def 호출(self):
    print("자식호출")

나 = 자식()
나.호출()
# >> 자식호출

#289
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")

나 = 자식()
# >> 자식생성

#290
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()
# >> 부모생성
