#coding:utf-8
import pygame, random, os
from pygame.locals import *
from time import sleep
from math import sqrt
pygame.init()

game_dir = os.getcwd()

level_look_00 = pygame.font.SysFont('华文楷体', 100)
game_over_1 = pygame.font.SysFont('华文楷体', 70)
def quit_game():
    screen.fill(white)
    text = level_look_00.render('ヾ•ω•`o拜拜！', True, (black))
    screen.blit(text, (120, 40))
    pygame.display.update()
    sleep(0.5)
    pygame.quit()
    quit()

clock = pygame.time.Clock()
white = 255, 255, 255
black =   0,   0,   0
green =  84, 255, 159
yellow = 255, 218, 185
blue = 0, 255, 255
red = 255,   0,   0

dir_1 = os.path.isdir(f'{game_dir}\\字体')
if dir_1 == False:
    while True:
        print('回避（错误）：遗失字体文件夹')
        sleep(666666)
font_1 = os.path.exists(f'{game_dir}\\字体\\华文楷体.TTF')
font_2 = os.path.exists(f'{game_dir}\\字体\\华文行楷.TTF')
if font_1 == False or font_2 == False:
    while True:
        print('回避（错误）：遗失游戏内字体')
        sleep(666666)

dir_2 = os.path.isdir(f'{game_dir}\\图片')
if dir_2 == False:
    screen = pygame.display.set_mode((800 , 200))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    quit_game()

                elif event.key == K_ESCAPE:
                    quit_game()
        clock.tick(3)
        screen.fill(white)
        pygame.display.set_caption('回避（错误）')
        text = level_look_00.render('遗失图片文件夹', True, (red))
        screen.blit(text, (46, 20))
        pygame.display.update()
image_1 = os.path.exists(f'{game_dir}\\图片\\图标.png')
image_2 = os.path.exists(f'{game_dir}\\图片\\背景图.png')
image_3 = os.path.exists(f'{game_dir}\\图片\\zeus.png')
image_4 = os.path.exists(f'{game_dir}\\图片\\背景.png')
image_5 = os.path.exists(f'{game_dir}\\图片\\金币.png')
image_6 = os.path.exists(f'{game_dir}\\图片\\暂停.png')
image_7 = os.path.exists(f'{game_dir}\\图片\\减速.png')
image_8 = os.path.exists(f'{game_dir}\\图片\\减速1.png')
image_9 = os.path.exists(f'{game_dir}\\图片\\回复.png')
image_10 = os.path.exists(f'{game_dir}\\图片\\回复1.png')
image_11 = os.path.exists(f'{game_dir}\\图片\\地刺.png')
image_12 = os.path.exists(f'{game_dir}\\图片\\激光.png')
image_13 = os.path.exists(f'{game_dir}\\图片\\激光攻击.png')
image_14 = os.path.exists(f'{game_dir}\\图片\\玩家1.png')
image_15 = os.path.exists(f'{game_dir}\\图片\\玩家2.png')
image_16 = os.path.exists(f'{game_dir}\\图片\\玩家3.png')
image_17 = os.path.exists(f'{game_dir}\\图片\\玩家4.png')
image_18 = os.path.exists(f'{game_dir}\\图片\\玩家坠毁1.png')
image_19 = os.path.exists(f'{game_dir}\\图片\\玩家坠毁2.png')
image_20 = os.path.exists(f'{game_dir}\\图片\\玩家坠毁3.png')
image_21 = os.path.exists(f'{game_dir}\\图片\\速度.png')
image_22 = os.path.exists(f'{game_dir}\\图片\\速度1.png')
image_23 = os.path.exists(f'{game_dir}\\图片\\金币.png')
image_24 = os.path.exists(f'{game_dir}\\图片\\金币翻倍.png')
image_25 = os.path.exists(f'{game_dir}\\图片\\金币翻倍1.png')
image_26 = os.path.exists(f'{game_dir}\\图片\\长块.png')
if image_1 == False or image_2 == False or image_3 == False or image_4 == False or image_5 == False or image_6 == False or image_7 == False or image_8 == False or image_9 == False or image_10 == False or image_11 == False or image_12 == False or image_13 == False or image_14 == False or image_15 == False or image_16 == False or image_17 == False or image_18 == False or image_19 == False or image_20 == False or image_21 == False or image_22 == False or image_23 == False or image_24 == False or image_25 == False or image_26 == False:
    screen = pygame.display.set_mode((800 , 200))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    quit_game()

                elif event.key == K_ESCAPE:
                    quit_game()
        clock.tick(3)
        screen.fill(white)
        pygame.display.set_caption('回避（错误）')
        text = level_look_00.render('遗失游戏内图片', True, (red))
        screen.blit(text, (46, 20))
        pygame.display.update()

dir_3 = os.path.isdir(f'{game_dir}\\音乐')
if dir_3 == False:
    screen = pygame.display.set_mode((800 , 200))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    quit_game()

                elif event.key == K_ESCAPE:
                    quit_game()
        clock.tick(3)
        screen.fill(white)
        pygame.display.set_caption('回避（错误）')
        text = level_look_00.render('遗失音乐文件夹', True, (red))
        screen.blit(text, (46, 20))
        pygame.display.update()
sound_1 = os.path.exists(f'{game_dir}\\音乐\\游戏点击音效.wav')
sound_2 = os.path.exists(f'{game_dir}\\音乐\\游戏结束！.wav')
sound_3 = os.path.exists(f'{game_dir}\\音乐\\游戏音乐.wav')
sound_4 = os.path.exists(f'{game_dir}\\音乐\\获胜.wav')
if sound_1 == False or sound_2 == False or sound_3 == False or sound_4 == False:
    screen = pygame.display.set_mode((800 , 200))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    quit_game()

                elif event.key == K_ESCAPE:
                    quit_game()
        if sound_3 == False and sound_4 == True and sound_2 == True and sound_1 == True:
            clock.tick(3)
            screen.fill(white)
            pygame.display.set_caption('回避（错误）')
            text = level_look_00.render('遗失游戏内音乐', True, (red))
            screen.blit(text, (46, 20))
            pygame.display.update()
        else:
            clock.tick(3)
            screen.fill(white)
            pygame.display.set_caption('回避（错误）')
            text = game_over_1.render('遗失音乐（音效）文件', True, (red))
            screen.blit(text, (46, 20))
            pygame.display.update()

game_text_1 = os.path.exists(f'{game_dir}\\save_1.py')
game_text_2 = os.path.exists(f'{game_dir}\\save_2.py')
game_text_3 = os.path.exists(f'{game_dir}\\save_3.py')
game_text_4 = os.path.exists(f'{game_dir}\\game_save.py')
if game_text_1 == False or game_text_2 == False or game_text_3 == False or game_text_4 == False:
    screen = pygame.display.set_mode((800 , 200))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    quit_game()

                elif event.key == K_ESCAPE:
                    quit_game()
            clock.tick(3)
            screen.fill(white)
            pygame.display.set_caption('回避（错误）')
            text = level_look_00.render('遗失游戏内存档', True, (red))
            screen.blit(text, (46, 20))
            pygame.display.update()


screen = pygame.display.set_mode((800 , 600))
screen.fill(white)
game_over_1 = pygame.font.SysFont('华文楷体', 50)
text = game_over_1.render('ZEUS', True, (blue))
pygame.display.set_caption('回避')
icon_img = pygame.image.load('图片\图标.png')
zeus_img = pygame.image.load('图片\zeus.png')
pygame.display.set_icon(icon_img)
screen.blit(zeus_img, (330, 200))
screen.blit(text, (335, 320))
pygame.display.update()
ko = True
clock_2 = pygame.time.Clock()
clock_3 = 0
while ko:
    clock_3 += clock_2.tick()
    for event in pygame.event.get():
        if event.type == QUIT:
            quit_game()
        elif event.type == KEYDOWN:
            if event.key == ord('r'):
                quit_game()
            elif event.key == ESCAPE:
                quit_game()
    if clock_3 >= 300 and clock_3 <= 400:
        ko = False
ko = True
c = False
user = True
read_ok = False
def save():
    global save_open
    if user == True:
        save_open = open('save_1.py', 'w')

    elif user_2 == True:
        save_open = open('save_2.py', 'w')

    elif user_3 == True:
        save_open = open('save_3.py', 'w')
    save_open.write(f'''#coding:cp936
name = \'{name}\'
fps = {fps_1}
tips = {tips_1}
sound = {sound_1}
sound_4 = {sound_4}
coins = {coins}
player_speed_3 = {player_speed_3}
hp_2 = {hp_2}
player_speed = {player_speed}
hp = {hp_3}
die_number = {die_number}
e = {e}
open_level = {open_level}
level_ok_number = {level_ok_number}
first_open_game = {first_open_game}
save_name_true = {save_name_true}

first_cheng_jiu_open = {first_cheng_jiu_open}
first_shop_open = {first_shop_open}
first_upgrade_open = {first_upgrade_open}
first_tong_ji_open = {first_tong_ji_open}
first_dui_huan_open = {first_dui_huan_open}

first_enter_cheng_jiu = {first_enter_cheng_jiu}
first_enter_shop = {first_enter_shop}
first_enter_upgrade = {first_enter_upgrade}
first_enter_tong_ji = {first_enter_tong_ji}
first_enter_dui_huan = {first_enter_dui_huan}

cheng_jiu_open = {cheng_jiu_open}
shop_open = {shop_open}
upgrade_open = {upgrade_open}
tong_ji_open = {tong_ji_open}
dui_huan_open = {dui_huan_open}

su_du_upgrade_number = {su_du_upgrade_number}
hp_upgrade_number = {hp_upgrade_number}
upgrade_number = {upgrade_number}

dao_ju_hp_level = {dao_ju_hp_level}
dao_ju_su_du_level = {dao_ju_su_du_level}
dao_ju_lower_level = {dao_ju_lower_level}
dao_ju_coins_two_level = {dao_ju_coins_two_level}

hui_fu_number = {hui_fu_number}
su_du_number = {su_du_number}
lower_number = {lower_number}
coins_two_number = {coins_two_number}

starts = {starts}
starts_open_1 = {starts_open_1}
starts_open_2 = {starts_open_2}
starts_open_3 = {starts_open_3}
starts_open_4 = {starts_open_4}
starts_open_5 = {starts_open_5}

cheng_jiu_cishu_1 = {cheng_jiu_cishu_1}
cheng_jiu_cishu_2 = {cheng_jiu_cishu_2}
cheng_jiu_cishu_3 = {cheng_jiu_cishu_3}
cheng_jiu_cishu_4 = {cheng_jiu_cishu_4}
cheng_jiu_cishu_5 = {cheng_jiu_cishu_5}
cheng_jiu_cishu_6 = {cheng_jiu_cishu_6}
cheng_jiu_cishu_7 = {cheng_jiu_cishu_7}
cheng_jiu_cishu_8 = {cheng_jiu_cishu_8}
cheng_jiu_cishu_9 = {cheng_jiu_cishu_9}
cheng_jiu_cishu_10 = {cheng_jiu_cishu_10}
cheng_jiu_cishu_11 = {cheng_jiu_cishu_11}
cheng_jiu_cishu_12 = {cheng_jiu_cishu_12}
cheng_jiu_cishu_13 = {cheng_jiu_cishu_13}
cheng_jiu_cishu_14 = {cheng_jiu_cishu_14}

coins_dui_huan_1 = {coins_dui_huan_1}
coins_dui_huan_2 = {coins_dui_huan_2}
coins_dui_huan_3 = {coins_dui_huan_3}
coins_dui_huan_4 = {coins_dui_huan_4}
coins_dui_huan_5 = {coins_dui_huan_5}
coins_dui_huan_6 = {coins_dui_huan_6}
coins_dui_huan_7 = {coins_dui_huan_7}
coins_dui_huan_8 = {coins_dui_huan_8}
coins_dui_huan_9 = {coins_dui_huan_9}
coins_dui_huan_10 = {coins_dui_huan_10}
coins_dui_huan_11 = {coins_dui_huan_11}

first_level_1 = {first_level_1}
first_level_2 = {first_level_2}
first_level_3 = {first_level_3}
first_level_4 = {first_level_4}
first_level_5 = {first_level_5}

tong_guan_1 = {tong_guan_1}
tong_guan_2 = {tong_guan_2}
tong_guan_3 = {tong_guan_3}
tong_guan_4 = {tong_guan_4}
tong_guan_5 = {tong_guan_5}

donut_open = {donut_open}
level_1_donut = {level_1_donut}
level_2_donut = {level_2_donut}
level_3_donut = {level_3_donut}
level_4_donut = {level_4_donut}
level_5_donut = {level_5_donut}''')
    save_open.close()

    save_open_2 = open('game_save.py', 'w')
    save_open_2.write(f'default_save_name = {default_save_name}')
    save_open_2.close()

def default_save_name_pan_duan():
    import game_save
    global default_save_name, user, user_2, user_3
    default_save_name = game_save.default_save_name
    if default_save_name == 1:
        user = True
        user_2 = False
        user_3 = False
    elif default_save_name == 2:
        user = False
        user_2 = True
        user_3 = False
    elif default_save_name == 3:
        user = False
        user_2 = False
        user_3 = True

