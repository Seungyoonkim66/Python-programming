# https://wikidocs.net/22000 : 81~90
# https://wikidocs.net/78563 : 91~100

#81 별 표현식
a, b, *c = (0, 1, 2, 3, 4, 5)
print(a)
print(b)
print(c)
print(type(c)) # >> list

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_scores,p,q = scores
print(valid_scores)

#82
p, q, *valid_scores_r = scores
print(valid_scores_r)

#83
p, *valid_scores_m, q = scores
print(valid_scores_m)

#84
temp = { }

#85
icecream = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(icecream)

#86
icecream['죠스바'] = 1200
icecream['월드콘'] = 1500
print(icecream)

#87
print(f"메로나 가격: {icecream['메로나']}")
# 딕셔너리는 인덱스 값 대신 key 값으로 접근하여 value를 반환한다. 

#88
icecream['메로나'] = 1300
print(f"메로나 가격: {icecream['메로나']}")

#89
del icecream['메로나']
print(icecream)

#90
# 딕셔너리에 없는 key값으로 접근하면 에러가 발생한다. 

#91
inventory = {'메로나':[300,20], '비비빅':[400,3], '죠스바':[250,100]}
print(inventory)

#92
print(inventory['메로나'][0], '원')

#93
print(inventory['메로나'][1], '개')

#94
inventory['월드콘'] = [500, 7]
print(inventory)

#95
ice = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
k = list(ice.keys())
print(k)

#96
v = list(ice.values())
print(v)

#97 
sum = sum(ice.values())
print(sum)

#98
# list의 append = dictionary의 update 
new = {'팥빙수':2700, '아맛나':1000}
ice.update(new)
print(ice)

#99
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)