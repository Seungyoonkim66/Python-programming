# https://wikidocs.net/7023 : 51~60
# https://wikidocs.net/7025 : 61~70

#51
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)

#52
movie_rank.append('배트맨')
print(movie_rank)

#53
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)

#54
movie_rank.remove('럭키')
#del movie_rank[3]
print(movie_rank)

#55
movie_rank.remove("스플릿")
movie_rank.remove("배트맨")
print(movie_rank)

#56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

#57
nums = [1, 2, 3, 4, 5, 6, 7]
max = max(nums)
min = min(nums)
print(f"max: {max}\nmin: {min}")

#58
nums2 = [1, 2, 3, 4, 5]
print(sum(nums2))

#59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

#60
avg = sum(nums2)/len(nums2)
print(avg)
# 평균구하는 함수는 따로 없다. sum과 len을 활용해야 한다. 

#61
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#62
nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums3[::2])

#63
print(nums3[1::2])

#64
nums4 = [1, 2, 3, 4, 5]
print(nums4[::-1])

#65
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

#66
#" ".join - 리스트의 요소들을 " "로 연결
interest2 = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest2))

#67
print("/".join(interest2))

#68
print("\n".join(interest2))

#69
string = "삼성전자/LG전자/Naver"
interest3 = string.split("/")
print(interest3)

#70
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
