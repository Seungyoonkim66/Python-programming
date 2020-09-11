# https://wikidocs.net/7027 : 71~80

#71
my_variable = ()
print(type(my_variable))
# >> <class 'tuple'>

#72
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

#73
t = (1)
print(type(t))
# >> int
t1 = (1, )
print(type(t1))
# >> tuple

#74
# 튜플은 수정이 불가능한 자료구조이다. like 문자열

#75
t3 = 1, 2, 3, 4
print(type(t3))
# >> tuple

#76
interest = ('삼성전자', 'LG전자', 'SK Hynix')
l = list(interest)
print(type(l))
# >> list

#78
interest1 = ['삼성전자', 'LG전자', 'SK Hynix']
t4 = tuple(interest1)
print(type(t4))

#79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# >> apple banana cake 

#80
t5 = tuple(range(2,99,2))
print(t5)
#range(,,)
