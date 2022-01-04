from random import *
# lst = list(range(1, 21))
# shuffle(lst)
# chicken = lst[19] # chicken 당첨자
# lst. pop()
# coffee = sample(lst, 3) # coffee 당첨자

# print(" -- 당첨자 발표 --\n치킨 당첨자 : {0}\n커피 당첨자 : {1}\n -- 축하합니다 --". format(chicken, coffee))

users = list(range(1, 21))
shuffle(users)
winners = sample(users, 4)
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {}". format(winners[0]))
print("커피 당첨자 : {}". format(winners[1:]))
print(" -- 축하합니다 --")