def user_pan_duan():
    global name, player_speed, player_speed_00, player_speed_4, fps, fps_1, sound, sound_1, sound_4, sound_5, hp, hp_3, hp_00, coins, die_number, e, open_level, level_ok_number, starts, starts_open_1, starts_open_2, starts_open_3, starts_open_4, starts_open_5, cheng_jiu_cishu_1, cheng_jiu_cishu_2, cheng_jiu_cishu_3, cheng_jiu_cishu_4, cheng_jiu_cishu_5, cheng_jiu_cishu_6, cheng_jiu_cishu_7, cheng_jiu_cishu_8, cheng_jiu_cishu_9, cheng_jiu_cishu_10, cheng_jiu_cishu_11, cheng_jiu_cishu_12, cheng_jiu_cishu_13, cheng_jiu_cishu_14, coins_dui_huan_1, coins_dui_huan_2, coins_dui_huan_3, coins_dui_huan_4, coins_dui_huan_5, coins_dui_huan_6, coins_dui_huan_7, coins_dui_huan_8, coins_dui_huan_9, coins_dui_huan_10, coins_dui_huan_11, first_level_1, first_level_2, first_level_3, first_level_4, first_level_5, tips, tips_1, player_speed_3, hp_2, tong_guan_1, tong_guan_2, tong_guan_3, tong_guan_4, tong_guan_5, su_du_upgrade_number, hp_upgrade_number, upgrade_number, hui_fu_number, su_du_number, lower_number, coins_two_number, dao_ju_hp_level, dao_ju_su_du_level, dao_ju_lower_level, dao_ju_coins_two_level, read_ok, first_cheng_jiu_open, first_shop_open, first_upgrade_open, first_tong_ji_open, first_dui_huan_open, first_enter_cheng_jiu, first_enter_shop, first_enter_upgrade, first_enter_tong_ji, first_enter_dui_huan, cheng_jiu_open, shop_open, upgrade_open, tong_ji_open, dui_huan_open, first_open_game, save_name_true, donut_open, level_1_donut, level_2_donut, level_3_donut, level_4_donut, level_5_donut
    import save_1, save_2, save_3
    default_save_name_pan_duan()
    if user == True:
        name = save_1.name
        player_speed = save_1.player_speed
        player_speed_00 = save_1.player_speed
        player_speed_4 = save_1.player_speed
        fps = save_1.fps
        fps_1 = save_1.fps
        sound = save_1.sound
        sound_1 = save_1.sound
        sound_4 = save_1.sound_4
        sound_5 = save_1.sound_4
        hp = save_1.hp
        hp_3 = save_1.hp
        hp_00 = save_1.hp
        coins = save_1.coins
        die_number = save_1.die_number
        e = save_1.e
        open_level = save_1.open_level
        level_ok_number = save_1.level_ok_number
        first_open_game = save_1.first_open_game
        save_name_true = save_1.save_name_true

        first_cheng_jiu_open = save_1.first_cheng_jiu_open
        first_shop_open = save_1.first_shop_open
        first_upgrade_open = save_1.first_upgrade_open
        first_tong_ji_open = save_1.first_tong_ji_open
        first_dui_huan_open = save_1.first_dui_huan_open
        
        first_enter_cheng_jiu = save_1.first_enter_cheng_jiu
        first_enter_shop = save_1.first_enter_shop
        first_enter_upgrade = save_1.first_enter_upgrade
        first_enter_tong_ji = save_1.first_enter_tong_ji
        first_enter_dui_huan = save_1.first_enter_dui_huan

        cheng_jiu_open = save_1.cheng_jiu_open
        shop_open = save_1.shop_open
        upgrade_open = save_1.upgrade_open
        tong_ji_open = save_1.tong_ji_open
        dui_huan_open = save_1.dui_huan_open

        starts = save_1.starts
        starts_open_1 = save_1.starts_open_1
        starts_open_2 = save_1.starts_open_2
        starts_open_3 = save_1.starts_open_3
        starts_open_4 = save_1.starts_open_4
        starts_open_5 = save_1.starts_open_5

        cheng_jiu_cishu_1 = save_1.cheng_jiu_cishu_1
        cheng_jiu_cishu_2 = save_1.cheng_jiu_cishu_2
        cheng_jiu_cishu_3 = save_1.cheng_jiu_cishu_3
        cheng_jiu_cishu_4 = save_1.cheng_jiu_cishu_4
        cheng_jiu_cishu_5 = save_1.cheng_jiu_cishu_5
        cheng_jiu_cishu_6 = save_1.cheng_jiu_cishu_6
        cheng_jiu_cishu_7 = save_1.cheng_jiu_cishu_7
        cheng_jiu_cishu_8 = save_1.cheng_jiu_cishu_8
        cheng_jiu_cishu_9 = save_1.cheng_jiu_cishu_9
        cheng_jiu_cishu_10 = save_1.cheng_jiu_cishu_10
        cheng_jiu_cishu_11 = save_1.cheng_jiu_cishu_11
        cheng_jiu_cishu_12 = save_1.cheng_jiu_cishu_12
        cheng_jiu_cishu_13 = save_1.cheng_jiu_cishu_13
        cheng_jiu_cishu_14 = save_1.cheng_jiu_cishu_14

        coins_dui_huan_1 = save_1.coins_dui_huan_1
        coins_dui_huan_2 = save_1.coins_dui_huan_2
        coins_dui_huan_3 = save_1.coins_dui_huan_3
        coins_dui_huan_4 = save_1.coins_dui_huan_4
        coins_dui_huan_5 = save_1.coins_dui_huan_5
        coins_dui_huan_6 = save_1.coins_dui_huan_6
        coins_dui_huan_7 = save_1.coins_dui_huan_7
        coins_dui_huan_8 = save_1.coins_dui_huan_8
        coins_dui_huan_9 = save_1.coins_dui_huan_9
        coins_dui_huan_10 = save_1.coins_dui_huan_10
        coins_dui_huan_11 = save_1.coins_dui_huan_11

        first_level_1 = save_1.first_level_1
        first_level_2 = save_1.first_level_2
        first_level_3 = save_1.first_level_3
        first_level_4 = save_1.first_level_4
        first_level_5 = save_1.first_level_5

        tips = save_1.tips
        tips_1 = save_1.tips
        player_speed_3 = save_1.player_speed_3
        hp_2 = save_1.hp_2

        tong_guan_1 = save_1.tong_guan_1
        tong_guan_2 = save_1.tong_guan_2
        tong_guan_3 = save_1.tong_guan_3
        tong_guan_4 = save_1.tong_guan_4
        tong_guan_5 = save_1.tong_guan_5

        su_du_upgrade_number = save_1.su_du_upgrade_number
        hp_upgrade_number = save_1.hp_upgrade_number
        upgrade_number = save_1.upgrade_number

        hui_fu_number = save_1.hui_fu_number
        su_du_number = save_1.su_du_number
        lower_number = save_1.lower_number
        coins_two_number = save_1.coins_two_number

        dao_ju_hp_level = save_1.dao_ju_hp_level
        dao_ju_su_du_level = save_1.dao_ju_su_du_level
        dao_ju_lower_level = save_1.dao_ju_lower_level
        dao_ju_coins_two_level = save_1.dao_ju_coins_two_level
        
        donut_open = save_1.donut_open
        level_1_donut = save_1.level_1_donut
        level_2_donut = save_1.level_2_donut
        level_3_donut = save_1.level_3_donut
        level_4_donut = save_1.level_4_donut
        level_5_donut = save_1.level_5_donut
        
        read_ok = True
        save()

    elif user_2 == True:
        name = save_2.name
        player_speed = save_2.player_speed
        player_speed_00 = save_2.player_speed
        player_speed_4 = save_2.player_speed
        fps = save_2.fps
        fps_1 = save_2.fps
        sound = save_2.sound
        sound_1 = save_2.sound
        sound_4 = save_2.sound_4
        sound_5 = save_2.sound_4
        hp = save_2.hp
        hp_3 = save_2.hp
        hp_00 = save_2.hp
        coins = save_2.coins
        die_number = save_2.die_number
        e = save_2.e
        open_level = save_2.open_level
        level_ok_number = save_2.level_ok_number
        first_open_game = save_2.first_open_game
        save_name_true = save_2.save_name_true

        first_cheng_jiu_open = save_2.first_cheng_jiu_open
        first_shop_open = save_2.first_shop_open
        first_upgrade_open = save_2.first_upgrade_open
        first_tong_ji_open = save_2.first_tong_ji_open
        first_dui_huan_open = save_2.first_dui_huan_open
        
        first_enter_cheng_jiu = save_2.first_enter_cheng_jiu
        first_enter_shop = save_2.first_enter_shop
        first_enter_upgrade = save_2.first_enter_upgrade
        first_enter_tong_ji = save_2.first_enter_tong_ji
        first_enter_dui_huan = save_2.first_enter_dui_huan

        cheng_jiu_open = save_2.cheng_jiu_open
        shop_open = save_2.shop_open
        upgrade_open = save_2.upgrade_open
        tong_ji_open = save_2.tong_ji_open
        dui_huan_open = save_2.dui_huan_open

        starts = save_2.starts
        starts_open_1 = save_2.starts_open_1
        starts_open_2 = save_2.starts_open_2
        starts_open_3 = save_2.starts_open_3
        starts_open_4 = save_2.starts_open_4
        starts_open_5 = save_2.starts_open_5

        cheng_jiu_cishu_1 = save_2.cheng_jiu_cishu_1
        cheng_jiu_cishu_2 = save_2.cheng_jiu_cishu_2
        cheng_jiu_cishu_3 = save_2.cheng_jiu_cishu_3
        cheng_jiu_cishu_4 = save_2.cheng_jiu_cishu_4
        cheng_jiu_cishu_5 = save_2.cheng_jiu_cishu_5
        cheng_jiu_cishu_6 = save_2.cheng_jiu_cishu_6
        cheng_jiu_cishu_7 = save_2.cheng_jiu_cishu_7
        cheng_jiu_cishu_8 = save_2.cheng_jiu_cishu_8
        cheng_jiu_cishu_9 = save_2.cheng_jiu_cishu_9
        cheng_jiu_cishu_10 = save_2.cheng_jiu_cishu_10
        cheng_jiu_cishu_11 = save_2.cheng_jiu_cishu_11
        cheng_jiu_cishu_12 = save_2.cheng_jiu_cishu_12
        cheng_jiu_cishu_13 = save_2.cheng_jiu_cishu_13
        cheng_jiu_cishu_14 = save_2.cheng_jiu_cishu_14

        coins_dui_huan_1 = save_2.coins_dui_huan_1
        coins_dui_huan_2 = save_2.coins_dui_huan_2
        coins_dui_huan_3 = save_2.coins_dui_huan_3
        coins_dui_huan_4 = save_2.coins_dui_huan_4
        coins_dui_huan_5 = save_2.coins_dui_huan_5
        coins_dui_huan_6 = save_2.coins_dui_huan_6
        coins_dui_huan_7 = save_2.coins_dui_huan_7
        coins_dui_huan_8 = save_2.coins_dui_huan_8
        coins_dui_huan_9 = save_2.coins_dui_huan_9
        coins_dui_huan_10 = save_2.coins_dui_huan_10
        coins_dui_huan_11 = save_2.coins_dui_huan_11

        first_level_1 = save_2.first_level_1
        first_level_2 = save_2.first_level_2
        first_level_3 = save_2.first_level_3
        first_level_4 = save_2.first_level_4
        first_level_5 = save_2.first_level_5

        tips = save_2.tips
        tips_1 = save_2.tips
        player_speed_3 = save_2.player_speed_3
        hp_2 = save_2.hp_2

        tong_guan_1 = save_2.tong_guan_1
        tong_guan_2 = save_2.tong_guan_2
        tong_guan_3 = save_2.tong_guan_3
        tong_guan_4 = save_2.tong_guan_4
        tong_guan_5 = save_2.tong_guan_5

        su_du_upgrade_number = save_2.su_du_upgrade_number
        hp_upgrade_number = save_2.hp_upgrade_number
        upgrade_number = save_2.upgrade_number

        hui_fu_number = save_2.hui_fu_number
        su_du_number = save_2.su_du_number
        lower_number = save_2.lower_number
        coins_two_number = save_2.coins_two_number

        dao_ju_hp_level = save_2.dao_ju_hp_level
        dao_ju_su_du_level = save_2.dao_ju_su_du_level
        dao_ju_lower_level = save_2.dao_ju_lower_level
        dao_ju_coins_two_level = save_2.dao_ju_coins_two_level
        
        donut_open = save_2.donut_open
        level_1_donut = save_2.level_1_donut
        level_2_donut = save_2.level_2_donut
        level_3_donut = save_2.level_3_donut
        level_4_donut = save_2.level_4_donut
        level_5_donut = save_2.level_5_donut
        
        read_ok = True
        save()

    elif user_3 == True:
        name = save_3.name
        player_speed = save_3.player_speed
        player_speed_00 = save_3.player_speed
        player_speed_4 = save_3.player_speed
        fps = save_3.fps
        fps_1 = save_3.fps
        sound = save_3.sound
        sound_1 = save_3.sound
        sound_4 = save_3.sound_4
        sound_5 = save_3.sound_4
        hp = save_3.hp
        hp_3 = save_3.hp
        hp_00 = save_3.hp
        coins = save_3.coins
        die_number = save_3.die_number
        e = save_3.e
        open_level = save_3.open_level
        level_ok_number = save_3.level_ok_number
        first_open_game = save_3.first_open_game
        save_name_true = save_3.save_name_true

        first_cheng_jiu_open = save_3.first_cheng_jiu_open
        first_shop_open = save_3.first_shop_open
        first_upgrade_open = save_3.first_upgrade_open
        first_tong_ji_open = save_3.first_tong_ji_open
        first_dui_huan_open = save_3.first_dui_huan_open

        cheng_jiu_open = save_3.cheng_jiu_open
        shop_open = save_3.shop_open
        upgrade_open = save_3.upgrade_open
        tong_ji_open = save_3.tong_ji_open
        dui_huan_open = save_3.dui_huan_open
        
        first_enter_cheng_jiu = save_3.first_enter_cheng_jiu
        first_enter_shop = save_3.first_enter_shop
        first_enter_upgrade = save_3.first_enter_upgrade
        first_enter_tong_ji = save_3.first_enter_tong_ji
        first_enter_dui_huan = save_3.first_enter_dui_huan

        starts = save_3.starts
        starts_open_1 = save_3.starts_open_1
        starts_open_2 = save_3.starts_open_2
        starts_open_3 = save_3.starts_open_3
        starts_open_4 = save_3.starts_open_4
        starts_open_5 = save_3.starts_open_5

        cheng_jiu_cishu_1 = save_3.cheng_jiu_cishu_1
        cheng_jiu_cishu_2 = save_3.cheng_jiu_cishu_2
        cheng_jiu_cishu_3 = save_3.cheng_jiu_cishu_3
        cheng_jiu_cishu_4 = save_3.cheng_jiu_cishu_4
        cheng_jiu_cishu_5 = save_3.cheng_jiu_cishu_5
        cheng_jiu_cishu_6 = save_3.cheng_jiu_cishu_6
        cheng_jiu_cishu_7 = save_3.cheng_jiu_cishu_7
        cheng_jiu_cishu_8 = save_3.cheng_jiu_cishu_8
        cheng_jiu_cishu_9 = save_3.cheng_jiu_cishu_9
        cheng_jiu_cishu_10 = save_3.cheng_jiu_cishu_10
        cheng_jiu_cishu_11 = save_3.cheng_jiu_cishu_11
        cheng_jiu_cishu_12 = save_3.cheng_jiu_cishu_12
        cheng_jiu_cishu_13 = save_3.cheng_jiu_cishu_13
        cheng_jiu_cishu_14 = save_3.cheng_jiu_cishu_14

        coins_dui_huan_1 = save_3.coins_dui_huan_1
        coins_dui_huan_2 = save_3.coins_dui_huan_2
        coins_dui_huan_3 = save_3.coins_dui_huan_3
        coins_dui_huan_4 = save_3.coins_dui_huan_4
        coins_dui_huan_5 = save_3.coins_dui_huan_5
        coins_dui_huan_6 = save_3.coins_dui_huan_6
        coins_dui_huan_7 = save_3.coins_dui_huan_7
        coins_dui_huan_8 = save_3.coins_dui_huan_8
        coins_dui_huan_9 = save_3.coins_dui_huan_9
        coins_dui_huan_10 = save_3.coins_dui_huan_10
        coins_dui_huan_11 = save_3.coins_dui_huan_11

        first_level_1 = save_3.first_level_1
        first_level_2 = save_3.first_level_2
        first_level_3 = save_3.first_level_3
        first_level_4 = save_3.first_level_4
        first_level_5 = save_3.first_level_5

        tips = save_3.tips
        tips_1 = save_3.tips
        player_speed_3 = save_3.player_speed_3
        hp_2 = save_3.hp_2

        tong_guan_1 = save_3.tong_guan_1
        tong_guan_2 = save_3.tong_guan_2
        tong_guan_3 = save_3.tong_guan_3
        tong_guan_4 = save_3.tong_guan_4
        tong_guan_5 = save_3.tong_guan_5

        su_du_upgrade_number = save_3.su_du_upgrade_number
        hp_upgrade_number = save_3.hp_upgrade_number
        upgrade_number = save_3.upgrade_number

        hui_fu_number = save_3.hui_fu_number
        su_du_number = save_3.su_du_number
        lower_number = save_3.lower_number
        coins_two_number = save_3.coins_two_number

        dao_ju_hp_level = save_3.dao_ju_hp_level
        dao_ju_su_du_level = save_3.dao_ju_su_du_level
        dao_ju_lower_level = save_3.dao_ju_lower_level
        dao_ju_coins_two_level = save_3.dao_ju_coins_two_level

        donut_open = save_3.donut_open
        level_1_donut = save_3.level_1_donut
        level_2_donut = save_3.level_2_donut
        level_3_donut = save_3.level_3_donut
        level_4_donut = save_3.level_4_donut
        level_5_donut = save_3.level_5_donut

        read_ok = True
        save()



if read_ok == False:
    user_pan_duan()
d_2 = '升级后购买所需金币加8'
e_2 = '购买所需金币64枚'

ticks = 0
player_X = 360
player_Y = 478
player_x = 0
player_y = 0
score = 0
hp_coloer = green
hp_upgrade_coins = 125
cheng_jiu_1_coins = 0
cheng_jiu_1a_coins = 0
dici_zhong_lei = 0
level_tips_4 = '0'
dici_number = 0
dici_2_number = 0
dici_3_number = 0
home = False
wins = False
game_overs = False
open_block_ok = False

hp_zeng_jia = 1
hui_fu_coins = 48
su_du_zeng_jia = 1
su_du_coins = 48
lower_jian_shao = 1
lower_coins = 48
coins_two_zeng_jia = 2
if tong_guan_5 == True:
    coins_two_coins = 24

else:
    coins_two_coins = 6
hui_fu_ci_shu = 0
su_du_ci_shu = 0
lower_ci_shu = 0
coins_two_ci_shu = 0
coins_two = False

level_1 = False
level_2 = False
level_3 = False
level_4 = False
level_5 = False

ok = False
ok_2 = False
ok_3 = False
ok_4 = False
ok_5 = False

cheng_jiu_donut = False
shop_donut = False
upgrade_donut = False
tong_ji_donut = False
dui_huan_donut = False

bg_img_2 = pygame.image.load('图片\背景.png')
coins_img = pygame.image.load('图片\金币.png')
tong_guan_img = pygame.image.load('图片\ok.png')
player_img = pygame.image.load('图片\玩家1.png')
player_img_2 = pygame.image.load('图片\玩家2.png')
player_img_3 = pygame.image.load('图片\玩家3.png')
player_img_4 = pygame.image.load('图片\玩家4.png')
player_ko_1 = pygame.image.load('图片\玩家坠毁1.png')
player_ko_2 = pygame.image.load('图片\玩家坠毁2.png')
player_ko_3 = pygame.image.load('图片\玩家坠毁3.png')
bg_img = pygame.image.load('图片\背景图.png')
stop_game = pygame.image.load('图片\暂停.png')

hui_fu_img = pygame.image.load('图片\回复.png')
hui_fu_2_img = pygame.image.load('图片\回复1.png')
su_du_img = pygame.image.load('图片\速度.png')
su_du_2_img = pygame.image.load('图片\速度1.png')
lower_img = pygame.image.load('图片\减速.png')
lower_2_img = pygame.image.load('图片\减速1.png')
coins_two_img = pygame.image.load('图片\金币翻倍.png')
coins_two_2_img = pygame.image.load('图片\金币翻倍1.png')

pygame.mixer.music.load('音乐\游戏音乐.wav')
dianji = pygame.mixer.Sound('音乐\游戏点击音效.wav')
win_sound = pygame.mixer.Sound('音乐\获胜.wav')
game_over_sound = pygame.mixer.Sound('音乐\游戏结束！.wav')

pygame.mixer.music.set_volume(sound_4)
dianji.set_volume(sound)
win_sound.set_volume(sound)
game_over_sound.set_volume(sound)

pygame.mixer.music.play(-1)

title = pygame.font.SysFont('华文楷体', 96)
start = pygame.font.SysFont('华文楷体', 39)
tips_game = pygame.font.SysFont('华文楷体', 14)
coins_look = pygame.font.SysFont('华文楷体', 28)
shop_1 = pygame.font.SysFont('华文楷体', 26)
upgrade = pygame.font.SysFont('华文楷体', 32)
exit_game = pygame.font.SysFont('华文楷体', 40)
a = pygame.font.SysFont('华文楷体', 20)
fps_00 = pygame.font.SysFont('华文楷体', 48)
e_00 = pygame.font.SysFont('华文楷体', 46)
select = pygame.font.SysFont('华文楷体', 125)
a_00 = pygame.font.SysFont('华文楷体', 52)
stop_tips_1 = pygame.font.SysFont('华文楷体', 38)
cheng_jiu_1a = pygame.font.SysFont('华文楷体', 24)
game_over = pygame.font.SysFont('华文楷体', 100)
game_over_1 = pygame.font.SysFont('华文楷体', 50)
score_look = pygame.font.SysFont('华文楷体', 42)
level_look_00 = pygame.font.SysFont('华文楷体', 150)
tips_game_over = pygame.font.SysFont('华文行楷', 150)


def quit_game():
    screen.fill(white)
    text = fps_00.render('ヾ•ω•`o拜拜！', True, (black))
    screen.blit(text, (260, 240))
    pygame.display.update()
    sleep(0.5)
    pygame.quit()
    save()
    quit()



def back():
    if wins == True:
        text = coins_look.render('《==返回', True, (green))
        screen.blit(text, (0, 0))
    elif game_overs == True:
        text = coins_look.render('《==返回', True, (red))
        screen.blit(text, (0, 0))
    else:
        text = coins_look.render('《==返回', True, (black))
        screen.blit(text, (0, 0))



def set_o():
    import save_1, save_2, save_3
    global player_speed_4, fps_1, fps, tips_1, tips, sound, sound_1, sound_2, sound_4, sound_5, coins, player_speed_3, hp_2, player_speed, hp, first_level_1, first_level_2, first_level_3, first_level_4, first_level_5, tong_guan_1, tong_guan_2, tong_guan_3, tong_guan_4, tong_guan_5, hp_3, e, starts, starts_open_1, starts_open_2, starts_open_3, starts_open_4, starts_open_5, die_number, cheng_jiu_cishu_1, cheng_jiu_cishu_2, cheng_jiu_cishu_3, cheng_jiu_cishu_4, cheng_jiu_cishu_5, cheng_jiu_cishu_6, cheng_jiu_cishu_7, cheng_jiu_cishu_8, cheng_jiu_cishu_9, cheng_jiu_cishu_10, cheng_jiu_cishu_11, cheng_jiu_cishu_12, cheng_jiu_cishu_13, open_level, level_ok_number, hui_fu_number, su_du_number, lower_number, coins_two_number, su_du_upgrade_number, hp_upgrade_number, upgrade_number, dao_ju_hp_level, dao_ju_su_du_level, dao_ju_lower_level, dao_ju_coins_two_level, save_name_true, save_name_true_2, default_save_name, donut_open
    while True:

        fps = fps_1
        tips = tips_1
        sound = sound_1
        sound_4 = sound_5
        clock.tick(12)

        dianji.set_volume(sound)
        win_sound.set_volume(sound)
        game_over_sound.set_volume(sound)
        pygame.mixer.music.set_volume(sound_4)

        if fps_1 > 96:
            fps_1 = 96

        elif fps_1 < 32:
            fps_1 = 32

        screen.fill(white)

        if tips == True:
            text = a.render('上下左右', True, (green))
            screen.blit(text, (18, 96))

            text = a.render('A', True, (green))
            screen.blit(text, (600, 96))

            text = a.render('D', True, (green))
            screen.blit(text, (52, 180))

            text = a.render('S', True, (green))
            screen.blit(text, (320, 180))

            text = a.render('V', True, (green))
            screen.blit(text, (140, 534))

            text = a.render('C', True, (green))
            screen.blit(text, (390, 534))

            text = a.render('U', True, (green))
            screen.blit(text, (640, 534))
            
            text = a.render('Q', True, (green))
            screen.blit(text, (52, 252))
            
            text = a.render('E', True, (green))
            screen.blit(text, (600, 252))

        text = fps_00.render(f'帧率：{fps_1}', True, (black))
        screen.blit(text, (12, 42))

        if tips_1 == True:
            tips_2 = '打开'

        elif tips_1 == False:
            tips_2 = '关闭'

        text = fps_00.render(f'提示：{tips_2}', True, (black))
        screen.blit(text, (270, 42))

        text = a.render('W', True, (green))
        screen.blit(text, (315, 96))

        if sound_1 < 0.25:
            sound_1 = 0

        elif sound_1 > 1.25:
            sound_1 = 0

        if sound == 0:
            sound_2 = '关闭'

        elif sound == 0.25:
            sound_2 = '很小'

        elif sound == 0.5:
            sound_2 = '小'

        elif sound == 0.75:
            sound_2 = '正常'

        elif sound == 1:
            sound_2 = '大'

        elif sound == 1.25:
            sound_2 = '很大'




        if sound_5 < 0.25:
            sound_5 = 0

        elif sound_5 > 1.25:
            sound_5 = 0

        if sound_4 == 0:
            sound_6 = '关闭'

        elif sound_4 == 0.25:
            sound_6 = '很小'

        elif sound_4 == 0.5:
            sound_6 = '小'

        elif sound_4 == 0.75:
            sound_6 = '正常'

        elif sound_4 == 1:
            sound_6 = '大'

        elif sound_4 == 1.25:
            sound_6 = '很大'


        text = fps_00.render(f'音效：{sound_2}', True, (black))
        screen.blit(text, (560, 42))

        text = fps_00.render(f'音乐：{sound_6}', True, (black))
        screen.blit(text, (12, 120))

        if save_name_true == True:
            save_name_true_2 = '打开'

        elif save_name_true == False:
            save_name_true_2 = '关闭'

        text = fps_00.render(f'显示存档名：{save_name_true_2}', True, (black))
        screen.blit(text, (270, 120))
        
        if default_save_name == 1:
            set_default_save_name = save_1.name
        elif default_save_name == 2:
            set_default_save_name = save_2.name
        elif default_save_name == 3:
            set_default_save_name = save_3.name
        
        text = fps_00.render(f'默认存档：{set_default_save_name}', True, (black))
        screen.blit(text, (12, 198))
        
        if donut_open == 1:
            donut_open_2 = '首次'
        elif donut_open == 2:
            donut_open_2 = '打开'
        elif donut_open == 3:
            donut_open_2 = '关闭'
        
        text = fps_00.render(f'旁白：{donut_open_2}', True, (black))
        screen.blit(text, (560, 198))

        text = fps_00.render('重置游戏', True, (black))
        screen.blit(text, (57, 480))

        text = fps_00.render('重置设置', True, (black))
        screen.blit(text, (307, 480))

        text = fps_00.render('切换存档', True, (black))
        screen.blit(text, (557, 480))

        back()

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_UP:
                    dianji.play()
                    fps_1 += 16

                elif event.key == K_LEFT or event.key == K_DOWN:
                    dianji.play()
                    fps_1 -= 16

                elif event.key == ord('w'):
                    dianji.play()
                    if tips_1 == True:
                        tips_1 = False

                    elif tips_1 == False:
                        tips_1 = True

                elif event.key == ord('a'):
                    dianji.play()
                    sound_1 += 0.25

                elif event.key == ord('d'):
                    dianji.play()
                    sound_5 += 0.25

                elif event.key == ord('s'):
                    dianji.play()
                    if save_name_true == True:
                        save_name_true = False

                    elif save_name_true == False:
                        save_name_true = True

                elif event.key == ord('r'):
                    dianji.play()
                    save()
                    home_page()

                elif event.key == ord('c'):
                    dianji.play()
                    fps_1 = 64
                    tips_1 = True
                    sound_1 = 0.75
                    sound_5 = 0.75
                    save_name_true = True
                    donut_open = 1
                    text = fps_00.render('重置完成！', True, (black))
                    screen.blit(text, (307, 280))

                    text = exit_game.render('=￣ω￣=', True, (black))
                    screen.blit(text, (327, 340))
                    pygame.display.update()
                    clock.tick(0.8)
                    save()

                elif event.key == ord('v'):
                    dianji.play()
                    save_restet()

                elif event.key == ord('u'):
                    dianji.play()
                    save()
                    user_select()
                    
                elif event.key == ord('q'):
                    dianji.play()
                    default_save_name += 1
                    if default_save_name > 3:
                        default_save_name = 1
                        
                elif event.key == ord('e'):
                    dianji.play()
                    donut_open += 1
                    if donut_open > 3:
                        donut_open = 1

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    home_page()

        pygame.display.update()



