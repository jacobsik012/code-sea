# from random import *
import pygame

# pygame.init()

# for event in pygame.event.get(): # pygame.event.get() 함수를 통해 사용자가 발생시킨 이벤트를 가져옴
#     if event.type == pygame.QUIT: # 가져온 이벤트 중 하나를 event 라는 변수로 생각하고, 해당 이벤트의 type을 검사
#         running = False

import os
current_path = os.path.dirname(__file__) # os.path 모듈의 dir() 함수는 현재 파일의 위치 반환
# alias : 컴퓨터 프로그램에서 동일한 데이터 요소나 포인트를 지칭하는 수단으로 사용되는 대체 레이블(alternate label). 동일한 변수, 배열, 레코드, 절차 등 데이터 요소를 가리키는데 1개의 레이블과 1개 또는 2개의 대체(별명) 레이블이 사용될 수 있다.
print(current_path)
image_path = os.path.join(current_path, "images", "lily")
print(image_path)

# 무기 만들기
# weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
# # weapon_rect = weapon.get_rect()
# weapon_size = weapon.get_rect().size
# print(weapon) # <Surface(20x430x24 SW)>
# print(weapon_rect) # <rect(0, 0, 20, 430)>
# print(weapon_size) # (20, 430) 사이즈가 튜플로 나옴

a = [[1, 2]]
a.append([3, 4])
print(a)

print(__file__) # 현재 파일의 디렉터리를 알려줌
print(os.path.dirname(__file__)) # 현재 파일을 담고 있는 디렉터리를 알려줌



# ball_images = [
#     pygame.image.load(os.path.join("C:/Users/매체협력부/Desktop/PythonWorkspace/pygame_project/images", "balloon1.png")),
#     pygame.image.load(os.path.join("C:/Users/매체협력부/Desktop/PythonWorkspace/pygame_project/images", "balloon2.png")),
#     pygame.image.load(os.path.join("C:/Users/매체협력부/Desktop/PythonWorkspace/pygame_project/images", "balloon3.png")),
#     pygame.image.load(os.path.join("C:/Users/매체협력부/Desktop/PythonWorkspace/pygame_project/images", "balloon4.png")),
#     pygame.image.load(os.path.join("C:/Users/매체협력부/Desktop/PythonWorkspace/pygame_project/images", "character.png")),
#     pygame.image.load(os.path.join("C:/Users/매체협력부/Desktop/PythonWorkspace/pygame_project/images", "background.png")),
#     pygame.image.load(os.path.join("C:/Users/매체협력부/Desktop/PythonWorkspace/pygame_project/images", "weapon.png"))
#     ]

# for ball_rect in ball_images:
#     print(ball_rect)

# floor = int(input("몇층까지 쌓을까요? "))

# for f in range(floor):
#     print("*" * (f + 1))

# balls = [1, 2, 3, 4]
# weapons = [11, 22, 3, 44]

# for ball_idx, ball_val in enumerate(balls):
#     print("ball :", ball_val)
#     for weapon_idx, weapon_val in enumerate(weapons):
#         print("weapon :", weapon_val)
#         if ball_val == weapon_val:
#             print("공과 무기가 충돌")
#             break

#     else:
#            continue
#     print("바깥 for 문 break")
#     break

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE"
title = title.split()
print(title)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE"
title = title.split("\t")
print(title)

title = ['가','나','다']
print(title)