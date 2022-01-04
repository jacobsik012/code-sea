# Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐, X 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS 는 30 으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480 (세로 가로) - background.png
# 2. 캐릭터 : 70 * 70 - character.png
# 3. 똥 : 70 * 70 - enemy.png

import pygame
from random import *
#####################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("허윤이의 엄마 아빠 피하기 게임") # 게임 이름

# FPS
clock = pygame.time.Clock()
#####################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# background 이미지
background = pygame.image.load("C:/Users/매체협력부/Desktop/PythonWorkspace/pygame_basic/background_2.png")

# sprite 이미지
character = pygame.image.load("C:/Users/매체협력부/Desktop/PythonWorkspace/pygame_basic/character_2.png")
character_size = character.get_rect().size # 캐릭터 객체의 사이즈를 불러옴
character_width = character_size[0] # 캐릭터 객체의 가로 사이즈
character_height = character_size[1] # 캐릭터 객체의 세로 사이즈
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# sprite 이동할 좌표
to_x = 0
to_y = 0

# sprite 스피드
character_speed = 1

# 똥 이미지
enemy = pygame.image.load("C:/Users/매체협력부/Desktop/PythonWorkspace/pygame_basic/enemy_3.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, (screen_width - enemy_width))
enemy_y_pos = 0

# 똥 스피드
enemy_speed = 12

# 똥_2 이미지
enemy_2 = pygame.image.load("C:/Users/매체협력부/Desktop/PythonWorkspace/pygame_basic/enemy_4.png")
enemy_2_size = enemy_2.get_rect().size
enemy_2_width = enemy_2_size[0]
enemy_2_height = enemy_2_size[1]
enemy_2_x_pos = randint(0, (screen_width - enemy_2_width))
enemy_2_y_pos = 0 - enemy_2_height

# 똥_2 스피드
enemy_2_speed = 0

# 폰트 정의
game_font = pygame.font.Font(None, 30)

# 총 시간
total_time = 60

# 시작 시간
start_ticks = pygame.time.get_ticks()

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            # elif event.key == pygame.K_UP:
            #     to_y -= character_speed
            # elif event.key == pygame.K_DOWN:
            #     to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            # elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #     to_y = 0

        
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt
    # character_y_pos += to_y * dt

    # 가로 경계 값 정의
    if character_x_pos <= 0:
        character_x_pos = 0
    elif character_x_pos >= screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계 값 정의
    # if character_y_pos <= 0:
    #     character_y_pos = 0
    # elif character_y_pos >= screen_height - character_height:
    #     character_y_pos = screen_height - character_height

    enemy_y_pos += enemy_speed
    enemy_2_y_pos += enemy_2_speed
    if enemy_y_pos < (screen_height / 2) - (enemy_height / 2):
        enemy_speed = 12

    elif screen_height > enemy_y_pos >= (screen_height / 2) - (enemy_height / 2):
        enemy_2_speed = 12
        if enemy_2_y_pos > screen_height:
            enemy_2_y_pos = 0
            enemy_2_x_pos = randint(0, (screen_width - enemy_2_width))

    elif enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = randint(0, (screen_width - enemy_width))

    # 4. 충돌 처리
    character_rect = character.get_rect() # 캐릭터의 실제 랙탱글 정보 객체 생성
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    enemy_2_rect = enemy_2.get_rect()
    enemy_2_rect.left = enemy_2_x_pos
    enemy_2_rect.top = enemy_2_y_pos

    if character_rect.colliderect(enemy_rect) or character_rect.colliderect(enemy_2_rect):
        print("충돌했습니다.")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos ,character_y_pos))
    screen.blit(enemy, (enemy_x_pos ,enemy_y_pos))
    screen.blit(enemy_2, (enemy_2_x_pos, enemy_2_y_pos))

    # 타이머 집어 넣기
    # 경과 시간 넣기
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    
    # 타이머 그리기
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        print("타임 오버")
        running = False

    pygame.display.update()

pygame.time.delay(1000)

pygame.quit()