def save_restet():
    global sound_4, tips, hp, player_speed_4, fps_1, fps, tips_1, tips, sound, sound_1, sound_2, sound_4, sound_5, coins, player_speed_3, hp_2, player_speed, hp, first_level_1, first_level_2, first_level_3, first_level_4, first_level_5, tong_guan_1, tong_guan_2, tong_guan_3, tong_guan_4, tong_guan_5, hp_3, e, starts, starts_open_1, starts_open_2, starts_open_3, starts_open_4, starts_open_5, die_number, cheng_jiu_cishu_1, cheng_jiu_cishu_2, cheng_jiu_cishu_3, cheng_jiu_cishu_4, cheng_jiu_cishu_5, cheng_jiu_cishu_6, cheng_jiu_cishu_7, cheng_jiu_cishu_8, cheng_jiu_cishu_9, cheng_jiu_cishu_10, cheng_jiu_cishu_11, cheng_jiu_cishu_12, cheng_jiu_cishu_13, cheng_jiu_cishu_14, open_level, level_ok_number, hui_fu_number, su_du_number, lower_number, coins_two_number, su_du_upgrade_number, hp_upgrade_number, upgrade_number, dao_ju_hp_level, dao_ju_su_du_level, dao_ju_lower_level, dao_ju_coins_two_level, first_open_game, save_name_true, cheng_jiu_open, shop_open, upgrade_open, tong_ji_open, dui_huan_open, first_cheng_jiu_open, first_shop_open, first_upgrade_open, first_tong_ji_open, first_dui_huan_open, coins_dui_huan_1, coins_dui_huan_2, coins_dui_huan_3, coins_dui_huan_4, coins_dui_huan_5, coins_dui_huan_6, coins_dui_huan_7, coins_dui_huan_8, coins_dui_huan_9, coins_dui_huan_10, coins_dui_huan_11, default_save_name, donut_open, level_1_donut, level_2_donut, level_3_donut, level_4_donut, level_5_donut, first_enter_cheng_jiu, first_enter_shop, first_enter_upgrade, first_enter_tong_ji, first_enter_dui_huan
    while True:
        screen.fill(white)
        text = upgrade.render('确定要重置游戏吗？', True, (black))
        screen.blit(text, (270, 140))
        text = upgrade.render('这将无法恢复！', True, (black))
        screen.blit(text, (310, 180))
        text = upgrade.render('Yes                            No', True, (black))
        screen.blit(text, (250, 220))
        if tips == True:
            text = a.render('Y', True, (green))
            screen.blit(text, (260, 250))

            text = a.render('N', True, (green))
            screen.blit(text, (530, 250))
        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                set_o()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    set_o()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    set_o()

                elif event.key == ord('n'):
                    dianji.play()
                    save()
                    set_o()

                elif event.key == ord('y'):
                    dianji.play()
                    fps_1 = 64
                    tips_1 = True
                    tips = True
                    sound_1 = 0.75
                    sound_5 = 0.75
                    sound_4 = 0.75
                    coins = 0
                    player_speed_3 = False
                    hp_2 = False
                    player_speed = 3
                    hp_3 = 3
                    hp = 3
                    die_number = 0
                    e = 0
                    open_level = 0
                    level_ok_number = 0
                    first_open_game = False
                    save_name_true = True

                    cheng_jiu_open = False
                    shop_open = False
                    upgrade_open = False
                    tong_ji_open = False
                    dui_huan_open = False

                    first_cheng_jiu_open = False
                    first_shop_open = False
                    first_upgrade_open = False
                    first_tong_ji_open = False
                    first_dui_huan_open = False
                    
                    first_enter_cheng_jiu = False
                    first_enter_shop = False
                    first_enter_upgrade = False
                    first_enter_tong_ji = False
                    first_enter_dui_huan = False

                    dao_ju_hp_level = 1
                    dao_ju_su_du_level = 1
                    dao_ju_lower_level = 1
                    dao_ju_coins_two_level = 1

                    su_du_upgrade_number = 0
                    hp_upgrade_number = 0
                    upgrade_number = 0

                    hui_fu_number = 0
                    su_du_number = 0
                    lower_number = 0
                    coins_two_number = 0
                    player_speed_4 = 3

                    starts = 0
                    starts_open_1 = False
                    starts_open_2 = False
                    starts_open_3 = False
                    starts_open_4 = False
                    starts_open_5 = False

                    cheng_jiu_cishu_1 = False
                    cheng_jiu_cishu_2 = False
                    cheng_jiu_cishu_3 = False
                    cheng_jiu_cishu_4 = False
                    cheng_jiu_cishu_5 = False
                    cheng_jiu_cishu_6 = False
                    cheng_jiu_cishu_7 = False
                    cheng_jiu_cishu_8 = False
                    cheng_jiu_cishu_9 = False
                    cheng_jiu_cishu_10 = False
                    cheng_jiu_cishu_11 = False
                    cheng_jiu_cishu_12 = False
                    cheng_jiu_cishu_13 = False
                    cheng_jiu_cishu_14 = False

                    coins_dui_huan_1 = False
                    coins_dui_huan_2 = False
                    coins_dui_huan_3 = False
                    coins_dui_huan_4 = False
                    coins_dui_huan_5 = False
                    coins_dui_huan_6 = False
                    coins_dui_huan_7 = False
                    coins_dui_huan_8 = False
                    coins_dui_huan_9 = False
                    coins_dui_huan_10 = False
                    coins_dui_huan_11 = False

                    first_level_1 = False
                    first_level_2 = False
                    first_level_3 = False
                    first_level_4 = False
                    first_level_5 = False

                    tong_guan_1 = False
                    tong_guan_2 = False
                    tong_guan_3 = False
                    tong_guan_4 = False
                    tong_guan_5 = False
                    
                    default_save_name = 1
                    
                    donut_open = 1
                    level_1_donut = False
                    level_2_donut = False
                    level_3_donut = False
                    level_4_donut = False
                    level_5_donut = False
                    
                    save()
                    text = fps_00.render('重置完成！', True, (black))
                    screen.blit(text, (300, 280))

                    text = exit_game.render('=￣ω￣=', True, (black))
                    screen.blit(text, (310, 340))
                    pygame.display.update()
                    sleep(1)
                    save()
                    set_o()

        pygame.display.update()



def user_select():
    global user, user_2, user_3, user_save, tips, sound, sound_4, open_user
    import save_1, save_2, save_3
    while True:
        tips = tips_1
        sound = sound_1
        sound_4 = sound_5

        dianji.set_volume(sound)
        win_sound.set_volume(sound)
        game_over_sound.set_volume(sound)
        pygame.mixer.music.set_volume(sound_4)

        clock.tick(5)
        screen.fill(white)
        back()

        if len(save_1.name) >= 5:
            text = upgrade.render(f'{save_1.name}', True, (black))
            screen.blit(text, (340, 25))

        else:
            text = upgrade.render(f'{save_1.name}', True, (black))
            screen.blit(text, (360, 25))

        text = shop_1.render('累计通关：', True, (black))
        screen.blit(text, (15, 75))

        text = shop_1.render(f'{save_1.level_ok_number}关', True, (black))
        screen.blit(text, (20, 100))

        text = shop_1.render('完美通关：', True, (black))
        screen.blit(text, (215, 75))

        text = shop_1.render(f'{save_1.starts}关', True, (black))
        screen.blit(text, (220, 100))

        text = shop_1.render('累积金币：', True, (black))
        screen.blit(text, (415, 75))

        text = shop_1.render(f'{save_1.coins}枚', True, (black))
        screen.blit(text, (420, 100))

        text = shop_1.render('消费金币：', True, (black))
        screen.blit(text, (615, 75))

        text = shop_1.render(f'{save_1.e}枚', True, (black))
        screen.blit(text, (620, 100))

        text = shop_1.render('更名存档', True, (black))
        screen.blit(text, (30, 145))

        text = shop_1.render('进入存档', True, (black))
        screen.blit(text, (650, 145))



        if len(save_1.name) >= 5:
            text = upgrade.render(f'{save_2.name}', True, (black))
            screen.blit(text, (340, 205))

        else:
            text = upgrade.render(f'{save_2.name}', True, (black))
            screen.blit(text, (360, 205))

        text = shop_1.render('累计通关：', True, (black))
        screen.blit(text, (15, 255))

        text = shop_1.render(f'{save_2.level_ok_number}关', True, (black))
        screen.blit(text, (20, 280))

        text = shop_1.render('完美通关：', True, (black))
        screen.blit(text, (215, 255))

        text = shop_1.render(f'{save_2.starts}关', True, (black))
        screen.blit(text, (220, 280))

        text = shop_1.render('累积金币：', True, (black))
        screen.blit(text, (415, 255))

        text = shop_1.render(f'{save_2.coins}枚', True, (black))
        screen.blit(text, (420, 280))

        text = shop_1.render('消费金币：', True, (black))
        screen.blit(text, (615, 255))

        text = shop_1.render(f'{save_2.e}枚', True, (black))
        screen.blit(text, (620, 280))

        text = shop_1.render('更名存档', True, (black))
        screen.blit(text, (30, 325))

        text = shop_1.render('进入存档', True, (black))
        screen.blit(text, (650, 325))




        if len(save_1.name) >= 5:
            text = upgrade.render(f'{save_3.name}', True, (black))
            screen.blit(text, (340, 385))

        else:
            text = upgrade.render(f'{save_3.name}', True, (black))
            screen.blit(text, (360, 385))

        text = shop_1.render(f'累计通关：', True, (black))
        screen.blit(text, (15, 435))

        text = shop_1.render(f'{save_3.level_ok_number}关', True, (black))
        screen.blit(text, (20, 460))

        text = shop_1.render('完美通关：', True, (black))
        screen.blit(text, (215, 435))

        text = shop_1.render(f'{save_3.starts}关', True, (black))
        screen.blit(text, (220, 460))

        text = shop_1.render('累积金币：', True, (black))
        screen.blit(text, (415, 435))

        text = shop_1.render(f'{save_2.coins}枚', True, (black))
        screen.blit(text, (420, 460))

        text = shop_1.render('消费金币：', True, (black))
        screen.blit(text, (615, 435))

        text = shop_1.render(f'{save_3.e}枚', True, (black))
        screen.blit(text, (620, 460))

        text = shop_1.render('更名存档', True, (black))
        screen.blit(text, (30, 505))

        text = shop_1.render('进入存档', True, (black))
        screen.blit(text, (650, 505))

        if tips == True:
            text = shop_1.render('q', True, (black))
            screen.blit(text, (75, 175))

            text = shop_1.render('a', True, (black))
            screen.blit(text, (695, 175))



            text = shop_1.render('w', True, (black))
            screen.blit(text, (75, 355))

            text = shop_1.render('s', True, (black))
            screen.blit(text, (695, 355))



            text = shop_1.render('e', True, (black))
            screen.blit(text, (75, 535))

            text = shop_1.render('d', True, (black))
            screen.blit(text, (695, 535))

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    set_o()

                elif event.key == ord('q'):
                    dianji.play()
                    user_save = 1
                    user = True
                    user_2 = False
                    user_3 = False
                    user_pan_duan()
                    geng_ming_save()

                elif event.key == ord('w'):
                    dianji.play()
                    user_save = 2
                    user_2 = True
                    user = False
                    user_3 = False
                    user_pan_duan()
                    geng_ming_save()

                elif event.key == ord('e'):
                    dianji.play()
                    user_save = 3
                    user_3 = True
                    user = False
                    user_2 = False
                    user_pan_duan()
                    geng_ming_save()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    set_o()

                elif event.key == ord('a'):
                    dianji.play()
                    user = True
                    user_2 = False
                    user_3 = False
                    user_pan_duan()
                    save()

                elif event.key == ord('s'):
                    dianji.play()
                    user_2 = True
                    user = False
                    user_3 = False
                    user_pan_duan()
                    save()

                elif event.key == ord('d'):
                    dianji.play()
                    user_3 = True
                    user = False
                    user_2 = False
                    user_pan_duan()
                    save()

        pygame.display.update()



def geng_ming_save():
    global name
    screen.fill(white)
    text = upgrade.render('请在控制台操作', True, (black))
    screen.blit(text, (280, 240))
    pygame.display.update()
    n = input('''
请输入要改成的名字（最多五个字符）：''')
    if len(n) > 5:
        print('更改后的存档名最多只能有5个字符！')
        geng_ming_save()
    while True:
        screen.fill(white)
        clock.tick(3)
        back()

        text = upgrade.render(f'确定要改成：【{n}】吗？', True, (black))
        screen.blit(text, (270, 240))

        text = upgrade.render('按S确定', True, (black))
        screen.blit(text, (270, 320))

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    user_true()
                    user_select()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    user_true()
                    user_select()

                elif event.key == ord('s'):
                    dianji.play()
                    n = str(n)
                    name = n
                    save()
                    user_true()
                    print('''
重启游戏后存档名生效！''')
                    user_select()

        pygame.display.update()



def user_true():
    global user, user_2, user_3
    if user_save == 1:
        user = True
        user_2 = False
        user_3 = False

    elif user_save == 2:
        user_2 = True
        user = False
        user_3 = False

    elif user_save == 3:
        user_3 = True
        user = False
        user_2 = False



def tong_ji_1():
    global first_enter_tong_ji, tong_ji_donut
    if donut_open == 1 or donut_open == 2:
        if first_enter_tong_ji == False:
            tong_ji_donut = True
            first_enter_tong_ji = True
            donut.block_open_donut()            # 显示第一次进入统计界面时的旁白
    cheng_jiu_pan_duan()
    while True:
        screen.fill(white)
        clock.tick(3)
        back()

        text = e_00.render(f'进入关卡：{open_level}次', True, (black))
        text_1 = e_00.render(f'死亡次数：{die_number}次', True, (black))
        text_2 = e_00.render(f'累计通关：{level_ok_number}关', True, (black))
        text_3 = e_00.render(f'完美通关：{starts}关', True, (black))
        text_4 = e_00.render(f'累积金币：{coins + e}枚', True, (black))
        text_5 = e_00.render(f'消费金币：{e}枚', True, (black))
        text_6 = e_00.render(f'获得成就：{cheng_jiu_1_coins}个', True, (black))

        screen.blit(text, (240, 0))
        screen.blit(text_1, (240, 82))
        screen.blit(text_2, (240, 164))
        screen.blit(text_3, (240, 246))
        screen.blit(text_4, (240, 328))
        screen.blit(text_5, (240, 410))
        screen.blit(text_6, (240, 492))

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    home_page()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    home_page()

        pygame.display.update()



def upgrade_player():
    global hp, player_speed, player_speed_3, hp_2, hp_3, hp_upgrade_coins, speed_upgrade_coins, player_speed_2, coins, e, player_speed_4, upgrade_number, su_du_upgrade_number, hp_upgrade_number, ticks, first_enter_upgrade, upgrade_donut
    if donut_open == 1 or donut_open == 2:
        if first_enter_upgrade == False:
            upgrade_donut = True
            first_enter_upgrade = True
            donut.block_open_donut()            # 显示第一次进入兑换界面时的旁白
    while True:
        ticks += 1
        cheng_jiu_0()

        hp = hp_3
        player_speed = player_speed_4

        clock.tick(5)
        screen.fill(white)
        if ticks % 12 < 6:
            screen.blit(player_img_3, (50, 50))
        else:
            screen.blit(player_img_4, (50, 50))
        back()

        if hp == 3:
            hp_upgrade_coins = 125
            save()

        elif hp == 4:
            hp_upgrade_coins = 245
            save()

        elif hp == 5:
            hp_upgrade_coins = 365
            save()

        elif hp == 6:
            hp_upgrade_coins = 485
            save()

        elif hp == 7:
            hp_upgrade_coins = '∞'
            hp = 7
            hp_2 = True
            save()

        elif hp > 7:
            hp = 7



        if player_speed == 3:
            player_speed_2 = '很慢'
            speed_upgrade_coins = 60
            save()

        elif player_speed == 3.5:
            player_speed_2 = '慢'
            speed_upgrade_coins = 125
            save()

        elif player_speed == 4:
            player_speed_2 = '正常'
            speed_upgrade_coins = 190
            save()

        elif player_speed == 4.5:
            player_speed_2 = '快'
            speed_upgrade_coins = 250
            save()

        elif player_speed == 5:
            player_speed_2 = '很快'
            speed_upgrade_coins = 305
            save()

        elif player_speed == 5.5:
            player_speed_2 = '超快'
            speed_upgrade_coins = 370
            save()

        elif player_speed == 6:
            player_speed_2 = '极限'
            speed_upgrade_coins = '∞'
            player_speed = 6
            player_speed_3 = True
            save()

        elif player_speed > 6:
            player_speed = 6

        text = upgrade.render(f'速度：{player_speed_2}      升级（{speed_upgrade_coins}金币）', True, (black))
        screen.blit(text, (300, 50))

        text = upgrade.render(f'血量：{hp}            升级（{hp_upgrade_coins}金币）', True, (black))
        screen.blit(text, (300, 150))

        text = coins_look.render(f'道具升级==》', True, (black))
        screen.blit(text, (630, 0))

        if tips == True:
            text = shop_1.render('1', True, (black))
            screen.blit(text, (460, 20))

            text = shop_1.render('2', True, (black))
            screen.blit(text, (460, 120))

            text = shop_1.render('D', True, (black))
            screen.blit(text, (670 ,25))

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    home_page()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    home_page()

                elif event.key == K_1:
                    dianji.play()
                    if player_speed_3 == True:
                        man()
                        continue
                    elif coins < speed_upgrade_coins:
                        no_coins()

                    dianji.play()
                    coins -= speed_upgrade_coins
                    e += speed_upgrade_coins
                    player_speed_4 += 0.5
                    upgrade_number += 1
                    su_du_upgrade_number += 1

                elif event.key == K_2:
                    dianji.play()
                    if hp_2 == True:
                        man()
                        continue
                    if coins < hp_upgrade_coins:
                        no_coins()

                    dianji.play()
                    coins -= hp_upgrade_coins
                    e += hp_upgrade_coins
                    hp_3 += 1
                    upgrade_number += 1
                    hp_upgrade_number += 1

                elif event.key == ord('d') or event.key == K_LEFT:
                    dianji.play()
                    upgrade_dao_ju()

        pygame.display.update()



