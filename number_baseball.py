import pygame
import random

# 맞는지 틀린지 증명
def test_answer():
    global s,b, running
    s = 0
    b = 0
    # 몫
    quoto_1 = int(texts[0]) // 100 # ex) 538 // 100 = 5
    quoto_2 = (int(texts[0]) - quoto_1*100) // 10 # ex) 538 -500 = 30 30// 10 = 3
    quoto_3 = (int(texts[0]) - quoto_1*100 - quoto_2 *10) # ex 538 - 530 = 8
   
   # 입력한 수 중 1개가 숫자와 위치가같다면 - 1strike
    if quoto_1== three_numbers[0]:
        s =1
        # 입력한 수 중 2개가 숫자와 위치가 같다면 - 2strike
        if quoto_2 == three_numbers[1]:
            s = 2
            # 입력한 수 중 3개가 숫자와 위치가 같다면 - success
            if quoto_3 == three_numbers[2]: 
                s = 3
                screen.fill(BLACK)
                screen.blit(success,(success_x,success_y))
                screen.blit(ans_num,(ans_num_x,ans_num_y))
                running = False
                
        elif quoto_3 == three_numbers[2]:
            s = 2
    elif quoto_2==three_numbers[1]:
        s = 1
        if quoto_3 == three_numbers[2]:
            s = 2
    elif quoto_3 == three_numbers[2]:
        s = 1
    
    # 입력한 수가 위치는 다르지만 숫자가 같다면 - 1BALL
    if not quoto_1 == three_numbers[0] and quoto_1 in three_numbers :
        b = 1
        if not quoto_2 == three_numbers[1] and quoto_2 in three_numbers :
            b= 2
            if not quoto_3 == three_numbers[2] and quoto_3 in three_numbers :
                b= 3
        elif not quoto_3 == three_numbers[2] and quoto_3 in three_numbers :
            b= 2
    elif not quoto_2 == three_numbers[1] and quoto_2 in three_numbers :
        b = 1
        if not quoto_3 == three_numbers[2] and quoto_3 in three_numbers :
            b= 2
    elif not quoto_3 == three_numbers[2] and quoto_3 in three_numbers :
        b = 1
    

# 시작화면 보여주기
def display_start_screen():

    screen.blit(title,(title_x,title_y))
    screen.blit(press,(press_x,press_y))
    pygame.draw.circle(screen,WHITE,start_button.center,60,5)
    

# 게임화면 보여주기
def display_game_screen():
    global s,b
    screen.blit(background,(0,0))
    screen.blit(timer,(20,20))
    
    # Render the current text.
    txt_surface = game_font2.render(text, True, color)
    # Resize the box if the text is too long.
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    # Blit the text.
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    # Blit the input_box rect.
    pygame.draw.rect(screen, color, input_box, 2)
    
    test_answer()
    
    # 전광판
    strike_ball = game_font2.render("strike:"+ str(s) +'/'+"ball:"+str(b),True,GREEN)
    strike_ball_x = 200
    strike_ball_y = 100
    screen.blit(strike_ball,(strike_ball_x,strike_ball_y))
          

# pos에 해당하는 버튼 확인
def check_buttons(pos):
    global start # 전역변수로 바꿈 즉 밑에 start값이 정의되도 사용가능
    if start_button.collidepoint(pos): # start_button 과 사용자가 클릭한 좌표가 같을때 게임 시작
        start = True 


##################################################################################
pygame.init()

screen_width = 1040
screen_height = 740
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Number Baseball")

background = pygame.image.load("C:/Users/82108/Desktop/대현/baseball.png")
###################################################################################

# 입력 박스
input_box = pygame.Rect(400, 500, 120, 120)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''

# text
texts = [0]

# 숨김 처리
hidden = False

# 시작
start = False

# COLOR
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (50,50,50)
GREEN = (0,255,0)

# Font
game_font = pygame.font.Font(None,150)
game_font2 = pygame.font.Font(None,120)
game_font3 = pygame.font.Font(None,40)

# 타이머
start_ticks = pygame.time.get_ticks()
total_time = 100

# 세개의 랜덤 숫자를 정함
three_numbers = random.sample(range(1,10),3)

# 정답을 알고싶다면? print(answer)
answer_pt = []
answer_pt.append(three_numbers[0])
answer_pt.extend(str(three_numbers[1]))
answer_pt.extend(str(three_numbers[2]))
answer = 100*int(three_numbers[0]) + 10*int(three_numbers[1]) + int(three_numbers[2])

# 시작 화면 - 버튼
start_button = pygame.Rect(0,0,120,120)
start_button.center = ((screen_width/2),screen_height-120)

# 게임 문구
title = game_font.render("Number Baseball",True,WHITE)
title_size = title.get_rect().size
title_width = title_size[0]
title_height = title_size[1]
title_x = 100
title_y = 200


press = game_font2.render("Press Circle!",True,WHITE)
press_x = 250
press_y = 450

success = game_font2.render("Success!",True,GREEN)
success_x = 200
success_y = 200

ans_num = game_font2.render("Number is : "+str(answer),True,GREEN)
ans_num_x = 200
ans_num_y = 300


# 게임 루프
running = True
while running:
    
    click_pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스클릭 했을때
            click_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input _box rect.
            if input_box.collidepoint(event.pos):
                # Toggle the active variable.
                active = not active
            else:
                active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    text = text
                    texts.append(text)
                    del texts[0]
                    test_answer()
                    if int(texts[0]) < 100 or int(texts[0]) > 999:
                        print("There are only three digits available.")
                    else:
                        print(texts,"strike:"+ str(s) +'/'+"ball:"+str(b))
                    
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
    screen.fill(BLACK)

    # 게임 시작하지 않았다면
    if not start:
        display_start_screen()
    
    # 게임 시작했다면
    else:
        display_game_screen()

    if click_pos :
        check_buttons(click_pos)

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font3.render("Time:" + str(int(total_time-elapsed_time)),True,WHITE)
    time_over = game_font.render("Time Over",True,WHITE)

    if int(total_time) - int(elapsed_time) < 0:
        running = False
        screen.fill(BLACK)
        screen.blit(time_over,(250,300))
        
    
    pygame.display.update()
      

pygame.time.delay(2000)

pygame.quit()