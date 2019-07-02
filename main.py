
import pygame, random
pygame.init()
pygame.font.init()
screenwidth = 1000
screenheight = 800
icon = pygame.image.load('images/dove_right_up.png')
window = pygame.display.set_mode([screenwidth, screenheight])
pygame.display.set_caption('Too Many Doves!')
pygame.display.set_icon(icon)
c = pygame.time.Clock()
x=450
y=650
player = pygame.Rect(x,y,50,150)
player_color = (20, 214, 10)
shot = False
run = True
speed = 25
white = (255,255,255)
wait_time = 40
left = 1
right = 6
background = pygame.image.load('images/bgtest1.png')
curtains = pygame.image.load('images/bgtest2.png')
right_jim = pygame.image.load('images/jim_left_1.png')
going_right = False
moves = 0
dove_h = 44
dove_w = 39
spacing = 75
score = 0
jim_move = True
font = pygame.font.SysFont('advanced-_pixel-7.ttf', 75)
digit1 = 0
digit2 = 0
digit3 = 0
scoretext = font.render('SCORE: ' + str(digit1) + str(digit2) + str(digit3) , False, (255,255,255))
#row1 = [first1,first2,first3,first4,first5,first6]
pygame.mixer.music.load('Song_Doves_Go_Fast.wav')
pygame.mixer.music.play(-1)
score_sound = pygame.mixer.Sound('snd_score.wav')
shoot_sound = pygame.mixer.Sound('snd_Got_Hit.wav')
get_hit = pygame.mixer.Sound('snd_Hit_with_poop.wav')
poop_sound = pygame.mixer.Sound('sndPoop1.wav')
#---ROW ONE---#
first1_alive = True
first2_alive = True
first3_alive = True
first4_alive = True
first5_alive = True
first6_alive = True

#---Load row1---#
first1 = pygame.Rect(25,200,dove_w,dove_h)
first2 = pygame.Rect((first1.x + spacing),200,dove_w,dove_h)
first3 = pygame.Rect((first2.x + spacing),200,dove_w,dove_h)
first4 = pygame.Rect((first3.x + spacing),200,dove_w,dove_h)
first5 = pygame.Rect((first4.x + spacing),200,dove_w,dove_h)
first6 = pygame.Rect((first5.x + spacing),200,dove_w,dove_h)

#---ROW TWO---#
second1_alive = True
second2_alive = True
second3_alive = True
second4_alive = True
second5_alive = True
second6_alive = True

#---ROW THREE---#
third1_alive = True
third2_alive = True
third3_alive = True
third4_alive = True
third5_alive = True
third6_alive = True

#---ROW THREE---#
fourth1_alive = True
fourth2_alive = True
fourth3_alive = True
fourth4_alive = True
fourth5_alive = True
fourth6_alive = True
shot0 = pygame.image.load('images/magic_bolt0.png')
shot1 = pygame.image.load('images/magic_bolt1.png')
poop = pygame.image.load('images/poop1.png')
poop_w = 15
poop_h = 30
flaps = 0
move_timer = 25
jim_w = 124
jim_h = 125
dove_right_up = pygame.image.load('images/dove_right_up.png')
dove_right_down = pygame.image.load('images/dove_right_down.png')
dove_left_up = pygame.image.load('images/dove_left_up.png')
dove_left_down = pygame.image.load('images/dove_left_down.png')

jim_left = pygame.image.load('images/jim_left_1.png')
shot_w = 8
shot_h = 35
shot_rect = pygame.Rect((player.x + 42),screenheight - 100,shot_w,shot_h)
shot_timer = 0
#def fall(dove):