def upgrade_dao_ju():
    global dao_ju_hp_upgrade_coins, dao_ju_su_du_upgrade_coins, dao_ju_lower_upgrade_coins, dao_ju_hp_level, dao_ju_su_du_level, dao_ju_lower_level
    dao_ju_hp_upgrade_coins = 120
    dao_ju_su_du_upgrade_coins = 120
    dao_ju_lower_upgrade_coins = 240
    while True:
        upgrade_dao_ju_pan_duan()

        clock.tick(10)
        screen.fill(white)
        screen.blit(hui_fu_2_img, (25, 50))
        screen.blit(su_du_2_img, (25, 182))
        screen.blit(lower_2_img, (25, 314))
        back()

        text = upgrade.render(f'生命增加', True, (black))
        screen.blit(text, (152, 50))

        text = upgrade.render(f'速度提升', True, (black))
        screen.blit(text, (152, 182))

        text = upgrade.render(f'敌人速度减少', True, (black))
        screen.blit(text, (152, 314))

        text = cheng_jiu_1a.render(f'                 升级（{dao_ju_hp_upgrade_coins}金币）', True, (black))
        screen.blit(text, (252, 60))

        text = cheng_jiu_1a.render(f'                 升级（{dao_ju_su_du_upgrade_coins}金币）', True, (black))
        screen.blit(text, (252, 192))

        text = cheng_jiu_1a.render(f'         升级（{dao_ju_lower_upgrade_coins}金币）', True, (black))
        screen.blit(text, (302, 324))

        text = cheng_jiu_1a.render(f'一关中使用后生命增加{hp_zeng_jia}点', True, (black))
        screen.blit(text, (152, 80))

        text = cheng_jiu_1a.render(f'一关中使用后速度提升{su_du_zeng_jia}点', True, (black))
        screen.blit(text, (152, 212))

        text = cheng_jiu_1a.render(f'一关中使用后敌人速度减少{lower_jian_shao}点', True, (black))
        screen.blit(text, (152, 344))

        text = cheng_jiu_1a.render(f'{d_2}', True, (black))
        screen.blit(text, (152, 100))

        text = cheng_jiu_1a.render(f'{d_2}', True, (black))
        screen.blit(text, (152, 232))

        text = cheng_jiu_1a.render(f'{d_2}', True, (black))
        screen.blit(text, (152, 364))


        if tips == True:
            text = shop_1.render('1', True, (black))
            screen.blit(text, (600, 80))

            text = shop_1.render('2', True, (black))
            screen.blit(text, (600, 212))

            text = shop_1.render('3', True, (black))
            screen.blit(text, (600, 344))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    upgrade_player()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    upgrade_player()

                elif event.key == K_1:
                    dianji.play()
                    if dao_ju_hp_level == 4:
                        man_2()
                    elif coins < dao_ju_hp_upgrade_coins:
                        no_coins_3()

                    else:
                        dao_ju_hp_level += 1

                elif event.key == K_2:
                    dianji.play()
                    if dao_ju_su_du_level == 4:
                        man_2()
                    elif coins < dao_ju_su_du_upgrade_coins:
                        no_coins_3()

                    else:
                        dao_ju_su_du_level += 1

                elif event.key == K_3:
                    dianji.play()
                    if dao_ju_lower_level == 4:
                        man_2()
                    elif coins < dao_ju_lower_upgrade_coins:
                        no_coins_3()

                    else:
                        dao_ju_lower_level += 1



def man_2():
    while True:
        text = fps_00.render('已经满级了！', True, (black))
        screen.blit(text, (420, 400))

        text = exit_game.render('q≧▽≦q', True, (black))
        screen.blit(text, (460, 450))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    upgrade_dao_ju()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    upgrade_dao_ju()

        clock.tick(0.8)
        upgrade_dao_ju()



def upgrade_dao_ju_pan_duan():
    global dao_ju_hp_upgrade_coins, dao_ju_su_du_upgrade_coins, dao_ju_lower_upgrade_coins, dao_ju_hp_level, dao_ju_su_du_level, dao_ju_lower_level, d_2, d_1
    if dao_ju_hp_level == 1:
        dao_ju_hp_upgrade_coins = 240
        pygame.display.update()

    elif dao_ju_hp_level == 2:
        dao_ju_hp_upgrade_coins = 336
        pygame.display.update()

    elif dao_ju_hp_level == 3:
        dao_ju_hp_upgrade_coins = 432
        d_2 = e_2
        pygame.display.update()

    elif dao_ju_hp_level > 3:
        dao_ju_hp_upgrade_coins = '∞'
        dao_ju_hp_level = 4
        d_2 = e_2
        pygame.display.update()


    if dao_ju_su_du_level == 1:
        dao_ju_su_du_upgrade_coins = 240
        pygame.display.update()

    elif dao_ju_su_du_level == 2:
        dao_ju_su_du_upgrade_coins = 336
        pygame.display.update()

    elif dao_ju_su_du_level == 3:
        dao_ju_su_du_upgrade_coins = 432
        d_2 = e_2
        pygame.display.update()

    elif dao_ju_su_du_level > 3:
        dao_ju_su_du_upgrade_coins = '∞'
        dao_ju_su_du_level = 4
        d_2 = e_2
        pygame.display.update()



    if dao_ju_lower_level == 1:
        dao_ju_lower_upgrade_coins = 240
        pygame.display.update()

    elif dao_ju_lower_level == 2:
        dao_ju_lower_upgrade_coins = 336
        pygame.display.update()

    elif dao_ju_lower_level == 3:
        dao_ju_lower_upgrade_coins = 432
        d_2 = e_2
        pygame.display.update()

    elif dao_ju_lower_level > 3:
        dao_ju_lower_upgrade_coins = '∞'
        dao_ju_lower_level = 4
        d_2 = e_2
        pygame.display.update()



def no_coins_3():
    while True:
        upgrade_dao_ju_pan_duan()
        text = fps_00.render('没金币了呢！', True, (black))
        screen.blit(text, (270, 400))

        text = fps_00.render('╯︿╰', True, (black))
        screen.blit(text, (329, 450))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    upgrade_dao_ju()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    upgrade_dao_ju()

        clock.tick(0.8)
        upgrade_dao_ju()



