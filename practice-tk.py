import pygame  # 파이게임 모듈 불러오기
import sys     # 게임 시스템 종료용

X = 600  # 가로 크기
Y = 600  # 세로 크기
pygame.init()  # pygame 초기화

# 창 크기 정하기
SURFACE = pygame.display.set_mode((X, Y))
# 창 업데이트 조정하기
FPSCLOCK = pygame.time.Clock()
# 창 이름 정하기
pygame.display.set_caption("파이게임 해보기")

# 게임 루프 시작
i = 0
while True:
    for event in pygame.event.get():   # 이벤트 받기
        if event.type == pygame.QUIT:  # 종료 이벤트(창 닫기) 라면
            pygame.quit()              # 파이게임 종료
            sys.exit()                 # 파이썬 종료
    SURFACE.fill((255, 255, 255))      # 배경 채우기(흰색)
    pygame.draw.rect(SURFACE, (255, 0, 0), (100, i, 100, 100))  # 빨간색 사각형 생성
    pygame.draw.ellipse(SURFACE, (0, 0, 255), (i, 100, 75, 75))  # 파란색 타원 생성
    i += 1  # 1씩 증가
    if i > Y:  # Y좌표계를 초과하면
        i = 0  # 0으로 초기화
    pygame.display.update()            # 창 업데이트
    FPSCLOCK.tick(120)  # 초당 120회로 업데이트를 조절