pooping = False
while run:
    window.blit(background,(0,0))
    second1 = pygame.Rect(first1.x,first1.y - dove_h,dove_w,dove_h)
    second2 = pygame.Rect(first2.x,first2.y - dove_h,dove_w,dove_h)
    second3 = pygame.Rect(first3.x,first3.y - dove_h,dove_w,dove_h)
    second4 = pygame.Rect(first4.x,first4.y - dove_h,dove_w,dove_h)
    second5 = pygame.Rect(first5.x,first5.y - dove_h,dove_w,dove_h)
    second6 = pygame.Rect(first6.x,first6.y - dove_h,dove_w,dove_h)
    third1 = pygame.Rect(first1.x,first1.y - (dove_h * 2),dove_w,dove_h)
    third2 = pygame.Rect(first2.x,first2.y - (dove_h * 2),dove_w,dove_h)
    third3 = pygame.Rect(first3.x,first3.y - (dove_h * 2),dove_w,dove_h)
    third4 = pygame.Rect(first4.x,first4.y - (dove_h * 2),dove_w,dove_h)
    third5 = pygame.Rect(first5.x,first5.y - (dove_h * 2),dove_w,dove_h)
    third6 = pygame.Rect(first6.x,first6.y - (dove_h * 2),dove_w,dove_h)
    fourth1 = pygame.Rect(first1.x,first1.y - (dove_h * 3),dove_w,dove_h)
    fourth2 = pygame.Rect(first2.x,first2.y - (dove_h * 3),dove_w,dove_h)
    fourth3 = pygame.Rect(first3.x,first3.y - (dove_h * 3),dove_w,dove_h)
    fourth4 = pygame.Rect(first4.x,first4.y - (dove_h * 3),dove_w,dove_h)
    fourth5 = pygame.Rect(first5.x,first5.y - (dove_h * 3),dove_w,dove_h)
    fourth6 = pygame.Rect(first6.x,first6.y - (dove_h * 3),dove_w,dove_h)
    flap_up = (flaps%2) == 0
    if flap_up and not pooping:
        poop_column = random.randint(1,6)
        if poop_column == 1:
            if first1_alive:
                poop_dove = first1
            elif second1_alive:
                poop_dove = second1
            elif third1_alive:
                poop_dove = third1
            elif fourth1_alive:
                poop_dove = fourth1

        if poop_column == 2:
            if first2_alive:
                poop_dove = first2
            elif second2_alive:
                poop_dove = second2
            elif third2_alive:
                poop_dove = third2
            elif fourth2_alive:
                poop_dove = fourth2

        if poop_column == 3:
            if first3_alive:
                poop_dove = first3
            elif second3_alive:
                poop_dove = second3
            elif third3_alive:
                poop_dove = third3
            elif fourth3_alive:
                poop_dove = fourth3
        if poop_column == 4:
            if first4_alive:
                poop_dove = first4
            elif second4_alive:
                poop_dove = second4
            elif third4_alive:
                poop_dove = third4
            elif fourth4_alive:
                poop_dove = fourth4
        if poop_column == 5:
            if first5_alive:
                poop_dove = first5
            elif second5_alive:
                poop_dove = second5
            elif third5_alive:
                poop_dove = third5
            elif fourth5_alive:
                poop_dove = fourth5
        if poop_column == 6:
            if first6_alive:
                poop_dove = first6
            elif second6_alive:
                poop_dove = second6
            elif third6_alive:
                poop_dove = third6
            elif fourth6_alive:
                poop_dove = fourth6
        pooping = True
        poop_y = poop_dove.y + dove_h
        poop_rect = pygame.Rect(poop_dove.x + (dove_w / 2),poop_y, poop_w, poop_h)
        pygame.mixer.Sound.play(poop_sound)
    elif not flap_up:
        pooping = False
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Detects if Shot
    if keys[pygame.K_UP] and not shot:
        shot = True
        shot_rect = pygame.Rect((player.x + 42),screenheight - 100,shot_w,shot_h)
        pygame.mixer.Sound.play(shoot_sound)



    #Move left or right
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
        going_right = False
        move_timer -= 1
    if keys[pygame.K_RIGHT] and player.x < screenwidth - (player.width*2):
        player.x += 5
        going_right = True
        move_timer -= 1



    #---ROW ONE---#

    #---Move Doves---#
    wait_time -= 1
    if wait_time == 0:
        first1.x += speed
        first2.x += speed
        first3.x += speed
        first4.x += speed
        first5.x += speed
        first6.x += speed
        flaps+=1
        wait_time = 40

    #---BOTTOM---#

    #--LEFT--#
    if first1_alive:
        left = first1.x
    elif second1_alive:
        left = second1.x
    elif third1_alive:
        left = third1.x
    elif fourth1_alive:
        left = fourth1.x

    elif first2_alive:
        left = first2.x
    elif second2_alive:
        left = second2.x
    elif third2_alive:
        left = third2.x
    elif fourth2_alive:
        left = fourth2.x

    elif first3_alive:
        left = first3.x
    elif second3_alive:
        left = second3.x
    elif third3_alive:
        left = third3.x
    elif fourth3_alive:
        left = fourth3.x

    elif first4_alive:
        left = first4.x
    elif second4_alive:
        left = second4.x
    elif third4_alive:
        left = third4.x
    elif fourth4_alive:
        left = fourth4.x

    elif first5_alive:
        left = first5.x
    elif second5_alive:
        left = second5.x
    elif third5_alive:
        left = third5.x
    elif fourth5_alive:
        left = fourth5.x

    elif first6_alive:
        left = first6.x
    elif second6_alive:
        left = second6.x6
    elif third6_alive:
        left = third6.x
    elif fourth6_alive:
        left = fourth6.x

    #--RIGHT--#
    if first6_alive:
        right = first6.x
    elif second6_alive:
        right = first6.x
    elif third6_alive:
        right = third6.x
    elif fourth6_alive:
        right = fourth6.x

    elif first5_alive:
        right = first5.x
    elif second5_alive:
        right = first5.x
    elif third5_alive:
        right = third5.x
    elif fourth5_alive:
        right = fourth5.x

    elif first4_alive:
        right = first4.x
    elif second4_alive:
        right = first4.x
    elif third4_alive:
        right = third4.x
    elif fourth4_alive:
        right = fourth4.x

    elif first3_alive:
        right = first3.x
    elif second3_alive:
        right = first3.x
    elif third3_alive:
        right = third3.x
    elif fourth3_alive:
        right = fourth3.x

    elif first2_alive:
        right = first2.x
    elif second2_alive:
        right = first2.x
    elif third2_alive:
        right = third2.x
    elif fourth2_alive:
        right = fourth2.x

    elif first1_alive:
        right = first1.x
    elif second1_alive:
        right = first1.x
    elif third1_alive:
        right = third1.x
    elif fourth1_alive:
        right = fourth1.x





    if right >= screenwidth - 100 or left <= 0:
        moves += 1
        speed *= -1
        first1.y += 50
        first2.y += 50
        first3.y += 50
        first4.y += 50
        first5.y += 50
        first6.y += 50
        first1.x += speed
        first2.x += speed
        first3.x += speed
        first4.x += speed
        first5.x += speed
        first6.x += speed
    #window.fill((0,0,0))
    if speed > 0:
        if first1_alive and flap_up:
            window.blit(dove_right_up, (first1.x,first1.y))
        elif first1_alive:
            window.blit(dove_right_down, (first1.x,first1.y))

        if first2_alive and flap_up:
            window.blit(dove_right_up, (first2.x,first2.y))
        elif first2_alive:
            window.blit(dove_right_down, (first2.x,first2.y))

        if first3_alive and flap_up:
            window.blit(dove_right_up, (first3.x,first3.y))
        elif first3_alive:
            window.blit(dove_right_down, (first3.x,first3.y))

        if first4_alive and flap_up:
            window.blit(dove_right_up, (first4.x,first4.y))
        elif first4_alive:
            window.blit(dove_right_down, (first4.x,first4.y))

        if first5_alive and flap_up:
            window.blit(dove_right_up, (first5.x,first5.y))
        elif first5_alive:
            window.blit(dove_right_down, (first5.x,first5.y))

        if first6_alive and flap_up:
            window.blit(dove_right_up, (first6.x,first6.y))
        elif first6_alive:
            window.blit(dove_right_down, (first6.x,first6.y))
    if speed < 0:
        if first1_alive and flap_up:
            window.blit(dove_left_up, (first1.x,first1.y))
        elif first1_alive:
            window.blit(dove_left_down, (first1.x,first1.y))

        if first2_alive and flap_up:
            window.blit(dove_left_up, (first2.x,first2.y))
        elif first2_alive:
            window.blit(dove_left_down, (first2.x,first2.y))

        if first3_alive and flap_up:
            window.blit(dove_left_up, (first3.x,first3.y))
        elif first3_alive:
            window.blit(dove_left_down, (first3.x,first3.y))

        if first4_alive and flap_up:
            window.blit(dove_left_up, (first4.x,first4.y))
        elif first4_alive:
            window.blit(dove_left_down, (first4.x,first4.y))

        if first5_alive and flap_up:
            window.blit(dove_left_up, (first5.x,first5.y))
        elif first5_alive:
            window.blit(dove_left_down, (first5.x,first5.y))

        if first6_alive and flap_up:
            window.blit(dove_left_up, (first6.x,first6.y))
        elif first6_alive:
            window.blit(dove_left_down, (first6.x,first6.y))
    if shot_rect.y <= 0:
        shot = False

    #Detect if a dove is shot
    if shot_rect.x >= first1.x and shot_rect.x <= first1.x+dove_w and shot_rect.y <=first1.y+dove_w and first1_alive and shot:
        shot=False
        first1_alive = False
        score += 5

    if shot_rect.x >= first2.x and shot_rect.x <= first2.x+dove_w and shot_rect.y <=first2.y+dove_w and first2_alive and shot:
        shot=False
        first2_alive = False
        score += 5

    if shot_rect.x >= first3.x and shot_rect.x <= first3.x+dove_w and shot_rect.y <=first3.y+dove_w and first3_alive and shot:
        shot=False
        first3_alive = False
        score += 5

    if shot_rect.x >= first4.x and shot_rect.x <= first4.x+dove_w and shot_rect.y <=first4.y+dove_w and first4_alive and shot:
        shot=False
        first4_alive = False
        score += 5

    if shot_rect.x >= first5.x and shot_rect.x <= first5.x+dove_w and shot_rect.y <=first5.y+dove_w and first5_alive and shot:
        shot=False
        first5_alive = False
        score += 5

    if shot_rect.x >= first6.x and shot_rect.x <= first6.x+dove_w and shot_rect.y <=first6.y+dove_w and first6_alive and shot:
        shot=False
        first6_alive = False
        score += 5


    #---ROW TWO---#

    if speed > 0:
        if second1_alive and flap_up:
            window.blit(dove_right_up, (second1.x,second1.y))
        elif second1_alive:
            window.blit(dove_right_down, (second1.x,second1.y))

        if second2_alive and flap_up:
            window.blit(dove_right_up, (second2.x,second2.y))
        elif second2_alive:
            window.blit(dove_right_down, (second2.x,second2.y))

        if second3_alive and flap_up:
            window.blit(dove_right_up, (second3.x,second3.y))
        elif second3_alive:
            window.blit(dove_right_down, (second3.x,second3.y))

        if second4_alive and flap_up:
            window.blit(dove_right_up, (second4.x,second4.y))
        elif second4_alive:
            window.blit(dove_right_down, (second4.x,second4.y))

        if second5_alive and flap_up:
            window.blit(dove_right_up, (second5.x,second5.y))
        elif second5_alive:
            window.blit(dove_right_down, (second5.x,second5.y))

        if second6_alive and flap_up:
            window.blit(dove_right_up, (second6.x,second6.y))
        elif second6_alive:
            window.blit(dove_right_down, (second6.x,second6.y))
    if speed < 0:
        if second1_alive and flap_up:
            window.blit(dove_left_up, (second1.x,second1.y))
        elif second1_alive:
            window.blit(dove_left_down, (second1.x,second1.y))

        if second2_alive and flap_up:
            window.blit(dove_left_up, (second2.x,second2.y))
        elif second2_alive:
            window.blit(dove_left_down, (second2.x,second2.y))

        if second3_alive and flap_up:
            window.blit(dove_left_up, (second3.x,second3.y))
        elif second3_alive:
            window.blit(dove_left_down, (second3.x,second3.y))

        if second4_alive and flap_up:
            window.blit(dove_left_up, (second4.x,second4.y))
        elif second4_alive:
            window.blit(dove_left_down, (second4.x,second4.y))

        if second5_alive and flap_up:
            window.blit(dove_left_up, (second5.x,second5.y))
        elif second5_alive:
            window.blit(dove_left_down, (second5.x,second5.y))

        if second6_alive and flap_up:
            window.blit(dove_left_up, (second6.x,second6.y))
        elif second6_alive:
            window.blit(dove_left_down, (second6.x,second6.y))




    if shot_rect.y <= 0:
      shot = False

    #Detect if a dove is shot
    if shot_rect.x >= second1.x and shot_rect.x <= second1.x+dove_w and shot_rect.y <=second1.y+dove_w and second1_alive and shot:
        shot=False
        second1_alive = False
        score += 5
    if shot_rect.x >= second2.x and shot_rect.x <= second2.x+dove_w and shot_rect.y <=second2.y+dove_w and second2_alive and shot:
        shot=False
        second2_alive = False
        score += 5
    if shot_rect.x >= second3.x and shot_rect.x <= second3.x+dove_w and shot_rect.y <=second3.y+dove_w and second3_alive and shot:
        shot=False
        second3_alive = False
        score += 5
    if shot_rect.x >= second4.x and shot_rect.x <= second4.x+dove_w and shot_rect.y <=second4.y+dove_w and second4_alive and shot:
        shot=False
        second4_alive = False
        score += 5
    if shot_rect.x >= second5.x and shot_rect.x <= second5.x+dove_w and shot_rect.y <=second5.y+dove_w and second5_alive and shot:
        shot=False
        second5_alive = False
        score += 5
    if shot_rect.x >= second6.x and shot_rect.x <= second6.x+dove_w and shot_rect.y <=second6.y+dove_w and second6_alive and shot:
        shot=False
        second6_alive = False
        score += 5
    #---ROW THREE---#

    if speed > 0:
        if third1_alive and flap_up:
            window.blit(dove_right_up, (third1.x,third1.y))
        elif third1_alive:
            window.blit(dove_right_down, (third1.x,third1.y))

        if third2_alive and flap_up:
            window.blit(dove_right_up, (third2.x,third2.y))
        elif third2_alive:
            window.blit(dove_right_down, (third2.x,third2.y))

        if third3_alive and flap_up:
            window.blit(dove_right_up, (third3.x,third3.y))
        elif third3_alive:
            window.blit(dove_right_down, (third3.x,third3.y))

        if third4_alive and flap_up:
            window.blit(dove_right_up, (third4.x,third4.y))
        elif third4_alive:
            window.blit(dove_right_down, (third4.x,third4.y))

        if third5_alive and flap_up:
            window.blit(dove_right_up, (third5.x,third5.y))
        elif third5_alive:
            window.blit(dove_right_down, (third5.x,third5.y))

        if third6_alive and flap_up:
            window.blit(dove_right_up, (third6.x,third6.y))
        elif third6_alive:
            window.blit(dove_right_down, (third6.x,third6.y))
    if speed < 0:
        if third1_alive and flap_up:
            window.blit(dove_left_up, (third1.x,third1.y))
        elif third1_alive:
            window.blit(dove_left_down, (third1.x,third1.y))

        if third2_alive and flap_up:
            window.blit(dove_left_up, (third2.x,third2.y))
        elif third2_alive:
            window.blit(dove_left_down, (third2.x,third2.y))

        if third3_alive and flap_up:
            window.blit(dove_left_up, (third3.x,third3.y))
        elif third3_alive:
            window.blit(dove_left_down, (third3.x,third3.y))

        if third4_alive and flap_up:
            window.blit(dove_left_up, (third4.x,third4.y))
        elif third4_alive:
            window.blit(dove_left_down, (third4.x,third4.y))

        if third5_alive and flap_up:
            window.blit(dove_left_up, (third5.x,third5.y))
        elif third5_alive:
            window.blit(dove_left_down, (third5.x,third5.y))

        if third6_alive and flap_up:
            window.blit(dove_left_up, (third6.x,third6.y))
        elif third6_alive:
            window.blit(dove_left_down, (third6.x,third6.y))

    #Detect if a dove is shot
    if shot_rect.x >= third1.x and shot_rect.x <= third1.x+dove_w and shot_rect.y <=third1.y+dove_w and third1_alive and shot:
        shot=False
        third1_alive = False
        score += 5
    if shot_rect.x >= third2.x and shot_rect.x <= third2.x+dove_w and shot_rect.y <=third2.y+dove_w and third2_alive and shot:
        shot=False
        third2_alive = False
        score += 5
    if shot_rect.x >= third3.x and shot_rect.x <= third3.x+dove_w and shot_rect.y <=third3.y+dove_w and third3_alive and shot:
        shot=False
        third3_alive = False
        score += 5
    if shot_rect.x >= third4.x and shot_rect.x <= third4.x+dove_w and shot_rect.y <=third4.y+dove_w and third4_alive and shot:
        shot=False
        third4_alive = False
        score += 5
    if shot_rect.x >= third5.x and shot_rect.x <= third5.x+dove_w and shot_rect.y <=third5.y+dove_w and third5_alive and shot:
        shot=False
        third5_alive = False
        score += 5
    if shot_rect.x >= third6.x and shot_rect.x <= third6.x+dove_w and shot_rect.y <=third6.y+dove_w and third6_alive and shot:
        shot=False
        third6_alive = False
        score += 5



    #---ROW FOUR---#
    if speed > 0:
        if fourth1_alive and flap_up:
            window.blit(dove_right_up, (fourth1.x,fourth1.y))
        elif fourth1_alive:
            window.blit(dove_right_down, (fourth1.x,fourth1.y))

        if fourth2_alive and flap_up:
            window.blit(dove_right_up, (fourth2.x,fourth2.y))
        elif fourth2_alive:
            window.blit(dove_right_down, (fourth2.x,fourth2.y))

        if fourth3_alive and flap_up:
            window.blit(dove_right_up, (fourth3.x,fourth3.y))
        elif fourth3_alive:
            window.blit(dove_right_down, (fourth3.x,fourth3.y))

        if fourth4_alive and flap_up:
            window.blit(dove_right_up, (fourth4.x,fourth4.y))
        elif fourth4_alive:
            window.blit(dove_right_down, (fourth4.x,fourth4.y))

        if fourth5_alive and flap_up:
            window.blit(dove_right_up, (fourth5.x,fourth5.y))
        elif fourth5_alive:
            window.blit(dove_right_down, (fourth5.x,fourth5.y))

        if fourth6_alive and flap_up:
            window.blit(dove_right_up, (fourth6.x,fourth6.y))
        elif fourth6_alive:
            window.blit(dove_right_down, (fourth6.x,fourth6.y))
    if speed < 0:
        if fourth1_alive and flap_up:
            window.blit(dove_left_up, (fourth1.x,fourth1.y))
        elif fourth1_alive:
            window.blit(dove_left_down, (fourth1.x,fourth1.y))

        if fourth2_alive and flap_up:
            window.blit(dove_left_up, (fourth2.x,fourth2.y))
        elif fourth2_alive:
            window.blit(dove_left_down, (fourth2.x,fourth2.y))

        if fourth3_alive and flap_up:
            window.blit(dove_left_up, (fourth3.x,fourth3.y))
        elif fourth3_alive:
            window.blit(dove_left_down, (fourth3.x,fourth3.y))

        if fourth4_alive and flap_up:
            window.blit(dove_left_up, (fourth4.x,fourth4.y))
        elif fourth4_alive:
            window.blit(dove_left_down, (fourth4.x,fourth4.y))

        if fourth5_alive and flap_up:
            window.blit(dove_left_up, (fourth5.x,fourth5.y))
        elif fourth5_alive:
            window.blit(dove_left_down, (fourth5.x,fourth5.y))

        if fourth6_alive and flap_up:
            window.blit(dove_left_up, (fourth6.x,fourth6.y))
        elif fourth6_alive:
            window.blit(dove_left_down, (fourth6.x,fourth6.y))

    #Detect if a dove is shot
    if shot_rect.x >= fourth1.x and shot_rect.x <= fourth1.x+dove_w and shot_rect.y <=fourth1.y+dove_w and fourth1_alive and shot:
        shot=False
        fourth1_alive = False
        score += 5
    if shot_rect.x >= fourth2.x and shot_rect.x <= fourth2.x+dove_w and shot_rect.y <=fourth2.y+dove_w and fourth2_alive and shot:
        shot=False
        fourth2_alive = False
        score += 5
    if shot_rect.x >= fourth3.x and shot_rect.x <= fourth3.x+dove_w and shot_rect.y <=fourth3.y+dove_w and fourth3_alive and shot:
        shot=False
        fourth3_alive = False
        score += 5
    if shot_rect.x >= fourth4.x and shot_rect.x <= fourth4.x+dove_w and shot_rect.y <=fourth4.y+dove_w and fourth4_alive and shot:
        shot=False
        fourth4_alive = False
        score += 5
    if shot_rect.x >= fourth5.x and shot_rect.x <= fourth5.x+dove_w and shot_rect.y <=fourth5.y+dove_w and fourth5_alive and shot:
        shot=False
        fourth5_alive = False
        score += 5
    if shot_rect.x >= fourth6.x and shot_rect.x <= fourth6.x+dove_w and shot_rect.y <=fourth6.y+dove_w and fourth6_alive and shot:
        shot=False
        fourth6_alive = False
        score += 5



    if shot:
        if shot_timer < 10:
            window.blit(shot0,(shot_rect.x,shot_rect.y))
        shot_rect.y -= 10
        shot_timer += 1
        if shot_timer >= 10:
            window.blit(shot1,(shot_rect.x,shot_rect.y))
    elif not shot:
        shot_rect = pygame.Rect(-100,-100,15,25)
        shot_timer = 0
    if move_timer == 0:
        jim_move = not jim_move
        move_timer = 25
    if poop_rect.y <= player.y:
        poop_rect.y += 10
        window.blit(poop,(poop_rect.x,poop_rect.y))
    if poop_rect.x >= player.x and poop_rect.x <= player.x + jim_w and poop_rect.y >= player.y + 10:
        pygame.mixer.Sound.play(get_hit)



    if jim_move and going_right:
        jim = pygame.image.load('images/jim_right_2.png')
    elif not jim_move and going_right:
        jim = pygame.image.load('images/jim_right_1.png')


    elif jim_move:
        jim = pygame.image.load('images/jim_left_2.png')
    elif not jim_move:
        jim = pygame.image.load('images/jim_left_1.png')
    if score > 0:
        pygame.mixer.Sound.play(score_sound)
    digit3 += score
    if digit3 > 5:
        digit3 = 0
        digit2 += 1
    if digit2 > 9:
        digit2 = 0
        digit1 += 1
    score = 0
    scoretext = font.render('SCORE: ' + str(digit1) + str(digit2) + str(digit3) , False, (255,255,255))
    window.blit(jim, (player.x,player.y))
    window.blit(curtains,(0,0))
    window.blit(scoretext,(0,0))

    pygame.display.flip()
    c.tick(60)