def cheng_jiu():
    global first_enter_cheng_jiu, cheng_jiu_donut
    if donut_open == 1 or donut_open == 2:
        if first_enter_cheng_jiu == False:
            cheng_jiu_donut = True
            first_enter_cheng_jiu = True
            donut.block_open_donut()            # 显示第一次进入成就界面时的旁白
    cheng_jiu_pan_duan()
    while True:
        clock.tick(5)
        screen.fill(white)
        if tong_guan_1 == True:
            text = cheng_jiu_1a.render('★', True, (yellow))
            screen.blit(text, (240, 60))

        elif tong_guan_1 == False:
            text = cheng_jiu_1a.render('☆', True, (yellow))
            screen.blit(text, (240, 60))



        if tong_guan_1 == True and first_level_1 == True and starts_open_1 == True:
            text = cheng_jiu_1a.render('★', True, (yellow))
            screen.blit(text, (640, 60))

        elif (tong_guan_1 == False and first_level_1 == False and starts_open_1 == False) or (tong_guan_1 == True and first_level_1 == False and starts_open_1 == False) or (tong_guan_1 == True and first_level_1 == True and starts_open_1 == False) or (tong_guan_1 == True and first_level_1 == False and starts_open_1 == True):
            text = cheng_jiu_1a.render('☆', True, (yellow))
            screen.blit(text, (640, 60))



        if e >= 160:
            text = cheng_jiu_1a.render('★', True, (yellow))
            screen.blit(text, (240, 130))

        elif e < 160:
            text = cheng_jiu_1a.render('☆', True, (yellow))
            screen.blit(text, (240, 130))



        if e >= 280:
            text = cheng_jiu_1a.render('★', True, (yellow))
            screen.blit(text, (640, 130))

        elif e < 280:
            text = cheng_jiu_1a.render('☆', True, (yellow))
            screen.blit(text, (640, 130))



        if e >= 400:
            text = cheng_jiu_1a.render('★', True, (yellow))
            screen.blit(text, (240, 210))

        elif e < 400:
            text = cheng_jiu_1a.render('☆', True, (yellow))
            screen.blit(text, (240, 210))



        if upgrade_number >= 2:
            text = cheng_jiu_1a.render('★', True, (yellow))
            screen.blit(text, (640, 210))

        elif upgrade_number < 2:
            text = cheng_jiu_1a.render('☆', True, (yellow))
            screen.blit(text, (640, 210))



        if upgrade_number >= 4:
            text = cheng_jiu_1a.render('★', True, (yellow))
            screen.blit(text, (240, 290))

        elif upgrade_number < 4:
            text = cheng_jiu_1a.render('☆', True, (yellow))
            screen.blit(text, (240, 290))



        if upgrade_number >= 6:
            text = cheng_jiu_1a.render('★', True, (yellow))
            screen.blit(text, (640, 290))

        elif upgrade_number < 6:
            text = cheng_jiu_1a.render('☆', True, (yellow))
            screen.blit(text, (640, 290))



        if hp_upgrade_number == 4:
            text = cheng_jiu_1a.render('★', True, (yellow))
            screen.blit(text, (240, 370))

        elif hp_upgrade_number != 4:
            text = cheng_jiu_1a.render('☆', True, (yellow))
            screen.blit(text, (240, 370))



        if su_du_upgrade_number == 6:
            text = cheng_jiu_1a.render('★', True, (yellow))
            screen.blit(text, (640, 370))

        elif su_du_upgrade_number != 6:
            text = cheng_jiu_1a.render('☆', True, (yellow))
            screen.blit(text, (640, 370))



        if coins >= 500:
            text = cheng_jiu_1a.render('★', True, (yellow))
            screen.blit(text, (240, 450))

        elif coins < 500:
            text = cheng_jiu_1a.render('☆', True, (yellow))
            screen.blit(text, (240, 450))



        if coins >= 1500:
            text = cheng_jiu_1a.render('★', True, (yellow))
            screen.blit(text, (640, 450))

        elif coins < 1500:
            text = cheng_jiu_1a.render('☆', True, (yellow))
            screen.blit(text, (640, 450))



        if coins >= 4500:
            text = cheng_jiu_1a.render('★', True, (yellow))
            screen.blit(text, (240, 530))

        elif coins < 4500:
            text = cheng_jiu_1a.render('☆', True, (yellow))
            screen.blit(text, (240, 530))



        if cheng_jiu_1_coins == 13:
            text = cheng_jiu_1a.render('★', True, (yellow))
            screen.blit(text, (640, 530))

        elif cheng_jiu_1_coins < 13:
            text = cheng_jiu_1a.render('☆', True, (yellow))
            screen.blit(text, (640, 530))


        back()
        if dui_huan_open == True:
            text = coins_look.render('兑换↑', True, (black))
            screen.blit(text, (180, 0))

        if tips == True:
            if dui_huan_open == True:
                text = coins_look.render('H', True, (green))
                screen.blit(text ,(260, 0))

        clock.tick(fps)
        text = upgrade.render('开启征途', True, (black))
        screen.blit(text, (25, 50))
        text = upgrade.render('完美启程', True, (black))
        screen.blit(text, (425, 50))
        text = upgrade.render('日常消费', True, (black))
        screen.blit(text, (25, 130))
        text = upgrade.render('热爱消费', True, (black))
        screen.blit(text, (425, 130))
        text = upgrade.render('冲动消费', True, (black))
        screen.blit(text, (25, 210))
        text = upgrade.render('增强自己', True, (black))
        screen.blit(text, (425, 210))
        text = upgrade.render('突破自己', True, (black))
        screen.blit(text, (25, 290))
        text = upgrade.render('超越自己', True, (black))
        screen.blit(text, (425, 290))
        text = upgrade.render('血量专精', True, (black))
        screen.blit(text, (25, 370))
        text = upgrade.render('速度专精', True, (black))
        screen.blit(text, (425, 370))
        text = upgrade.render('富家子弟', True, (black))
        screen.blit(text, (25, 450))
        text = upgrade.render('钱财满贯', True, (black))
        screen.blit(text, (425, 450))
        text = upgrade.render('超级土豪', True, (black))
        screen.blit(text, (25, 530))
        text = upgrade.render('13颗星', True, (black))
        screen.blit(text, (425, 530))

        text = cheng_jiu_1a.render('通关第一关', True, (black))
        screen.blit(text, (25, 90))
        text = cheng_jiu_1a.render('第一次满血通关第一关', True, (black))
        screen.blit(text, (425, 90))
        text = cheng_jiu_1a.render('使用160枚金币', True, (black))
        screen.blit(text,(25, 170))
        text = cheng_jiu_1a.render('使用280枚金币', True, (black))
        screen.blit(text,(425, 170))
        text = cheng_jiu_1a.render('使用400枚金币', True, (black))
        screen.blit(text,(25, 250))
        text = cheng_jiu_1a.render('进行升级2次', True, (black))
        screen.blit(text, (425, 250))
        text = cheng_jiu_1a.render('进行升级4次', True, (black))
        screen.blit(text, (25, 330))
        text = cheng_jiu_1a.render('进行升级6次', True, (black))
        screen.blit(text, (425, 330))
        text = cheng_jiu_1a.render('将血量升至满级', True, (black))
        screen.blit(text, (25, 410))
        text = cheng_jiu_1a.render('将速度升至满级', True, (black))
        screen.blit(text, (425, 410))
        text = cheng_jiu_1a.render('拥有500枚金币', True, (black))
        screen.blit(text, (25, 490))
        text = cheng_jiu_1a.render('拥有1500枚金币', True, (black))
        screen.blit(text, (425, 490))
        text = cheng_jiu_1a.render('拥有4500枚金币', True, (black))
        screen.blit(text, (25, 570))
        text = cheng_jiu_1a.render('完成13个成就', True, (black))
        screen.blit(text, (425, 570))

        text = upgrade.render(f'★ x {cheng_jiu_1_coins}', True, (yellow))
        screen.blit(text, (320, 0))

        text = upgrade.render(f'☆ x {cheng_jiu_1a_coins}', True, (yellow))
        screen.blit(text, (480, 0))

        text = upgrade.render(f'☆★ x {cheng_jiu_1_coins + cheng_jiu_1a_coins}', True, (yellow))
        screen.blit(text, (640, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    home_page()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    home_page()

                if cheng_jiu_1_coins >= 7 or starts >= 7:
                    if event.key == ord('h'):
                        dianji.play()
                        save()
                        coins_dui_huan()

        pygame.display.update()



def coins_dui_huan():
    global coins, home, coins_dui_huan_1, coins_dui_huan_2, coins_dui_huan_3, coins_dui_huan_4, coins_dui_huan_5, coins_dui_huan_6, coins_dui_huan_7, coins_dui_huan_8, coins_dui_huan_9, coins_dui_huan_10, coins_dui_huan_11, first_enter_dui_huan, dui_huan_donut
    if donut_open == 1 or donut_open == 2:
        if first_enter_dui_huan == False:
            dui_huan_donut = True
            first_enter_dui_huan = True
            donut.block_open_donut()            # 显示第一次进入兑换界面时的旁白
    while True:
        clock.tick(5)
        screen.fill(white)
        back()
        screen.blit(coins_img, (338, 0))
        text = a.render(f'{coins}', True, (black))
        screen.blit(text, (370, 0))
        if tips == True:
            text = shop_1.render('使用数字键选择来兑换金币（最左为1，以此类推……）', True, (black))
            screen.blit(text, (80, 560))

            text = shop_1.render('Q.', True, (green))
            screen.blit(text, (120, 345))

            text = shop_1.render('W.', True, (green))
            screen.blit(text, (420, 345))

        screen.blit(coins_img, (200, 60))
        screen.blit(coins_img, (470, 60))
        screen.blit(coins_img, (725, 60))
        screen.blit(coins_img, (215, 130))
        screen.blit(coins_img, (470, 130))
        screen.blit(coins_img, (725, 130))

        screen.blit(coins_img, (200, 250))
        screen.blit(coins_img, (470, 250))
        screen.blit(coins_img, (725, 250))
        screen.blit(coins_img, (290, 320))
        screen.blit(coins_img, (595, 320))

        text = upgrade.render('★ x 7  = 125', True, (yellow))
        screen.blit(text, (25, 50))
        text = upgrade.render('★ x 14  = 180', True, (yellow))
        screen.blit(text, (280, 50))
        text = upgrade.render('★ x 21  = 235', True, (yellow))
        screen.blit(text, (535, 50))
        text = upgrade.render('★ x 28  = 290', True, (yellow))
        screen.blit(text, (25, 120))
        text = upgrade.render('★ x 35  = 345', True, (yellow))
        screen.blit(text, (280, 120))
        text = upgrade.render('★ x 42  = 400', True, (yellow))
        screen.blit(text, (535, 120))

        text = upgrade.render('★ x 7  = 125', True, (blue))
        screen.blit(text, (25, 240))
        text = upgrade.render('★ x 14  = 180', True, (blue))
        screen.blit(text, (280, 240))
        text = upgrade.render('★ x 21  = 235', True, (blue))
        screen.blit(text, (535, 240))
        text = upgrade.render('★ x 28  = 290', True, (blue))
        screen.blit(text, (100, 310))
        text = upgrade.render('★ x 35  = 345', True, (blue))
        screen.blit(text, (405, 310))

        coins_dui_huan_name()

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    if home == True:
                        home = False
                        home_page()
                    else:
                        cheng_jiu()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    if home == True:
                        home = False
                        home_page()
                    else:
                        cheng_jiu()

                elif event.key == K_1:
                    if cheng_jiu_1_coins >= 7 and coins_dui_huan_1 == False:
                        dianji.play()
                        coins += 125
                        coins_dui_huan_1 = True
                        save()

                elif event.key == K_2:
                    if cheng_jiu_1_coins >= 14 and coins_dui_huan_2 == False:
                        dianji.play()
                        coins += 180
                        coins_dui_huan_2 = True
                        save()

                elif event.key == K_3:
                    if cheng_jiu_1_coins >= 21 and coins_dui_huan_3 == False:
                        dianji.play()
                        coins += 235
                        coins_dui_huan_3 = True
                        save()

                elif event.key == K_4:
                    if cheng_jiu_1_coins >= 28 and coins_dui_huan_4 == False:
                        dianji.play()
                        coins += 290
                        coins_dui_huan_4 = True
                        save()

                elif event.key == K_5:
                    if cheng_jiu_1_coins >= 35 and coins_dui_huan_5 == False:
                        dianji.play()
                        coins += 345
                        coins_dui_huan_5 = True
                        save()

                elif event.key == K_6:
                    if cheng_jiu_1_coins >= 42 and coins_dui_huan_6 == False:
                        dianji.play()
                        coins += 400
                        coins_dui_huan_6 = True
                        save()

                elif event.key == K_7:
                    if starts >= 7 and coins_dui_huan_7 == False:
                        dianji.play()
                        coins += 125
                        coins_dui_huan_7 = True
                        save()

                elif event.key == K_8:
                    if starts >= 14 and coins_dui_huan_8 == False:
                        dianji.play()
                        coins += 180
                        coins_dui_huan_8 = True
                        save()

                elif event.key == K_9:
                    if starts >= 21 and coins_dui_huan_9 == False:
                        dianji.play()
                        coins += 235
                        coins_dui_huan_9 = True
                        save()

                elif event.key == ord('q'):
                    if starts >= 28 and coins_dui_huan_10 == False:
                        dianji.play()
                        coins += 290
                        coins_dui_huan_10 = True
                        save()

                elif event.key == ord('w'):
                    if starts >= 35 and coins_dui_huan_11 == False:
                        dianji.play()
                        coins += 345
                        coins_dui_huan_11 = True
                        save()

        pygame.display.update()



def coins_dui_huan_name():
    if coins_dui_huan_1 == True:
        text = shop_1.render('已兑换', True, (black))
        screen.blit(text, (50, 85))
    else:
        if cheng_jiu_1_coins >= 7:
            text = shop_1.render('兑换', True, (green))
            screen.blit(text, (50, 85))
        else:
            text = shop_1.render('兑换', True, (black))
            screen.blit(text, (50, 85))



    if coins_dui_huan_2 == True:
        text = shop_1.render('已兑换', True, (black))
        screen.blit(text, (325, 85))
    else:
        if cheng_jiu_1_coins >= 14:
            text = shop_1.render('兑换', True, (green))
            screen.blit(text, (325, 85))
        else:
            text = shop_1.render('兑换', True, (black))
            screen.blit(text, (325, 85))



    if coins_dui_huan_3 == True:
        text = shop_1.render('已兑换', True, (black))
        screen.blit(text, (580, 85))
    else:
        if cheng_jiu_1_coins >= 21:
            text = shop_1.render('兑换', True, (green))
            screen.blit(text, (580, 85))
        else:
            text = shop_1.render('兑换', True, (black))
            screen.blit(text, (580, 85))



    if coins_dui_huan_4 == True:
        text = shop_1.render('已兑换', True, (black))
        screen.blit(text, (70, 155))
    else:
        if cheng_jiu_1_coins >= 28:
            text = shop_1.render('兑换', True, (green))
            screen.blit(text, (70, 155))
        else:
            text = shop_1.render('兑换', True, (black))
            screen.blit(text, (70, 155))



    if coins_dui_huan_5 == True:
        text = shop_1.render('已兑换', True, (black))
        screen.blit(text, (325, 155))
    else:
        if cheng_jiu_1_coins >= 35:
            text = shop_1.render('兑换', True, (green))
            screen.blit(text, (325, 155))
        else:
            text = shop_1.render('兑换', True, (black))
            screen.blit(text, (325, 155))



    if coins_dui_huan_6 == True:
        text = shop_1.render('已兑换', True, (black))
        screen.blit(text, (580, 155))
    else:
        if cheng_jiu_1_coins >= 42:
            text = shop_1.render('兑换', True, (green))
            screen.blit(text, (580, 155))
        else:
            text = shop_1.render('兑换', True, (black))
            screen.blit(text, (580, 155))





    if coins_dui_huan_7 == True:
        text = shop_1.render('已兑换', True, (black))
        screen.blit(text, (70, 275))
    else:
        if starts >= 7:
            text = shop_1.render('兑换', True, (green))
            screen.blit(text, (70, 275))

        else:
            text = shop_1.render('兑换', True, (black))
            screen.blit(text, (70, 275))



    if coins_dui_huan_8 == True:
        text = shop_1.render('已兑换', True, (black))
        screen.blit(text, (325, 275))
    else:
        if starts >= 14:
            text = shop_1.render('兑换', True, (green))
            screen.blit(text, (325, 275))

        else:
            text = shop_1.render('兑换', True, (black))
            screen.blit(text, (325, 275))



    if coins_dui_huan_9 == True:
        text = shop_1.render('已兑换', True, (black))
        screen.blit(text, (580, 275))
    else:
        if starts >= 21:
            text = shop_1.render('兑换', True, (green))
            screen.blit(text, (580, 275))

        else:
            text = shop_1.render('兑换', True, (black))
            screen.blit(text, (580, 275))



    if coins_dui_huan_10 == True:
        text = shop_1.render('已兑换', True, (black))
        screen.blit(text, (145, 345))
    else:
        if starts >= 28:
            text = shop_1.render('兑换', True, (green))
            screen.blit(text, (145, 345))

        else:
            text = shop_1.render('兑换', True, (black))
            screen.blit(text, (145, 345))



    if coins_dui_huan_11 == True:
        text = shop_1.render('已兑换', True, (black))
        screen.blit(text, (450, 345))
    else:
        if starts >= 35:
            text = shop_1.render('兑换', True, (green))
            screen.blit(text, (450, 345))

        else:
            text = shop_1.render('兑换', True, (black))
            screen.blit(text, (450, 345))




def cheng_jiu_pan_duan():
    global cheng_jiu_1_coins, cheng_jiu_1a_coins
    cheng_jiu_1_coins = 0
    cheng_jiu_1a_coins = 0
    if tong_guan_1 == True:
        cheng_jiu_1_coins += 1

    elif tong_guan_1 == False:
        cheng_jiu_1a_coins += 1

    if tong_guan_1 == True and first_level_1 == True and starts_open_1 == True:
        cheng_jiu_1_coins += 1

    elif (tong_guan_1 == False and first_level_1 == False and starts_open_1 == False) or (tong_guan_1 == True and first_level_1 == False and starts_open_1 == False) or (tong_guan_1 == True and first_level_1 == True and starts_open_1 == False) or (tong_guan_1 == True and first_level_1 == False and starts_open_1 == True):
        cheng_jiu_1a_coins += 1

    if e >= 160:
        cheng_jiu_1_coins += 1

    elif e < 160:
        cheng_jiu_1a_coins += 1

    if e >= 280:
        cheng_jiu_1_coins += 1

    elif e < 280:
        cheng_jiu_1a_coins += 1

    if e >= 400:
        cheng_jiu_1_coins += 1

    elif e < 400:
        cheng_jiu_1a_coins += 1

    if upgrade_number >= 2:
        cheng_jiu_1_coins += 1

    elif upgrade_number < 2:
        cheng_jiu_1a_coins += 1

    if upgrade_number >= 4:
        cheng_jiu_1_coins += 1

    elif upgrade_number < 4:
        cheng_jiu_1a_coins += 1

    if upgrade_number >= 6:
        cheng_jiu_1_coins += 1

    elif upgrade_number < 6:
        cheng_jiu_1a_coins += 1

    if hp_upgrade_number == 4:
        cheng_jiu_1_coins += 1

    elif hp_upgrade_number != 4:
        cheng_jiu_1a_coins += 1

    if su_du_upgrade_number == 6:
        cheng_jiu_1_coins += 1

    elif su_du_upgrade_number != 6:
        cheng_jiu_1a_coins += 1

    if coins >= 500:
        cheng_jiu_1_coins += 1

    elif coins < 500:
        cheng_jiu_1a_coins += 1

    if coins >= 1500:
        cheng_jiu_1_coins += 1

    elif coins < 1500:
        cheng_jiu_1a_coins += 1

    if coins >= 4500:
        cheng_jiu_1_coins += 1

    elif coins < 4500:
        cheng_jiu_1a_coins += 1

    if cheng_jiu_1_coins == 13:
        cheng_jiu_1_coins += 1

    elif cheng_jiu_1_coins < 13:
        cheng_jiu_1a_coins += 1




def cheng_jiu_0():
    clock.tick(12)
    global cheng_jiu_cishu_1, cheng_jiu_cishu_2, cheng_jiu_cishu_3, cheng_jiu_cishu_4, cheng_jiu_cishu_5, cheng_jiu_cishu_6, cheng_jiu_cishu_7, cheng_jiu_cishu_8, cheng_jiu_cishu_9, cheng_jiu_cishu_10, cheng_jiu_cishu_11, cheng_jiu_cishu_12, cheng_jiu_cishu_13, cheng_jiu_cishu_14
    cheng_jiu_1_coins = 0
    cheng_jiu_1a_coins = 0
    if tong_guan_1 == True and cheng_jiu_cishu_1 == False:
        cheng_jiu_cishu_1 = True
        text = upgrade.render('成就解锁：开启征途', True, (red))
        screen.blit(text, (240, 23))
        pygame.display.update()
        sleep(1)
        screen.blit(bg_img, (0, 0))

    if tong_guan_1 == True and first_level_1 == True and starts_open_1 == True and cheng_jiu_cishu_2 == False:
        screen.blit(bg_img, (0, 0))
        cheng_jiu_cishu_2 = True
        text = upgrade.render('成就解锁：完美启程', True, (red))
        screen.blit(text, (240, 23))
        pygame.display.update()
        sleep(1)
        screen.blit(bg_img, (0, 0))

    if e >= 160 and cheng_jiu_cishu_3 == False:
        screen.fill(white)
        cheng_jiu_cishu_3 = True
        text = upgrade.render('成就解锁：日常消费', True, (red))
        screen.blit(text, (240, 23))
        pygame.display.update()
        sleep(1)

    if e >= 280 and cheng_jiu_cishu_4 == False:
        screen.fill(white)
        cheng_jiu_cishu_4 = True
        text = upgrade.render('成就解锁：热爱消费', True, (red))
        screen.blit(text, (240, 23))
        pygame.display.update()
        sleep(1)

    if e >= 400 and cheng_jiu_cishu_5 == False:
        screen.fill(white)
        cheng_jiu_cishu_5 = True
        text = upgrade.render('成就解锁：冲动消费', True, (red))
        screen.blit(text, (240, 23))
        pygame.display.update()
        sleep(1)

    if upgrade_number >= 2 and cheng_jiu_cishu_6 == False:
        screen.fill(white)
        cheng_jiu_cishu_6 = True
        text = upgrade.render('成就解锁：增强自己', True, (red))
        screen.blit(text, (240, 23))
        pygame.display.update()
        sleep(1)

    if upgrade_number >= 4 and cheng_jiu_cishu_7 == False:
        screen.fill(white)
        cheng_jiu_cishu_7 = True
        text = upgrade.render('成就解锁：突破自己', True, (red))
        screen.blit(text, (240, 23))
        pygame.display.update()
        sleep(1)

    if upgrade_number >= 6 and cheng_jiu_cishu_8 == False:
        screen.fill(white)
        cheng_jiu_cishu_8 = True
        text = upgrade.render('成就解锁：超越自己', True, (red))
        screen.blit(text, (240, 23))
        pygame.display.update()
        sleep(1)

    if hp_upgrade_number == 4 and cheng_jiu_cishu_9 == False:
        screen.fill(white)
        cheng_jiu_cishu_9 = True
        text = upgrade.render('成就解锁：血量专精', True, (red))
        screen.blit(text, (240, 23))
        pygame.display.update()
        sleep(1)

    if su_du_upgrade_number == 6 and cheng_jiu_cishu_10 == False:
        screen.fill(white)
        cheng_jiu_cishu_10 = True
        text = upgrade.render('成就解锁：速度专精', True, (red))
        screen.blit(text, (240, 23))
        pygame.display.update()
        sleep(1)

    if coins >= 500 and cheng_jiu_cishu_11 == False:
        screen.fill(white)
        cheng_jiu_cishu_11 = True
        text = upgrade.render('成就解锁：富家子弟', True, (red))
        screen.blit(text, (240, 23))
        pygame.display.update()
        sleep(1)

    if coins >= 1500 and cheng_jiu_cishu_12 == False:
        screen.fill(white)
        cheng_jiu_cishu_12 = True
        text = upgrade.render('成就解锁：钱财满贯', True, (red))
        screen.blit(text, (240, 23))
        pygame.display.update()
        sleep(1)

    if coins >= 4500 and cheng_jiu_cishu_13 == False:
        screen.fill(white)
        cheng_jiu_cishu_13 = True
        text = upgrade.render('成就解锁：超级土豪', True, (red))
        screen.blit(text, (240, 23))
        pygame.display.update()
        sleep(1)

    if cheng_jiu_1_coins == 13 and cheng_jiu_cishu_14 == False:
        screen.fill(white)
        cheng_jiu_cishu_14 = True
        text = upgrade.render('成就解锁：13颗星', True, (red))
        screen.blit(text, (240, 23))
        pygame.display.update()
        sleep(1)

    pygame.display.update()



def no_coins():
    while True:
        text = fps_00.render('没金币了呢！', True, (black))
        screen.blit(text, (370, 250))

        text = fps_00.render('lll￢ω￢', True, (black))
        screen.blit(text, (379, 305))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    home_page()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    home_page()

        clock.tick(0.8)
        upgrade_player()



def man():
    text = fps_00.render('已经满级了！', True, (black))
    screen.blit(text, (370, 250))

    text = exit_game.render('[]~￣▽￣~*', True, (black))
    screen.blit(text, (379, 305))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            dianji.play()
            save()
            quit_game()

        elif event.type == KEYDOWN:
            if event.key == ord('r'):
                dianji.play()
                save()
                home_page()

            elif event.key == K_ESCAPE:
                dianji.play()
                save()
                home_page()

    clock.tick(0.8)
    upgrade_player()



def game_shop():
    global coins, hui_fu_number, su_du_number, lower_number, coins_two_number, e, first_enter_shop, shop_donut
    if donut_open == 1 or donut_open == 2:
        if first_enter_shop == False:
            shop_donut = True
            first_enter_shop = True
            donut.block_open_donut()            # 显示第一次进入游戏商店界面时的旁白
    if tong_guan_5 == True:
        coins_two_coins = 24

    else:
        coins_two_coins = 6
    dao_ju_zeng_jia()
    while True:
        cheng_jiu_0()
        clock.tick(5)
        screen.fill(white)
        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    home_page()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    home_page()

                elif event.key == K_1:
                    if coins < hui_fu_coins:
                        no_coins_2()

                    else:
                        coins = coins - hui_fu_coins
                        e += hui_fu_coins
                        hui_fu_number += 1

                elif event.key == K_2:
                    if coins < su_du_coins:
                        no_coins_2()

                    else:
                        coins = coins - su_du_coins
                        e += su_du_coins
                        su_du_number += 1

                elif event.key == K_3:
                    if coins < lower_coins:
                        no_coins_2()

                    else:
                        coins = coins - lower_coins
                        e += lower_coins
                        lower_number += 1

                elif event.key == K_4:
                    if coins < coins_two_coins:
                        no_coins_2()

                    else:
                        coins = coins - coins_two_coins
                        e += coins_two_coins
                        coins_two_number += 1

        back()
        screen.blit(hui_fu_2_img, (25, 50))
        screen.blit(su_du_2_img, (25, 182))
        screen.blit(lower_2_img, (25, 314))
        screen.blit(coins_two_2_img, (25, 446))

        text = upgrade.render(f'生命增加                 拥有：{hui_fu_number}个', True, (black))
        screen.blit(text, (152, 50))

        text = cheng_jiu_1a.render(f'一关中使用后生命增加{hp_zeng_jia}点         购买（{hui_fu_coins}金币）', True, (black))
        screen.blit(text, (152, 80))

        text = upgrade.render(f'速度提升                 拥有：{su_du_number}个', True, (black))
        screen.blit(text, (152, 182))

        text = cheng_jiu_1a.render(f'一关中使用后速度提升{su_du_zeng_jia}点         购买（{su_du_coins}金币）', True, (black))
        screen.blit(text, (152, 212))

        text = upgrade.render(f'敌人速度减少         拥有：{lower_number}个', True, (black))
        screen.blit(text, (152, 314))

        text = cheng_jiu_1a.render(f'一关中使用后敌人速度减少{lower_jian_shao}点         购买（{lower_coins}金币）', True, (black))
        screen.blit(text, (152, 344))

        text = upgrade.render(f'金币翻倍                 拥有：{coins_two_number}个', True, (black))
        screen.blit(text, (152, 446))

        text = cheng_jiu_1a.render(f'一关中使用后金币乘{coins_two_zeng_jia}倍         购买（{coins_two_coins}金币）', True, (black))
        screen.blit(text, (152, 476))

        if tips == True:
            text = shop_1.render('1', True, (black))
            screen.blit(text, (720, 80))

            text = shop_1.render('2', True, (black))
            screen.blit(text, (720, 212))

            text = shop_1.render('3', True, (black))
            screen.blit(text, (720, 344))

            text = shop_1.render('4', True, (black))
            screen.blit(text, (720, 476))

        pygame.display.update()



def no_coins_2():
    while True:
        back()
        screen.blit(hui_fu_2_img, (25, 50))
        screen.blit(su_du_2_img, (25, 182))
        screen.blit(lower_2_img, (25, 314))
        screen.blit(coins_two_2_img, (25, 446))

        text = upgrade.render(f'生命增加                 拥有：{hui_fu_number}个', True, (black))
        screen.blit(text, (152, 50))

        text = cheng_jiu_1a.render(f'一关中使用后生命增加{hp_zeng_jia}点         购买（{hui_fu_coins}金币）', True, (black))
        screen.blit(text, (152, 80))

        text = upgrade.render(f'速度提升                 拥有：{su_du_number}个', True, (black))
        screen.blit(text, (152, 182))

        text = cheng_jiu_1a.render(f'一关中使用后速度提升{su_du_zeng_jia}点         购买（{su_du_coins}金币）', True, (black))
        screen.blit(text, (152, 212))

        text = upgrade.render(f'敌人速度减少         拥有：{lower_number}个', True, (black))
        screen.blit(text, (152, 314))

        text = cheng_jiu_1a.render(f'一关中使用后敌人速度减少{lower_jian_shao}点         购买（{lower_coins}金币）', True, (black))
        screen.blit(text, (152, 344))

        text = upgrade.render(f'金币翻倍                 拥有：{coins_two_number}个', True, (black))
        screen.blit(text, (152, 446))

        text = cheng_jiu_1a.render(f'一关中使用后金币增加{coins_two_zeng_jia}倍         购买（{coins_two_coins}金币）', True, (black))
        screen.blit(text, (152, 476))

        if tips == True:
            text = shop_1.render('1', True, (black))
            screen.blit(text, (720, 80))

            text = shop_1.render('2', True, (black))
            screen.blit(text, (720, 212))

            text = shop_1.render('3', True, (black))
            screen.blit(text, (720, 344))

            text = shop_1.render('4', True, (black))
            screen.blit(text, (720, 476))

        text = fps_00.render('没金币了呢！', True, (black))
        screen.blit(text, (260, 490))

        text = fps_00.render('￣_￣|||', True, (black))
        screen.blit(text, (290, 540))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    home_page()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    home_page()

        clock.tick(0.8)
        game_shop()



def level():
    global ticks
    while True:
        ticks += 1
        clock.tick(12)

        screen.fill(white)

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    home_page()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    home_page()

                elif event.key == K_1:
                    dianji.play()
                    level_select()

                elif event.key == K_2:
                    dianji.play()
                    pass

        back()

        text = start.render('1.闯关模式', True, (black))
        screen.blit(text, (298, 100))

        text = start.render('2.无尽模式', True, (black))
        screen.blit(text, (298, 160))

        if ticks % 12 < 6:
            screen.blit(player_img, (335 , 420))
        else:
            screen.blit(player_img_2, (335 , 420))

        pygame.display.update()



def level_select():
    global level_1, level_2, level_3, level_4, level_5, fps
    while True:
        clock.tick(24)
        screen.fill(white)
        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == K_1:
                    dianji.play()
                    level_1 = True
                    level_start()

                elif event.key == K_2:
                    if tong_guan_1 == True:
                        dianji.play()
                        level_2 = True
                        level_start()

                    else:
                        level_no()

                elif event.key == K_3:
                    if tong_guan_2 == True:
                        dianji.play()
                        level_3 = True
                        level_start()

                    else:
                        level_no()

                elif event.key == K_4:
                    if tong_guan_3 == True:
                        dianji.play()
                        level_4 = True
                        level_start()

                    else:
                        level_no()

                elif event.key == K_5:
                    if tong_guan_4 == True:
                        dianji.play()
                        level_5 = True
                        level_start()

                    else:
                        level_no()

                elif event.key == K_6:
                    dianji.play()
                    level_select()
                    level_start()

                elif event.key == K_7:
                    dianji.play()
                    level_select()
                    level_start()

                elif event.key == ord('r'):
                    dianji.play()
                    level()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    level()

        back()

        text = select.render('1     2     3', True, (black))
        screen.blit(text, (135, 25))

        text = select.render('4     5     6     7', True, (black))
        screen.blit(text, (10, 400))

        if tong_guan_1 == True:
            if starts_open_1 == True:
                text = upgrade.render('★', True, (blue))
                screen.blit(text, (150, 150))

            else:
                screen.blit(tong_guan_img, (150, 150))

        if tong_guan_2 == True:
            if starts_open_2 == True:
                text = upgrade.render('★', True, (blue))
                screen.blit(text, (365, 150))

            else:
                screen.blit(tong_guan_img, (365, 150))

        if tong_guan_3 == True:
            if starts_open_3 == True:
                text = upgrade.render('★', True, (blue))
                screen.blit(text, (580, 150))

            else:
                screen.blit(tong_guan_img, (580, 150))

        if tong_guan_4 == True:
            if starts_open_4 == True:
                text = upgrade.render('★', True, (blue))
                screen.blit(text, (35, 525))

            else:
                screen.blit(tong_guan_img, (35, 525))

        if tong_guan_5 == True:
            if starts_open_5 == True:
                text = upgrade.render('★', True, (blue))
                screen.blit(text, (240, 525))

            else:
                screen.blit(tong_guan_img, (240, 525))

        if tips == True:
            text = a_00.render('使用 w a s d 或者 上下左右 来移动', True, (green))
            screen.blit(text, (15, 200))

            text = exit_game.render('用数字键来选关，R键来返回', True, (green))
            screen.blit(text, (150, 250))

        else:
            text = a_00.render('感谢您的游玩！', True, (green))
            screen.blit(text, (230, 200))

            text = exit_game.render('ヾ≧▽≦*o', True, (green))
            screen.blit(text, (290, 250))

        pygame.display.update()



def level_no():
    while True:
        clock.tick(fps)
        screen.fill(white)
        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ESCAPE:
                    dianji.play()
                    save()
                    quit_game()

        text = fps_00.render('请先通关上一关！', True, (black))
        screen.blit(text, (240, 240))

        text = exit_game.render('←o(=•ェ•=)m←', True, (black))
        screen.blit(text, (270, 290))

        pygame.display.update()
        clock.tick(0.8)
        level_select()



def level_start():
    global ticks, player_X, player_Y, player_x, player_y, score, fps, hp_coloer, hp, hp_3, player_img, a, player_speed_4, clock, ko, clock_2, clock_3
    hp = hp_3
    fps = fps_1
    player_speed = player_speed_4
    if ok == False:
        play_game()
    else:
        while True:
            player_img = pygame.image.load('图片\玩家1.png')
            clock.tick(fps)
            ticks += 1
            screen.blit(bg_img, (0, 0))
            if ticks % 64 < 32:
                screen.blit(player_img, (player_X, player_Y))
            else:
                screen.blit(player_img_2, (player_X, player_Y))
            screen.blit(stop_game, (0, 0))

            score += 0.25

            hp_coloer_1()

            for event in pygame.event.get():
                if event.type == QUIT:
                    dianji.play()
                    save()
                    quit_game()

                elif event.type == KEYDOWN:
                    if event.key == ord('w') or event.key == K_UP:
                        player_y = -player_speed

                    elif event.key == ord('w') and ord('a'):
                        player_y = -player_speed
                        player_x = -player_speed

                    elif event.key == ord('w') and ord('d'):
                        player_y = -player_speed
                        player_x = player_speed



                    elif event.key == ord('s') or event.key == K_DOWN:
                        player_y = player_speed

                    elif event.key == ord('s') and ord('a'):
                        player_y = player_speed
                        player_x = -player_speed

                    elif event.key == ord('s') and ord('d'):
                        player_y = player_speed
                        player_x = player_speed



                    elif event.key == ord('a') or event.key == K_LEFT:
                        player_x = -player_speed

                    elif event.key == ord('d') or event.key == K_RIGHT:
                        player_x = player_speed

                    elif event.key == ord('r'):
                        dianji.play()
                        restet_all()
                        level_select()

                    elif event.key == K_ESCAPE:
                        dianji.play()
                        restet_all()
                        level_select()

                    elif event.key == ord('t'):
                        zan_tin()

                elif event.type == KEYUP:
                    player_x = 0
                    player_y = 0

            player_X += player_x
            player_Y += player_y

            if player_X > 700:
                player_X = 700

            elif player_X < 0:
                player_X = 0

            elif player_Y > 478:
                player_Y = 478

            elif player_Y < 0:
                player_Y = 0

            text = upgrade.render(f'{score}', True, (green))
            screen.blit(text, (370, 0))

            text = upgrade.render(f'{hp}', True, (hp_coloer))
            screen.blit(text, (760, 560))


            if hp <= 0:
                screen.blit(bg_img, (0, 0))
                game_over_2()

            if ok_2 == True:
                if score >= 580:
                    screen.blit(bg_img, (0, 0))
                    win()

            elif ok_3 == True or ok_4 == True:
                if score >= 860:
                    screen.blit(bg_img, (0, 0))
                    win()

            elif ok_5 == True:
                if score >= 1140:
                    screen.blit(bg_img, (0, 0))
                    win()

            elif score >= 300:
                screen.blit(bg_img, (0, 0))
                win()
            
            

            for e in dicis:
                e.dici_Y += e.dici_speed
                if e.dici_Y > 567:
                    e.restet()

                screen.blit(e.dici_img, (e.dici_X, e.dici_Y))

                if (hurt(player_X, player_Y, e.dici_X, e.dici_Y) < 52):
                    e.restet()
                    if hp > 0:
                        hp -= 1
                        pygame.display.update()
                        screen.blit(e.dici_img, (e.dici_X, e.dici_Y))
                        pygame.display.update()
                        ko = True
                        clock_2 = pygame.time.Clock()
                        clock_3 = 0
                        while ko:
                            clock_3 += clock_2.tick()
                            if clock_3 >= 80 and clock_3 <= 120:
                                player_img = pygame.image.load('图片\玩家坠毁1.png')
                                screen.blit(player_img, (player_X, player_Y))
                                pygame.display.update()
                                player_img = pygame.image.load('图片\玩家坠毁1.png')
                                screen.blit(player_img, (player_X, player_Y))
                                pygame.display.update()
                            elif clock_3 >= 120 and clock_3 <= 160:
                                player_img = pygame.image.load('图片\玩家坠毁2.png')
                                screen.blit(player_img, (player_X, player_Y))
                                pygame.display.update()
                                player_img = pygame.image.load('图片\玩家坠毁2.png')
                                screen.blit(player_img, (player_X, player_Y))
                                pygame.display.update()
                            elif clock_3 >= 160 and clock_3 <= 200:
                                player_img = pygame.image.load('图片\玩家坠毁3.png')
                                screen.blit(player_img, (player_X, player_Y))
                                pygame.display.update()
                                player_img = pygame.image.load('图片\玩家坠毁3.png')
                                screen.blit(player_img, (player_X, player_Y))
                                pygame.display.update()
                            elif clock_3 >= 200 and clock_3 <= 240:
                                ko = False
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    dianji.play()
                                    quit_game()
                                elif event.type == KEYDOWN:
                                    if event.key == ord('r'):
                                        dianji.play()
                                        quit_game()
                                    elif event.key == ESCAPE:
                                        dianji.play()
                                        quit_game()



            if ok_2 == True or ok_3 == True or ok_4 == True or ok_5 == True:
                for e in dicis_2:
                    e.dici_2_Y += e.dici_2_speed
                    if e.dici_2_Y > 567:
                        e.restet_2()

                    screen.blit(e.dici_2_img, (e.dici_2_X, e.dici_2_Y))

                    if (hurt(player_X, player_Y, e.dici_2_X, e.dici_2_Y) < 58):
                        e.restet_2()
                        if hp > 0:
                            hp -= 1
                            pygame.display.update()
                            screen.blit(e.dici_2_img, (e.dici_2_X, e.dici_2_Y))
                            pygame.display.update()
                            ko = True
                            clock_2 = pygame.time.Clock()
                            clock_3 = 0
                            while ko:
                                clock_3 += clock_2.tick()
                                if clock_3 >= 80 and clock_3 <= 120:
                                    player_img = pygame.image.load('图片\玩家坠毁1.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                    player_img = pygame.image.load('图片\玩家坠毁1.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                elif clock_3 >= 120 and clock_3 <= 160:
                                    player_img = pygame.image.load('图片\玩家坠毁2.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                    player_img = pygame.image.load('图片\玩家坠毁2.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                elif clock_3 >= 160 and clock_3 <= 200:
                                    player_img = pygame.image.load('图片\玩家坠毁3.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                    player_img = pygame.image.load('图片\玩家坠毁3.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                elif clock_3 >= 200 and clock_3 <= 240:
                                    ko = False
                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        dianji.play()
                                        quit_game()
                                    elif event.type == KEYDOWN:
                                        if event.key == ord('r'):
                                            dianji.play()
                                            quit_game()
                                        elif event.key == ESCAPE:
                                            dianji.play()
                                            quit_game()



            if ok_5 == True:
                for e in bullets:

                    if e.dici_3_bullet_X > 764:
                        e.bullet_restet()

                    k = random.randint(0, 2)
                    if k == 0:
                        e.dici_3_bullet_X += e.dici_3_bullet_speed

                    elif k == 1:
                        e.dici_3_bullet_X += 2
                        e.dici_3_bullet_Y -= 1

                    else:
                        e.dici_3_bullet_X += 2
                        e.dici_3_bullet_Y += 1

                    screen.blit(e.dici_3_bullet_img, (e.dici_3_bullet_X, e.dici_3_bullet_Y))

                    if (hurt(player_X, player_Y, e.dici_3_bullet_X, e.dici_3_bullet_Y) < 64):
                        e.bullet_restet()
                        if hp > 0:
                            hp -= 1
                            screen.blit(e.dici_3_bullet_img, (e.dici_3_bullet_X, e.dici_3_bullet_Y))
                            pygame.display.update()
                            ko = True
                            clock_2 = pygame.time.Clock()
                            clock_3 = 0
                            while ko:
                                clock_3 += clock_2.tick()
                                if clock_3 >= 80 and clock_3 <= 120:
                                    player_img = pygame.image.load('图片\玩家坠毁1.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                    player_img = pygame.image.load('图片\玩家坠毁1.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                elif clock_3 >= 120 and clock_3 <= 160:
                                    player_img = pygame.image.load('图片\玩家坠毁2.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                    player_img = pygame.image.load('图片\玩家坠毁2.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                elif clock_3 >= 160 and clock_3 <= 200:
                                    player_img = pygame.image.load('图片\玩家坠毁3.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                    player_img = pygame.image.load('图片\玩家坠毁3.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                elif clock_3 >= 200 and clock_3 <= 240:
                                    ko = False
                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        dianji.play()
                                        quit_game()
                                    elif event.type == KEYDOWN:
                                        if event.key == ord('r'):
                                            dianji.play()
                                            quit_game()
                                        elif event.key == ESCAPE:
                                            dianji.play()
                                            quit_game()

                for e in dicis_3:
                    e.dici_3_Y += e.dici_3_speed
                    if e.dici_3_Y > 548:
                        e.restet_3()

                    screen.blit(e.dici_3_img, (e.dici_3_X, e.dici_3_Y))

                    if (hurt(player_X, player_Y, e.dici_3_X, e.dici_3_Y) < 55):
                        e.restet_3()
                        if hp > 0:
                            hp -= 1
                            pygame.display.update()
                            screen.blit(e.dici_3_img, (e.dici_3_X, e.dici_3_Y))
                            pygame.display.update()
                            ko = True
                            clock = pygame.time.Clock()
                            clock_3 = 0
                            while ko:
                                clock_3 += clock_2.tick()
                                if clock_3 >= 80 and clock_3 <= 120:
                                    player_img = pygame.image.load('图片\玩家坠毁1.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                    player_img = pygame.image.load('图片\玩家坠毁1.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                elif clock_3 >= 120 and clock_3 <= 160:
                                    player_img = pygame.image.load('图片\玩家坠毁2.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                    player_img = pygame.image.load('图片\玩家坠毁2.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                elif clock_3 >= 160 and clock_3 <= 200:
                                    player_img = pygame.image.load('图片\玩家坠毁3.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                    player_img = pygame.image.load('图片\玩家坠毁3.png')
                                    screen.blit(player_img, (player_X, player_Y))
                                    pygame.display.update()
                                elif clock_3 >= 200 and clock_3 <= 240:
                                    ko = False
                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        dianji.play()
                                        quit_game()
                                    elif event.type == KEYDOWN:
                                        if event.key == ord('r'):
                                            dianji.play()
                                            quit_game()
                                        elif event.key == ESCAPE:
                                            dianji.play()
                                            quit_game()
                                    
            pygame.display.update()



def zan_tin():
    screen.blit(bg_img, (0, 0))
    screen.blit(player_img, (player_X, player_Y))
    for e in dicis:
        screen.blit(e.dici_img, (e.dici_X, e.dici_Y))

    for e in dicis_2:
        screen.blit(e.dici_2_img, (e.dici_2_X, e.dici_2_Y))

    for e in dicis_3:
        screen.blit(e.dici_3_img, (e.dici_3_X, e.dici_3_Y))

    for e in bullets:
        screen.blit(e.dici_3_bullet_img, (e.dici_3_bullet_X, e.dici_3_bullet_Y))
    
    text = upgrade.render(f'{score}', True, (green))
    screen.blit(text, (370, 0))

    text = upgrade.render(f'{hp}', True, (hp_coloer))
    screen.blit(text, (760, 560))

    text = a_00.render('暂停', True, (red))
    screen.blit(text, (120, 150))

    text = stop_tips_1.render('返回', True, (red))
    screen.blit(text, (100, 220))

    text = stop_tips_1.render('继续游戏', True, (red))
    screen.blit(text, (100, 270))

    text = stop_tips_1.render('重新开始', True, (red))
    screen.blit(text, (100, 320))

    text = stop_tips_1.render('返回主页', True, (red))
    screen.blit(text, (100, 370))

    text = stop_tips_1.render('退出游戏', True, (red))
    screen.blit(text, (100, 420))

    if tips == True:
       text = stop_tips_1.render('R.', True, (red))
       screen.blit(text, (60, 220))

       text = stop_tips_1.render('C.', True, (red))
       screen.blit(text, (60, 270))

       text = stop_tips_1.render('H.', True, (red))
       screen.blit(text, (60, 370))

       text = stop_tips_1.render('E.', True, (red))
       screen.blit(text, (60, 320))

       text = stop_tips_1.render('Q.', True, (red))
       screen.blit(text, (60, 420))                            
       pygame.display.update()

    while True:
       clock.tick(5)
       for event in pygame.event.get():
           if event.type == QUIT:
               dianji.play()
               quit_game()

           elif event.type == KEYDOWN:
               if event.key == ord('r'):
                   dianji.play()
                   restet_all()
                   level_select()

               elif event.key == ord('c'):
                   dianji.play()
                   level_start()

               elif event.key == ord('h'):
                   dianji.play()
                   restet_all()
                   home_page()

               elif event.key == ord('q'):
                   dianji.play()
                   restet_all()
                   quit_game()

               elif event.key == ord('e'):
                   dianji.play()
                   restet_all_2()
                   xing_xi()

               elif event.key == K_ESCAPE:
                   dianji.play()
                   level_start()

def restet_all():
    global hp, hp_3, player_speed, player_speed_4, hui_fu_ci_shu, su_du_ci_shu, lower_ci_shu, coins_two_ci_shu, player_X, player_Y, player_x, player_y, score, coins_two, wins, game_overs
    for e in dicis:
        e.restet()

    for e in dicis_2:
        e.restet_2()

    for e in dicis_3:
        e.restet_3()

    for e in bullets:
        e.bullet_restet()

    for e in dicis:
        e.dici_speed = 3

    for e in dicis_2:
        e.dici_2_speed = 2

    for e in dicis_3:
        e.dici_3_speed = 4
    hp = hp_00
    hp_3 = hp_00
    player_speed = player_speed_00
    player_speed_4 = player_speed_00
    hui_fu_ci_shu = 0
    su_du_ci_shu = 0
    lower_ci_shu = 0
    coins_two_ci_shu = 0
    player_X = 360
    player_Y = 478
    player_y = 0
    player_x = 0
    score = 0
    coins_two = False
    wins = False
    game_overs = False
    level_false()
    ok_false()
    save()

def restet_all_2():
    global hp, hp_3, player_speed, player_speed_4, hui_fu_ci_shu, su_du_ci_shu, lower_ci_shu, coins_two_ci_shu, player_X, player_Y, player_x, player_y, score, coins_two, wins, game_overs
    for e in dicis:
        e.restet()

    for e in dicis_2:
        e.restet_2()

    for e in dicis_3:
        e.restet_3()

    for e in bullets:
        e.bullet_restet()

    for e in dicis:
        e.dici_speed = 3

    for e in dicis_2:
        e.dici_2_speed = 2

    for e in dicis_3:
        e.dici_3_speed = 4
    hp = hp_00
    hp_3 = hp_00
    player_speed = player_speed_00
    player_speed_4 = player_speed_00
    hui_fu_ci_shu = 0
    su_du_ci_shu = 0
    lower_ci_shu = 0
    coins_two_ci_shu = 0
    player_X = 360
    player_Y = 478
    player_y = 0
    player_x = 0
    score = 0
    coins_two = False
    wins = False
    game_overs = False
    save()



def hp_coloer_1():
    global hp_coloer
    if hp_3 == 3 :
        if hp <= 1:
            hp_coloer = red

        elif hp == 2:
            hp_coloer = yellow

        elif hp >= hp_3:
            hp_coloer = green



    elif hp_3 == 4:
        if hp < hp_3 // 2:
            hp_coloer = red

        elif hp == hp_3 // 2:
            hp_coloer = yellow

        elif hp >= (hp_3 // 2 + 1):
            hp_coloer = green



    elif hp_3 == 5:
        if hp <= (hp_3 // 2 - 1):
            hp_coloer = red

        elif hp >= 2 and hp <= 3:
            hp_coloer = yellow

        elif hp > (hp_3 // 2 + 1):
            hp_coloer = green


    elif hp_3 == 6:
        if hp <= (hp_3 // 2 - 2):
            hp_coloer = red

        elif hp >= (hp_3 // 2 - 1) and hp <= (hp_3 // 2 + 1):
            hp_coloer = yellow

        elif hp > (hp_3 // 2 + 1):
            hp_coloer = green

    elif hp_3 == 7:
        if hp <= (hp_3 // 2 - 2):
            hp_coloer = red

        elif hp >= (hp_3 // 2 - 1) and hp <= (hp_3 // 2 + 2):
            hp_coloer = yellow

        elif hp > (hp_3 // 2 + 2):
            hp_coloer = green

    elif hp_3 == 8:
        if hp <= (hp_3 // 2 - 3):
            hp_coloer = red

        elif hp >= 2 and hp <= 6:
            hp_coloer = yellow

        elif hp > (hp_3 // 2 + 2):
            hp_coloer = green

    elif hp_3 == 9:
        if hp <= 1:
            hp_coloer = red

        elif hp >= 3 and hp <= 7:
            hp_coloer = yellow

        elif hp > 7:
            hp_coloer = green

    elif hp_3 == 10:
        if hp <= 2:
            hp_coloer = red

        elif hp >= 3 and hp <= 7:
            hp_coloer = yellow

        elif hp > 8:
            hp_coloer = green

    elif hp_3 == 11:
        if hp <= 3:
            hp_coloer = red

        elif hp >= 4 and hp <= 8:
            hp_coloer = yellow

        elif hp > 9:
            hp_coloer = green

    elif hp_3 == 12:
        if hp <= 4:
            hp_coloer = red

        elif hp >= 5 and hp <= 9:
            hp_coloer = yellow

        elif hp > 10:
            hp_coloer = green

    elif hp_3 == 13:
        if hp <= 5:
            hp_coloer = red

        elif hp >= 6 and hp <= 10:
            hp_coloer = yellow

        elif hp > 11:
            hp_coloer = green

    elif hp_3 == 14:
        if hp <= 6:
            hp_coloer = red

        elif hp >= 7 and hp <= 11:
            hp_coloer = yellow

        elif hp > 12:
            hp_coloer = green

    elif hp_3 == 15:
        if hp <= 7:
            hp_coloer = red

        elif hp >= 8 and hp <= 12:
            hp_coloer = yellow

        elif hp > 13:
            hp_coloer = green

    elif hp_3 == 16:
        if hp <= 8:
            hp_coloer = red

        elif hp >= 9 and hp <= 13:
            hp_coloer = yellow

        elif hp > 14:
            hp_coloer = green



def game_over_2():
    global player_y, player_x, hp, hp_3, player_speed, player_speed_4, hui_fu_ci_shu, su_du_ci_shu, score, player_X, player_Y, die_number, game_overs
    game_over_sound.play()
    game_overs = True
    die_number += 1
    while True:

        clock.tick(5)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    restet_all()
                    level_select()

                elif event.key == ord('t'):
                    dianji.play()
                    restet_all_2()
                    xing_xi()

                elif event.key == ord('h'):
                    dianji.play()
                    restet_all()
                    home_page()

                elif event.key == ord('q'):
                    dianji.play()
                    restet_all()
                    quit_game()

                elif event.key == ord('u'):
                    dianji.play()
                    restet_all()
                    upgrade_player()

                elif event.key == ord('s'):
                    dianji.play()
                    restet_all()
                    game_shop()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    restet_all()
                    level()

        back()

        if level_1 == True:
            level_name = '一'
        elif level_2 == True:
            level_name = '二'
        elif level_3 == True:
            level_name = '三'
        elif level_4 == True:
            level_name = '四'
        elif level_5 == True:
            level_name = '五'

        text = tips_game_over.render('坠毁', True, (red))
        screen.blit(text, (20, 50))

        text = score_look.render(f'失败关卡：第{level_name}关', True, (red))
        screen.blit(text, (395, 10))

        text = score_look.render(f'通关分数：{score}', True, (red))
        screen.blit(text, (395, 70))

        if level_1 == True:
            text = score_look.render(f'通关还差：{300 - score}分', True, (red))
            screen.blit(text, (395, 130))

        elif level_2 == True:
            text = score_look.render(f'通关还差：{580 - score}分', True, (red))
            screen.blit(text, (395, 130))

        elif level_3 == True or level_4 == True:
            text = score_look.render(f'通关还差：{860 - score}分', True, (red))
            screen.blit(text, (395, 130))

        elif level_5 == True:
            text = score_look.render(f'通关还差：{1140 - score}分', True, (red))
            screen.blit(text, (395, 130))

        text = upgrade.render('主页', True, (red))
        screen.blit(text, (130, 440))

        text = upgrade.render('再战', True, (red))
        screen.blit(text, (330, 440))

        text = upgrade.render('继续', True, (red))
        screen.blit(text, (530, 440))

        text = upgrade.render('升级', True, (red))
        screen.blit(text, (230, 350))

        text = upgrade.render('商店', True, (red))
        screen.blit(text, (430, 350))

        if tips == True:
            text = upgrade.render('H', True, (red))
            screen.blit(text, (150, 415))

            text = upgrade.render('T', True, (red))
            screen.blit(text, (350, 415))

            text = upgrade.render('N', True, (red))
            screen.blit(text, (550, 415))

            text = upgrade.render('U', True, (red))
            screen.blit(text, (250, 325))

            text = upgrade.render('S', True, (red))
            screen.blit(text, (450, 325))

        pygame.display.update()



def win():
    global player_y, player_x, player_speed, player_speed_4, hui_fu_ci_shu, su_du_ci_shu, level_ok_number, hp, hp_3, player_X, player_Y, reward, coins, first_level_1, first_level_2, first_level_3, first_level_4, tong_guan_1, tong_guan_2, tong_guan_3, tong_guan_4, starts_open_1, starts_open_2, starts_open_3, starts_open_4, starts, score, wins, cheng_jiu_open, shop_open, upgrade_open
    win_sound.play()
    wins = True
    level_ok_number += 1
    if level_1 == True:
        if hp == hp_3 and starts_open_1 == False:
            reward = 6
            starts += 1
            starts_open_1 = True
            first_level_1 = True
            tong_guan_1 = True

        elif first_level_1 == False:
            reward = 5
            first_level_1 = True
            tong_guan_1 = True
            cheng_jiu_open = True

        else:
            reward = 4



    elif level_2 == True:
        if hp == hp_3 and starts_open_2 == False:
            reward = 8
            starts += 1
            starts_open_2 = True
            first_level_2 = True
            tong_guan_2 = True

        elif first_level_2 == False:
            reward = 7
            first_level_2 = True
            tong_guan_2 = True
            shop_open = True

        else:
            reward = 6



    elif level_3 == True:
        if hp == hp_3 and starts_open_3 == False:
            reward = 10
            starts += 1
            starts_open_3 = True
            first_level_3 = True
            tong_guan_3 = True

        elif first_level_3 == False:
            reward = 9
            first_level_3 = True
            tong_guan_3 = True
            upgrade_open = True

        else:
            reward = 8



    elif level_4 == True:
        if hp == hp_3 and starts_open_4 == False:
            reward = 12
            starts += 1
            starts_open_4 = True
            first_level_4 = True
            tong_guan_4 = True

        elif first_level_3 == False:
            reward = 11
            first_level_4 = True
            tong_guan_4 = True

        else:
            reward = 10

    elif level_5 == True:
        if hp == hp_3 and starts_open_4 == False:
            reward = 14
            starts += 1
            starts_open_4 = True
            first_level_4 = True
            tong_guan_4 = True

        elif first_level_3 == False:
            reward = 13
            first_level_4 = True
            tong_guan_4 = True
            tong_ji_open = True

        else:
            reward = 12



    if coins_two == True:
        coins += reward * 2
        reward = reward * 2

    else:
        coins += reward
    if cheng_jiu_cishu_1 == False:
        cheng_jiu_0()

    while True:
        clock.tick(3)
        screen.blit(bg_img, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    restet_all()
                    level_select()

                elif event.key == ord('n'):
                    dianji.play()
                    restet_all_2()
                    next_level()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    restet_all()
                    level()

                elif event.key == ord('t'):
                    dianji.play()
                    restet_all_2()
                    xing_xi()

                elif event.key == ord('h'):
                    dianji.play()
                    restet_all()
                    home_page()

                elif event.key == ord('u'):
                    dianji.play()
                    restet_all()
                    upgrade_player()

                elif event.key == ord('s'):
                    dianji.play()
                    restet_all()
                    game_shop()

        back()
        hp_coloer_1()
        text = upgrade.render(f'{hp}', True, (hp_coloer))
        screen.blit(text, (775, 560))

        text = score_look.render(f'你还有{hp}滴血！', True, (green))
        screen.blit(text, (270, 500))

        if level_1 == True:
            level_name = '一'
        elif level_2 == True:
            level_name = '二'
        elif level_3 == True:
            level_name = '三'
        elif level_4 == True:
            level_name = '四'
        elif level_5 == True:
            level_name = '五'

        text = tips_game_over.render('通关', True, (green))
        screen.blit(text, (20, 50))

        text = score_look.render(f'通关关卡：第{level_name}关', True, (green))
        screen.blit(text, (395, 10))

        text = score_look.render(f'通关分数：{score}', True, (green))
        screen.blit(text, (395, 70))

        text = score_look.render(f'获得金币：{reward}', True, (green))
        screen.blit(text, (395, 130))

        if hp == hp_3:
            text = score_look.render('完美通关o゜▽゜o☆', True, (green))
            screen.blit(text, (395, 190))

        text = upgrade.render('主页', True, (green))
        screen.blit(text, (130, 440))

        text = upgrade.render('再战', True, (green))
        screen.blit(text, (330, 440))

        text = upgrade.render('继续', True, (green))
        screen.blit(text, (530, 440))

        text = upgrade.render('升级', True, (green))
        screen.blit(text, (230, 350))

        text = upgrade.render('商店', True, (green))
        screen.blit(text, (430, 350))

        if tips == True:
            text = upgrade.render('H', True, (green))
            screen.blit(text, (150, 415))

            text = upgrade.render('T', True, (green))
            screen.blit(text, (350, 415))

            text = upgrade.render('N', True, (green))
            screen.blit(text, (550, 415))

            text = upgrade.render('U', True, (green))
            screen.blit(text, (250, 325))

            text = upgrade.render('S', True, (green))
            screen.blit(text, (450, 325))

        pygame.display.update()



def next_level():
    global level_2, level_3, level_4, level_5, hp, player_X, player_Y, score
    hp = hp_3
    for e in dicis:
        e.restet()

    for e in dicis_2:
        e.restet_2()
    player_X = 360
    player_Y = 478
    score = 0
    if level_1 == True:
        ok_false()
        level_false()
        level_2 = True
        play_game()

    elif level_2 == True:
        ok_false()
        level_false()
        level_3 = True
        play_game()

    elif level_3 == True:
        ok_false()
        level_false()
        level_4 = True
        play_game()

    elif level_4 == True:
        ok_false()
        level_false()
        level_5 = True
        play_game()

    else:
        ok_false()
        level_false()
        screen.fill(white)
        text = fps_00.render('这是最后一关！', True, (black))
        screen.blit(text, (260, 240))
        text = exit_game.rander('ヾ≧ ▽ ≦ゝ', True, (black))
        screen.blit(text, (280, 320))
        clock.tick(0.8)



def level_false():
    global level_1, level_2, level_3, level_4, level_5
    level_1 = False
    level_2 = False
    level_3 = False
    level_4 = False
    level_5 = False


def ok_false():
    global ok, ok_2, ok_3, ok_4, ok_5, dicis, dicis_2, dicis_3
    ok = False
    ok_2 = False
    ok_3 = False
    ok_4 = False
    ok_5 = False
    dicis = []
    dicis_2 = []
    dicis_3 = []



def play_game():
    global open_level, dici_number, dici_2_number, dici_3_number, ok, ok_2, ok_3, ok_4, ok_5, dici_zhong_lei, level_tips_4
    dici_number = 0
    dici_2_number = 0
    if level_1 == True:
        open_level += 1
        dici_number = 6
        for i in range(dici_number):
            dicis.append(dici())
        ok = True

        level_tips_4 = '通关条件：撑到300分'
        dici_zhong_lei = 1

        xing_xi()

    elif level_2 == True:
        open_level += 1
        dici_number = 5
        dici_2_number = 3
        for i in range(dici_number):
            dicis.append(dici())

        for i in range(dici_2_number):
            dicis_2.append(dici_2())
        ok = True
        ok_2 = True

        dici_zhong_lei = 2

        level_tips_4 = '通关条件：撑到580分'
        xing_xi()

    elif level_3 == True:
        open_level += 1
        dici_number = 6
        dici_2_number = 3
        for i in range(dici_number):
            dicis.append(dici())

        for i in range(dici_2_number):
            dicis_2.append(dici_2())

        for e in dicis:
            e.dici_speed = 4

        for e in dicis_2:
            e.dici_2_speed = 3
        ok = True
        ok_3 = True

        dici_zhong_lei = 2

        level_tips_4 = '通关条件：撑到860分'
        xing_xi()

    elif level_4 == True:
        open_level += 1
        dici_number = 5
        dici_2_number = 8
        for i in range(dici_number):
            dicis.append(dici())

        for i in range(dici_2_number):
            dicis_2.append(dici_2())

        ok = True
        ok_4 = True

        dici_zhong_lei = 2

        level_tips_4 = '通关条件：撑到860分'
        xing_xi()

    elif level_5 == True:
        open_level += 1
        dici_number = 4
        dici_2_number = 4
        dici_3_number = 1
        for i in range(dici_number):
            dicis.append(dici())

        for i in range(dici_2_number):
            dicis_2.append(dici_2())

        for i in range(dici_3_number):
            dicis_3.append(dici_3())

        for i in range(2):
            bullets.append(bullet())

        ok = True
        ok_5 = True

        dici_zhong_lei = 3

        level_tips_4 = '通关条件：撑到1140分'
        xing_xi()

    save()
    level_start()




def xing_xi():
    global level_number, hui_fu_number, su_du_number, lower_number, coins_two_number, hp, hp_3, hp_00, player_speed, player_speed_00, player_speed_4, hui_fu_ci_shu, su_du_ci_shu, lower_ci_shu, coins_two_ci_shu, coins_two
    dao_ju_zeng_jia()
    while True:
        clock.tick(5)
        screen.fill(white)
        back()
        text = score_look.render(f'敌方总数量：{dici_number + dici_2_number}', True, (green))
        screen.blit(text, (0, 30))

        text = score_look.render(f'敌方种类：{dici_zhong_lei}种', True, (green))
        screen.blit(text, (500, 30))

        text = score_look.render('敌方阵营：', True, (green))
        screen.blit(text, (0, 90))

        text = score_look.render(f'尖刺：{dici_number}个', True, (green))
        screen.blit(text, (0, 150))
        for e in dicis:
            screen.blit(e.dici_img, (25, 200))

        if dici_2_number != 0:
            text = score_look.render(f'长块：{dici_2_number}个', True, (green))
            screen.blit(text, (300, 150))
            for e in dicis_2:
                screen.blit(e.dici_2_img, (325, 200))

        if dici_3_number != 0:
            text = score_look.render(f'激光：{dici_3_number}个', True, (green))
            screen.blit(text, (600, 150))
            for e in dicis_3:
                screen.blit(e.dici_3_img, (625, 200))

        text = exit_game.render(f'{level_tips_4}', True, (red))
        screen.blit(text, (0, 540))

        screen.blit(hui_fu_img, (528, 350))
        screen.blit(su_du_img, (638, 350))
        screen.blit(lower_img, (418, 350))
        screen.blit(coins_two_img, (748, 350))

        text = shop_1.render(f'{lower_number}', True, (green))
        screen.blit(text, (433, 410))

        text = shop_1.render(f'{hui_fu_number}', True, (green))
        screen.blit(text, (543, 410))

        text = shop_1.render(f'{su_du_number}', True, (green))
        screen.blit(text, (653, 410))

        text = shop_1.render(f'{coins_two_number}', True, (green))
        screen.blit(text, (753, 410))

        text = a_00.render('开始闯关', True, (green))
        screen.blit(text, (580, 530))

        if tips == True:
            text = shop_1.render('空格', True, (green))
            screen.blit(text, (725, 510))

            text = shop_1.render('1.', True, (green))
            screen.blit(text, (428, 320))

            text = shop_1.render('2.', True, (green))
            screen.blit(text, (538, 320))

            text = shop_1.render('3.', True, (green))
            screen.blit(text, (648, 320))

            text = shop_1.render('4.', True, (green))
            screen.blit(text, (748, 320))

        if level_1 == True:
            level_number = '一'
        elif level_2 == True:
            level_number = '二'
        elif level_3 == True:
            level_number = '三'
        elif level_4 == True:
            level_number = '四'
        elif level_5 == True:
            level_number = '五'

        text = upgrade.render(f'第{level_number}关', True, (red))
        screen.blit(text, (340, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    dianji.play()
                    hui_fu_ci_shu = 0
                    su_du_ci_shu = 0
                    lower_ci_shu = 0
                    play_game_2()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    level_false()
                    ok_false()
                    hui_fu_ci_shu = 0
                    su_du_ci_shu = 0
                    lower_ci_shu = 0
                    save()
                    level()

                elif event.key == ord('r'):
                    dianji.play()
                    level_false()
                    ok_false()
                    hp = hp_00
                    hp_3 = hp_00
                    player_speed = player_speed_00
                    player_speed_4 = player_speed_00
                    hui_fu_ci_shu = 0
                    su_du_ci_shu = 0
                    lower_ci_shu = 0
                    save()
                    level_select()

                elif event.key == K_1:
                    dianji.play()
                    if lower_ci_shu >= 1:
                        lower_ci_shu = 1
                        xianzhi()

                    lower_number -= 1
                    if lower_number < 1:
                        lower_number = 0
                        continue

                    else:
                        if dao_ju_lower_level == 1:
                            for e in dicis:
                                e.dici_speed -= 0.5

                            for e in dicis_2:
                                e.dici_2_speed -= 0.5

                            for e in dicis_3:
                                e.dici_3_speed -= 0.5
                            lower_ci_shu += 1

                        elif dao_ju_lower_level == 2:
                            for e in dicis:
                                e.dici_speed -= 1

                            for e in dicis_2:
                                e.dici_2_speed -= 1

                            for e in dicis_3:
                                e.dici_3_speed -= 1
                            lower_ci_shu += 1

                        elif dao_ju_lower_level == 3 or dao_ju_lower_level == 4:
                            for e in dicis:
                                e.dici_speed -= 1.5

                            for e in dicis_2:
                                e.dici_2_speed -= 1.5

                            for e in dicis_3:
                                e.dici_3_speed -= 1.5
                            lower_ci_shu += 1



                elif event.key == K_2:
                    dianji.play()
                    if hui_fu_ci_shu >= 3:
                        hui_fu_ci_shu = 3
                        xianzhi()

                    hui_fu_number -= 1
                    if hui_fu_number < 1:
                        hui_fu_number = 0
                        continue

                    else:
                        hp_00 = hp
                        hp_3 += hp_zeng_jia
                        hui_fu_ci_shu += 1



                elif event.key == K_3:
                    dianji.play()
                    if su_du_ci_shu >= 3:
                        su_du_ci_shu = 3
                        xianzhi()

                    su_du_number -= 1
                    if su_du_number < 1:
                        su_du_number = 0
                        continue

                    else:
                        player_speed_00 = player_speed
                        player_speed_4 += su_du_zeng_jia
                        su_du_ci_shu += 1

                elif event.key == K_4:
                    dianji.play()
                    if coins_two_ci_shu >= 1:
                        su_du_ci_shu = 1
                        xianzhi()

                    coins_two_number -= 1
                    if coins_two_number < 1:
                        coins_two_number = 0
                        continue

                    else:
                        coins_two = True
                        coins_two_ci_shu += 1

        pygame.display.update()



def dao_ju_zeng_jia():
    global su_du_zeng_jia, hp_zeng_jia, lower_jian_shao, hui_fu_coins, su_du_coins, lower_coins
    if dao_ju_su_du_level == 1:
        su_du_zeng_jia = 1

    elif dao_ju_su_du_level == 2:
        su_du_zeng_jia = 2
        su_du_coins = 56

    elif dao_ju_su_du_level == 3 or dao_ju_su_du_level == 4:
        su_du_zeng_jia = 3
        su_du_coins = 64



    if dao_ju_hp_level == 1:
        hp_zeng_jia = 1

    elif dao_ju_hp_level == 2:
        hp_zeng_jia = 2
        hui_fu_coins = 56

    elif dao_ju_hp_level == 3 or dao_ju_hp_level == 4:
        hp_zeng_jia = 3
        hui_fu_coins = 64



    if dao_ju_lower_level == 1:
        lower_jian_shao = 0.5

    elif dao_ju_lower_level == 2:
        lower_jian_shao = 1
        lower_coins = 56

    elif dao_ju_lower_level == 3 or dao_ju_lower_level == 4:
        lower_jian_shao = 1.5
        lower_coins = 64



def xianzhi():
    while True:
        text = fps_00.render('一关中一种道具只能用三次！', True, (black))
        screen.blit(text, (0, 420))

        text = fps_00.render('敌人速度减少只能用1次！￣へ￣', True, (black))
        screen.blit(text, (0, 470))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    home_page()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    home_page()

        clock.tick(0.6)
        xing_xi()



def play_game_2():
    global level_1, level_number, level_tips_2
    clock.tick(12)
    if level_1 == True:
        level_number = '一'
        level_tips_2 = '小心尖锐物！它们会让你的飞机遍体鳞伤！'

    elif level_2 == True:
        level_number = '二'
        level_tips_2 = '那些长块使你更加难躲避！不要碰到它们！'

    elif level_3 == True:
        level_number = '三'
        level_tips_2 = '小心！它们加快了它们的速度！快点躲避！'

    elif level_4 == True:
        level_number = '四'
        level_tips_2 = '速战速决不行，它们又打算围剿，躲好吧！'

    elif level_5 == True:
        level_number = '五'
        level_tips_2 = '小心那些失控的设备！它们会乱发射激光！'

    screen.blit(bg_img, (0, 0))
    text = level_look_00.render(f'第{level_number}关', True, (red))
    screen.blit(text, (170, 50))

    text = exit_game.render(f'{level_tips_2}', True, (red))
    screen.blit(text, (25, 240))

    pygame.display.update()
    clock.tick(0.3)
    screen.blit(bg_img, (0, 0))
    donut.level_donut()


class donut():
    def ord_n():
        text = cheng_jiu_1a.render('按下N键以继续', True, (green))
        screen.blit(text, (635, 565))

    def level_donut():
        global level_1_donut, level_2_donut, level_3_donut, level_4_donut, level_5_donut
        if donut_open == 3:
            level_start()
        elif (level_1 == True and level_1_donut == False and donut_open == 1) or donut_open == 2:
            level_1_donut = True
            screen.blit(bg_img, (0, 0))
            screen.blit(player_img, (360, 478))
            text = upgrade.render('美好的一天从工作开始！U•ェ•*U', True, (green))
            screen.blit(text, (150, 320))
            if tips == True:
               donut.ord_n()
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        dianji.play()
                        save()
                        quit_game()

                    elif event.type == KEYDOWN:
                        if event.key == ord('r'):
                            dianji.play()
                            save()
                            level_start()

                        elif event.key == K_ESCAPE:
                            dianji.play()
                            save()
                            level_start()
                        elif event.key == ord('n'):
                            dianji.play()
                            save()
                            level_start()

        elif (level_2 == True and level_2_donut == False and donut_open == 1) or donut_open == 2:
            level_2_donut = True
            screen.blit(bg_img, (0, 0))
            screen.blit(player_img, (360, 478))
            text = upgrade.render('果然还是宅在家里面安全(T_T)', True, (green))
            screen.blit(text, (150, 320))
            if tips == True:
                donut.ord_n()
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        dianji.play()
                        save()
                        quit_game()

                    elif event.type == KEYDOWN:
                        if event.key == ord('r'):
                            dianji.play()
                            save()
                            level_start()

                        elif event.key == K_ESCAPE:
                            dianji.play()
                            save()
                            level_start()
                        elif event.key == ord('n'):
                            dianji.play()
                            save()
                            level_start()

        elif (level_3 == True and level_3_donut == False and donut_open == 1) or donut_open == 2:
            level_3_donut = True
            screen.blit(bg_img, (0, 0))
            screen.blit(player_img, (360, 478))
            text = upgrade.render('要不请个假别，好危险啊…(⊙_⊙;)…', True, (green))
            screen.blit(text, (150, 320))
            if tips == True:
                donut.ord_n()
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        dianji.play()
                        save()
                        quit_game()

                    elif event.type == KEYDOWN:
                        if event.key == ord('r'):
                            dianji.play()
                            save()
                            level_start()

                        elif event.key == K_ESCAPE:
                            dianji.play()
                            save()
                            level_start()
                        elif event.key == ord('n'):
                            dianji.play()
                            save()
                            level_start()

        elif (level_4 == True and level_4_donut == False and donut_open == 1) or donut_open == 2:
            level_4_donut = True
            screen.blit(bg_img, (0, 0))
            screen.blit(player_img, (360, 478))
            text = upgrade.render('快到了快到了！加油！（好不容易才到这的，就别回去了吧）', True, (green))
            screen.blit(text, (0, 320))
            text = upgrade.render('╮（╯＿╰）╭', True, (green))
            screen.blit(text, (300, 350))
            if tips == True:
                donut.ord_n()
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        dianji.play()
                        save()
                        quit_game()

                    elif event.type == KEYDOWN:
                        if event.key == ord('r'):
                            dianji.play()
                            save()
                            level_start()

                        elif event.key == K_ESCAPE:
                            dianji.play()
                            save()
                            level_start()
                        elif event.key == ord('n'):
                            dianji.play()
                            save()
                            level_start()

        elif (level_5 == True and level_5_donut == False and donut_open == 1) or donut_open == 2:
            level_5_donut = True
            screen.blit(bg_img, (0, 0))
            screen.blit(player_img, (360, 478))
            text = upgrade.render('总算过来了，那些太空垃圾飞的真快(￣﹏￣；)', True, (green))
            screen.blit(text, (50, 320))
            if tips == True:
                donut.ord_n()
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        dianji.play()
                        save()
                        quit_game()

                    elif event.type == KEYDOWN:
                        if event.key == ord('r'):
                            dianji.play()
                            save()
                            level_start()

                        elif event.key == K_ESCAPE:
                            dianji.play()
                            save()
                            level_start()
                        elif event.key == ord('n'):
                            dianji.play()
                            save()
                            level_start()

        else:
            level_start()
            
    def block_open_donut():
        global cheng_jiu_donut, shop_donut, upgrade_donut, tong_ji_donut, dui_huan_donut
        if cheng_jiu_donut == True:
            cheng_jiu_donut = False
            screen.fill(white)
            text = upgrade.render('你定下了一个个目标，并期望通过完成来磨练自己', True, (green))
            screen.blit(text, (50, 220))
            text = upgrade.render('然后就变成了成就室……hhh', True, (green))
            screen.blit(text, (150, 250))
            if tips == True:
                donut.ord_n()
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        dianji.play()
                        save()
                        quit_game()

                    elif event.type == KEYDOWN:
                        if event.key == ord('r'):
                            dianji.play()
                            save()
                            cheng_jiu()
                        elif event.key == K_ESCAPE:
                            dianji.play()
                            save()
                            cheng_jiu()
                        elif event.key == ord('n'):
                            dianji.play()
                            save()
                            cheng_jiu()
            
        elif shop_donut == True:
            shop_donut = False
            screen.fill(white)
            text = upgrade.render('听说附近有个商店呢！说不定有好东西，去看看吧', True, (green))
            screen.blit(text, (50, 220))
            text = upgrade.render('要开始花钱了，你的钱包还行不（直击心灵的问题）', True, (green))
            screen.blit(text, (50, 250))
            if coins < 48:
                text = upgrade.render('你望了望自己干瘪瘪的钱包', True, (green))
                screen.blit(text, (180, 300))
            elif coins >= 100:
                text = upgrade.render('你望了望自己气鼓鼓的钱包', True, (green))
                screen.blit(text, (180, 300))
            if tips == True:
                donut.ord_n()
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        dianji.play()
                        save()
                        quit_game()

                    elif event.type == KEYDOWN:
                        if event.key == ord('r'):
                            dianji.play()
                            save()
                            game_shop()
                        elif event.key == K_ESCAPE:
                            dianji.play()
                            save()
                            game_shop()
                        elif event.key == ord('n'):
                            dianji.play()
                            save()
                            game_shop()
            
        elif upgrade_donut == True:
            upgrade_donut = False
            screen.fill(white)
            text = upgrade.render('是时候把这部飞机改造一下了！<(￣︶￣)↗[GO!]', True, (green))
            screen.blit(text, (50, 220))
            text = upgrade.render('钱包：我无所畏惧╰（‵□′）╯', True, (green))
            screen.blit(text, (130, 250))
            if tips == True:
                donut.ord_n()
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        dianji.play()
                        save()
                        quit_game()

                    elif event.type == KEYDOWN:
                        if event.key == ord('r'):
                            dianji.play()
                            save()
                            upgrade_player()
                        elif event.key == K_ESCAPE:
                            dianji.play()
                            save()
                            upgrade_player()
                        elif event.key == ord('n'):
                            dianji.play()
                            save()
                            upgrade_player()
            
        elif tong_ji_donut == True:
            tong_ji_donut = False
            screen.fill(white)
            text = upgrade.render('你的光荣历程在这被记载的仔仔细细', True, (green))
            screen.blit(text, (130, 220))
            if die_number > 6:
                text = upgrade.render('玩游戏嘛快乐就行~', True, (green))
                screen.blit(text, (150, 250))
            elif starts >= 4 and die_number < 6:
                text = upgrade.render('我的辉煌战绩真好看', True, (green))
                screen.blit(text, (150, 250))
            else:
                text = upgrade.render('看吧看吧~（平平常常啦）', True, (green))
                screen.blit(text, (170, 250))
            if tips == True:
                donut.ord_n()
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        dianji.play()
                        save()
                        quit_game()

                    elif event.type == KEYDOWN:
                        if event.key == ord('r'):
                            dianji.play()
                            save()
                            tong_ji_1()
                        elif event.key == K_ESCAPE:
                            dianji.play()
                            save()
                            tong_ji_1()
                        elif event.key == ord('n'):
                            dianji.play()
                            save()
                            tong_ji_1()

        elif dui_huan_donut == True:
            dui_huan_donut = False
            screen.fill(white)
            text = upgrade.render('众所周知成就和技术能当饭吃(￣y▽,￣)╭ ', True, (green))
            screen.blit(text, (90, 220))
            if tips == True:
                donut.ord_n()
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        dianji.play()
                        save()
                        quit_game()

                    elif event.type == KEYDOWN:
                        if event.key == ord('r'):
                            dianji.play()
                            save()
                            coins_dui_huan()
                        elif event.key == K_ESCAPE:
                            dianji.play()
                            save()
                            coins_dui_huan()
                        elif event.key == ord('n'):
                            dianji.play()
                            save()
                            coins_dui_huan()

    def first_donut():
        pass
    def wins_donut():
        pass
    def overs_donut():
        pass



class dici():
    def __init__(self):
        self.dici_img = pygame.image.load('图片\地刺.png')
        self.dici_Y = 0
        self.dici_X = random.randint(0, 744)
        self.dici_speed = 3

    def restet(self):
        self.dici_X = random.randint(0, 744)
        self.dici_Y = 0

dicis = []

class dici_2():
    def __init__(self):
        self.dici_2_img = pygame.image.load('图片\长块.png')
        self.dici_2_Y = 0
        self.dici_2_X = random.randint(0, 744)
        self.dici_2_speed = 2

    def restet_2(self):
        self.dici_2_Y = 0
        self.dici_2_X = random.randint(0, 744)

dicis_2 = []

class dici_3():
    def __init__(self):
        self.dici_3_img = pygame.image.load('图片\激光.png')
        self.dici_3_Y = 0
        self.dici_3_X = 0
        self.dici_3_speed = 3

    def restet_3(self):
        self.dici_3_Y = 0
        a = random.randint(0, 1)
        self.dici_3_X = 0

dicis_3 = []

class bullet():
    def __init__(self):
        self.dici_3_bullet_img = pygame.image.load('图片\激光攻击.png')
        for e in dicis_3:
            self.dici_3_bullet_X = (e.dici_3_X + 25)
            self.dici_3_bullet_Y = (e.dici_3_Y + 26)
        self.dici_3_bullet_speed = 3

    def bullet_restet(self):
        for e in dicis_3:
            self.dici_3_bullet_X = (e.dici_3_X + 25)
            self.dici_3_bullet_Y = (e.dici_3_Y + 26)
            e.dici_3_Y = e.dici_3_Y
            e.dici_3_X = e.dici_3_X

bullets = []



def hurt(px, py, ex, ey):
    a = px - ex
    b = py - ey
    return sqrt(a*a + b*b)



def first_open_game_tips():
    global player_Y, c, first_open_game
    while True:
        clock.tick(32)
        screen.blit(bg_img, (0, 0))
        screen.blit(player_img, (player_X, player_Y))
        if player_Y <= 478 and c == False:
            if player_Y <= 239:
                c = True
            player_Y -= 2

        elif c == True:
            if player_Y >= 478:
                player_Y = 478
                first_open_game = True
                home_page()
            player_Y += 2

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    quit_game()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    quit_game()

        pygame.display.update()



def open_block():
    aaa = False
    global first_cheng_jiu_open, first_shop_open, first_upgrade_open, first_tong_ji_open, first_dui_huan_open, open_block_ok, cheng_jiu_open, shop_open, upgrade_open, tong_ji_open, dui_huan_open, ticks, number
    ticks = 0
    if tong_guan_1 == True and cheng_jiu_cishu_1 == True:
        cheng_jiu_open = True
    if tong_guan_2 == True:
        shop_open = True
    if tong_guan_3 == True:
        upgrade_open = True
    if tong_guan_4 == True:
        tong_ji_open = True
    if tong_guan_5 == True:
        dui_huan_open = True
    if cheng_jiu_1_coins >= 7 or starts >= 7:
        dui_huan_open = True
    while True:
        clock.tick(5)
        ticks += 1
        if cheng_jiu_open == True and first_cheng_jiu_open == False:
            screen.blit(bg_img_2, (0, 0))
            text = score_look.render('成就模块解锁！', True, (green))
            screen.blit(text, (280, 230))
            text = cheng_jiu_1a.render('主页中按下A进入', True, (green))
            screen.blit(text, (320, 280))
            text = score_look.render('★', True, (yellow))
            screen.blit(text, (560, 180))
            first_cheng_jiu_open = True
            open_block_ok = True
            aaa = True
            sleep(1.5)

        elif shop_open == True and first_shop_open == False:
            screen.blit(bg_img_2, (0, 0))
            text = score_look.render('商店模块解锁！', True, (green))
            screen.blit(text, (280, 230))
            text = cheng_jiu_1a.render('主页中按下S进入', True, (green))
            screen.blit(text, (320, 280))
            screen.blit(hui_fu_img, (560, 210))
            screen.blit(su_du_img, (240, 320))
            screen.blit(lower_img, (200, 120))
            screen.blit(coins_two_img, (560, 380))
            first_shop_open = True
            open_block_ok = True
            aaa = True
            sleep(1.5)

        elif upgrade_open == True and first_upgrade_open == False:
            screen.blit(bg_img_2, (0, 0))
            text = score_look.render('升级模块解锁！', True, (green))
            screen.blit(text, (280, 230))
            text = cheng_jiu_1a.render('主页中按下U进入', True, (green))
            screen.blit(text, (320, 280))
            if ticks % 12 < 6:
                screen.blit(player_img, (560 , 350))
            else:
                screen.blit(player_img_2, (560 , 350))
            first_upgrade_open = True
            open_block_ok = True
            aaa = True
            sleep(1.5)

        elif tong_ji_open == True and first_tong_ji_open == False:
            screen.blit(bg_img_2, (0, 0))
            text = score_look.render('统计模块解锁！', True, (green))
            screen.blit(text, (280, 230))
            text = cheng_jiu_1a.render('主页中按下T进入', True, (green))
            screen.blit(text, (320, 280))
            text = score_look.render('★', True, (yellow))
            screen.blit(text, (420, 300))
            text = score_look.render('★', True, (blue))
            screen.blit(text, (530, 120))
            screen.blit(coins_img, (600, 230))
            first_tong_ji_open = True
            open_block_ok = True
            aaa = True
            sleep(1.5)

        elif dui_huan_open == True and first_dui_huan_open == False:
            screen.blit(bg_img_2, (0, 0))
            text = score_look.render('兑换模块解锁！', True, (green))
            screen.blit(text, (280, 230))
            text = cheng_jiu_1a.render('主页中按下H进入', True, (green))
            screen.blit(text, (320, 280))
            text = score_look.render('★', True, (yellow))
            screen.blit(text, (400, 120))
            text = score_look.render('★', True, (blue))
            screen.blit(text, (430, 410))
            screen.blit(coins_img, (230, 210))
            first_dui_huan_open = True
            open_block_ok = True
            aaa = True
            sleep(1.5)

        elif (cheng_jiu_open == True and first_cheng_jiu_open == True and aaa == False) or (cheng_jiu_open == False and first_cheng_jiu_open == False and aaa == False) or(shop_open == True and first_shop_open == True and aaa == False) or (shop_open == False and first_shop_open == False and aaa == False) or (upgrade_open == True and first_upgrade_open == True and aaa == False) or (upgrade_open == False and first_upgrade_open == False and aaa == False) or (tong_ji_open == True and first_tong_ji_open == True and aaa == False) or (tong_ji_open == False and first_tong_ji_open == False and aaa == False) or (dui_huan_open == True and first_dui_huan_open == True and aaa == False) or (dui_huan_open == False and first_dui_huan_open == False and aaa == False):
            open_block_ok = True
            home_page()

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == ord('r'):
                    dianji.play()
                    save()
                    home_page()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    home_page()

        pygame.display.update()



def home_page():
    global home, ticks, open_block_ok
    ticks = 0
    if first_open_game == False:
        first_open_game_tips()
    cheng_jiu_0()
    cheng_jiu_pan_duan()
    if open_block_ok == False:
        open_block()
    else:
        open_block_ok = False
    while True:
        ticks += 1
        clock.tick(5)
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == QUIT:
                dianji.play()
                save()
                quit_game()

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    dianji.play()
                    save()
                    level()

                elif event.key == ord('r'):
                    dianji.play()
                    save()
                    quit_game()

                elif event.key == K_ESCAPE:
                    dianji.play()
                    save()
                    quit_game()

                elif event.key == ord('o'):
                    dianji.play()
                    save()
                    set_o()

                if cheng_jiu_open == True:
                    if event.key == ord('a'):
                        dianji.play()
                        save()
                        cheng_jiu()

                if shop_open == True:
                    if event.key == ord('s'):
                        dianji.play()
                        save()
                        game_shop()

                if upgrade_open == True:
                    if event.key == ord('u'):
                        dianji.play()
                        save()
                        upgrade_player()

                if tong_ji_open == True:
                    if event.key == ord('t'):
                            dianji.play()
                            save()
                            tong_ji_1()

                if dui_huan_open == True:
                    if event.key == ord('h'):
                        dianji.play()
                        home = True
                        save()
                        coins_dui_huan()

        if save_name_true == True:
            if len(name) >= 5:
                text = a.render(f'{name}', True, (black))
                screen.blit(text, (340, 0))

            elif len(name) == 2:
                text = a.render(f'{name}', True, (black))
                screen.blit(text, (350, 0))

            else:
                text = a.render(f'{name}', True, (black))
                screen.blit(text, (360, 0))

        text = title.render('回避', True, (black))
        screen.blit(text, (280, 60))

        text = start.render('开始游戏', True, (black))
        screen.blit(text, (298, 200))

        if upgrade_open == True:
            if ticks % 12 < 6:
                screen.blit(player_img, (580 , 230))
            else:
                screen.blit(player_img_2, (580 , 230))
            text = upgrade.render('升级', True, (black))
            screen.blit(text, (595, 340))

        if shop_open == True:
            text = start.render('游戏商店', True, (black))
            screen.blit(text, (298, 260))

        if cheng_jiu_open == True:
            text = start.render('成就', True, (black))
            screen.blit(text, (330, 500))

        if tong_ji_open == True:
            text = coins_look.render('统计==》', True, (black))
            screen.blit(text, (690, 30))

        if dui_huan_open == True:
            text = coins_look.render('兑换==》', True, (black))
            screen.blit(text, (690, 60))

        text = exit_game.render('退出游戏', True, (black))
        screen.blit(text, (298, 320))


        text = coins_look.render('设置==》', True, (black))
        screen.blit(text, (690, 0))
        screen.blit(coins_img, (0, 0))
        text = a.render(f'{coins}', True, (black))
        screen.blit(text, (32, 0))

        text = tips_game.render('健康游戏忠告：', True, (black))
        screen.blit(text, (0, 500))
        text = tips_game.render('抵制不良游戏，拒绝盗版游戏。', True, (black))
        screen.blit(text, (0, 520))
        text = tips_game.render('注意自我保护，谨防上当受骗。', True, (black))
        screen.blit(text, (0, 540))
        text = tips_game.render('适度游戏益脑，沉迷游戏伤身。', True, (black))
        screen.blit(text, (0, 560))
        text = tips_game.render('合理安排时间，享受健康生活。', True, (black))
        screen.blit(text, (0, 580))

        if tips == True:
            text = coins_look.render('空格', True, (green))
            screen.blit(text, (355, 178))

            if shop_open == True:
                text = shop_1.render('S', True, (green))
                screen.blit(text, (375, 245))

            if upgrade_open == True:
                text = shop_1.render('U', True, (green))
                screen.blit(text, (618, 320))

            if cheng_jiu_open == True:
                text = shop_1.render('A', True, (green))
                screen.blit(text, (360, 490))

            if tong_ji_open == True:
                text = shop_1.render('T.', True, (green))
                screen.blit(text, (670, 30))

            if dui_huan_open == True:
                text = shop_1.render('H.', True, (green))
                screen.blit(text, (667, 60))

            text = shop_1.render('R', True, (green))
            screen.blit(text, (375, 300))

            text = shop_1.render('O.', True, (green))
            screen.blit(text, (667, 0))

        pygame.display.update()

home_page()
