import pygame
import sys
import traceback
from math import sqrt
import copy
from pygame.locals import *

pygame.font.init()
pygame.init()

red_chess = {'帅': {'color': 'red', 'coor': (4, 9)}, '仕1': {'color': 'red', 'coor': (3, 9)},
             '仕2': {'color': 'red', 'coor': (5, 9)}, '相1': {'color': 'red', 'coor': (2, 9)},
             '相2': {'color': 'red', 'coor': (6, 9)}, '馬1': {'color': 'red', 'coor': (1, 9)},
             '馬2': {'color': 'red', 'coor': (7, 9)}, '車1': {'color': 'red', 'coor': (0, 9)},
             '車2': {'color': 'red', 'coor': (8, 9)}, '炮1': {'color': 'red', 'coor': (1, 7)},
             '炮2': {'color': 'red', 'coor': (7, 7)}, '兵1': {'color': 'red', 'coor': (0, 6)},
             '兵2': {'color': 'red', 'coor': (2, 6)}, '兵3': {'color': 'red', 'coor': (4, 6)},
             '兵4': {'color': 'red', 'coor': (6, 6)}, '兵5': {'color': 'red', 'coor': (8, 6)}
             }
black_chess = {'将': {'color': 'black', 'coor': (4, 0)}, '士1': {'color': 'black', 'coor': (3, 0)},
               '士2': {'color': 'black', 'coor': (5, 0)}, '象1': {'color': 'black', 'coor': (2, 0)},
               '象2': {'color': 'black', 'coor': (6, 0)}, '馬1': {'color': 'black', 'coor': (1, 0)},
               '馬2': {'color': 'black', 'coor': (7, 0)}, '車1': {'color': 'black', 'coor': (0, 0)},
               '車2': {'color': 'black', 'coor': (8, 0)}, '炮1': {'color': 'black', 'coor': (1, 2)},
               '炮2': {'color': 'black', 'coor': (7, 2)}, '卒1': {'color': 'black', 'coor': (0, 3)},
               '卒2': {'color': 'black', 'coor': (2, 3)}, '卒3': {'color': 'black', 'coor': (4, 3)},
               '卒4': {'color': 'black', 'coor': (6, 3)}, '卒5': {'color': 'black', 'coor': (8, 3)}
               }


def draw_chessboard(screen):
    backgroud_color = (233, 204, 138)
    screen.fill(backgroud_color)
    outer_frame_color = (60, 20, 0)
    pygame.draw.rect(screen, outer_frame_color, [30, 30, 570, 640], 5)
    inner_frame_color = (0, 0, 0)
    for i in range(10):
        pygame.draw.line(screen, inner_frame_color, (35, 35 + i * 70), (595, 35 + i * 70))
    for i in range(9):
        if i == 0 or i == 8:
            pygame.draw.line(screen, inner_frame_color, (35 + i * 70, 35), (35 + i * 70, 665))
        else:
            pygame.draw.line(screen, inner_frame_color, (35 + i * 70, 35), (35 + i * 70, 315))
            pygame.draw.line(screen, inner_frame_color, (35 + i * 70, 385), (35 + i * 70, 665))
    pygame.draw.line(screen, inner_frame_color, (245, 35), (385, 175))
    pygame.draw.line(screen, inner_frame_color, (245, 175), (385, 35))
    pygame.draw.line(screen, inner_frame_color, (245, 525), (385, 665))
    pygame.draw.line(screen, inner_frame_color, (245, 665), (385, 525))
    rote_color = (255, 0, 0)
    for j in range(0, 2):
        for k in range(0, 4):
            pygame.draw.aalines(screen, rote_color, False,
                                [(155 + 140 * k, 240 + 210 * j), (170 + 140 * k, 240 + 210 * j),
                                 (170 + 140 * k, 225 + 210 * j)], 3)
            pygame.draw.aalines(screen, rote_color, False,
                                [(155 + 140 * k, 250 + 210 * j), (170 + 140 * k, 250 + 210 * j),
                                 (170 + 140 * k, 265 + 210 * j)], 3)
            pygame.draw.aalines(screen, rote_color, False,
                                [(40 + 140 * k, 225 + 210 * j), (40 + 140 * k, 240 + 210 * j),
                                 (55 + 140 * k, 240 + 210 * j)], 3)
            pygame.draw.aalines(screen, rote_color, False,
                                [(40 + 140 * k, 265 + 210 * j), (40 + 140 * k, 250 + 210 * j),
                                 (55 + 140 * k, 250 + 210 * j)], 3)
    for j in range(0, 2):
        for k in range(0, 2):
            pygame.draw.aalines(screen, rote_color, False,
                                [(85 + 420 * k, 170 + 350 * j), (100 + 420 * k, 170 + 350 * j),
                                 (100 + 420 * k, 155 + 350 * j)], 3)
            pygame.draw.aalines(screen, rote_color, False,
                                [(85 + 420 * k, 180 + 350 * j), (100 + 420 * k, 180 + 350 * j),
                                 (100 + 420 * k, 195 + 350 * j)], 3)
            pygame.draw.aalines(screen, rote_color, False,
                                [(110 + 420 * k, 155 + 350 * j), (110 + 420 * k, 170 + 350 * j),
                                 (125 + 420 * k, 170 + 350 * j)], 3)
            pygame.draw.aalines(screen, rote_color, False,
                                [(110 + 420 * k, 195 + 350 * j), (110 + 420 * k, 180 + 350 * j),
                                 (125 + 420 * k, 180 + 350 * j)], 3)
    s_font = pygame.font.Font('方正柳公权楷书(简).ttf', 55)
    line = s_font.render("楚 河           汉 界", True, (163, 80, 21))
    screen.blit(line, (115, 320))
    s1_font = pygame.font.Font('方正手迹-欧蝶正楷(简).ttf', 40)
    text1 = s1_font.render("悔    棋", True, (0, 0, 0))
    text2 = s1_font.render("重新开始", True, (0, 0, 0))
    text3 = s1_font.render("退出游戏", True, (0, 0, 0))
    text1_rect = text1.get_rect()
    text2_rect = text2.get_rect()
    text3_rect = text3.get_rect()
    text1_rect.center = (730, 220)
    text2_rect.center = (730, 300)
    text3_rect.center = (730, 380)
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)


def draw_chessman(screen, color, chessman, coor: tuple):
    red_color = (255, 0, 0)
    black_color = (0, 0, 0)
    coor_exchange = (coor[0] * 70 + 35, coor[1] * 70 + 35)
    man_coor = (coor[0] * 70 + 15, coor[1] * 70 + 13)

    pygame.draw.circle(screen, (0, 0, 0), coor_exchange, 33)
    pygame.draw.circle(screen, (247, 157, 12), coor_exchange, 32)
    pygame.draw.circle(screen, (0, 0, 0), coor_exchange, 28, 3)
    pygame.draw.circle(screen, (181, 131, 16), coor_exchange, 25)

    m_font = pygame.font.Font("方正榜书行(简繁).ttf", 38)
    m_color = ''

    if color == 'red':
        m_color = red_color
    elif color == 'black':
        m_color = black_color
    screen.blit(m_font.render(chessman[0], True, m_color), man_coor)


def draw_board_with_chessman(map, screen):
    draw_chessboard(screen)
    for each_chessman in red_chess.keys():
        draw_chessman(screen, red_chess[each_chessman]['color'], each_chessman, red_chess[each_chessman]['coor'])
    for each_chessman in black_chess.keys():
        draw_chessman(screen, black_chess[each_chessman]['color'], each_chessman,
                      black_chess[each_chessman]['coor'])


def coor_exchange(coor: tuple):
    for i in range(10):
        for j in range(11):
            if sqrt(((i * 70 - 35) - coor[0]) ** 2 + ((j * 70 - 35) - coor[1]) ** 2) <= 25:
                coor = (i - 1, j - 1)
            else:
                pass
    return coor


def judge_coor(coor: tuple):
    coor_all = []
    for key in red_chess.keys():
        coor_all.append(red_chess[key]['coor'])
    for key in black_chess.keys():
        coor_all.append(black_chess[key]['coor'])
    return True if coor in coor_all else False


def move_rules(chessman, color, coor: tuple):
    coor_red, coor_black = [], []
    for key in red_chess.keys():
        coor_red.append(red_chess[key]['coor'])
    for key in black_chess.keys():
        coor_black.append(black_chess[key]['coor'])
    coor_all = coor_red + coor_black

    can_move = []
    (x, y) = coor
    if chessman == '帅':
        t = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for k in t:
            if 3 <= k[0] <= 5 and k[1] >= 7:
                can_move.append(k)
        for k in coor_red:
            if k in can_move:
                can_move.remove(k)
    elif chessman == '将':
        t = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for k in t:
            if 3 <= k[0] <= 5 and k[1] <= 2:
                can_move.append(k)
        for k in coor_black:
            if k in can_move:
                can_move.remove(k)
    elif chessman == '兵':
        if y < 5:
            can_move = [(x + 1, y), (x - 1, y), (x, y - 1)]
        else:
            can_move = [(x, y - 1)]
        for k in coor_red:
            if k in can_move:
                can_move.remove(k)
    elif chessman == '卒':
        if y > 4:
            can_move = [(x + 1, y), (x - 1, y), (x, y + 1)]
        else:
            can_move = [(x, y + 1)]
        for k in coor_black:
            if k in can_move:
                can_move.remove(k)
    elif chessman == '仕':
        t = [(x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]
        for k in t:
            if 3 <= k[0] <= 5 and k[1] >= 7:
                can_move.append(k)
        for k in coor_red:
            if k in can_move:
                can_move.remove(k)
    elif chessman == '士':
        t = [(x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]
        for k in t:
            if 3 <= k[0] <= 5 and k[1] <= 2:
                can_move.append(k)
        for k in coor_black:
            if k in can_move:
                can_move.remove(k)
    elif chessman == '相':
        can_move = [(x + 2, y + 2), (x + 2, y - 2), (x - 2, y + 2), (x - 2, y - 2)]
        if (x + 1, y + 1) in coor_red:
            d = (x + 2, y + 2)
            can_move.remove(d)
        if (x + 1, y - 1) in coor_red:
            d = (x + 2, y - 2)
            can_move.remove(d)
        if (x - 1, y + 1) in coor_red:
            d = (x - 2, y + 2)
            can_move.remove(d)
        if (x - 1, y - 1) in coor_red:
            d = (x - 2, y - 2)
            can_move.remove(d)
        t = []
        for i in can_move:
            if i[1] > 4:
                t.append(i)
        can_move = t
        for k in coor_red:
            if k in can_move:
                can_move.remove(k)
    elif chessman == '象':
        can_move = [(x + 2, y + 2), (x + 2, y - 2), (x - 2, y + 2), (x - 2, y - 2)]
        if (x + 1, y + 1) in coor_black:
            d = (x + 2, y + 2)
            can_move.remove(d)
        if (x + 1, y - 1) in coor_black:
            d = (x + 2, y - 2)
            can_move.remove(d)
        if (x - 1, y + 1) in coor_black:
            d = (x - 2, y + 2)
            can_move.remove(d)
        if (x - 1, y - 1) in coor_black:
            d = (x - 2, y - 2)
            can_move.remove(d)
        t = []
        for i in can_move:
            if i[1] < 5:
                t.append(i)
        can_move = t
        for k in coor_black:
            if k in can_move:
                can_move.remove(k)
    elif chessman == '馬' and color == 'red':
        can_move = [(x - 1, y - 2), (x + 1, y - 2), (x - 1, y + 2), (x + 1, y + 2), (x - 2, y + 1), (x - 2, y - 1),
                    (x + 2, y + 1), (x + 2, y - 1)]
        if (x, y + 1) in coor_red:
            d1, d2 = (x - 1, y + 2), (x + 1, y + 2)
            can_move.remove(d1)
            can_move.remove(d2)
        if (x, y - 1) in coor_red:
            d1, d2 = (x - 1, y - 2), (x + 1, y - 2)
            can_move.remove(d1)
            can_move.remove(d2)
        if (x + 1, y) in coor_red:
            d1, d2 = (x + 2, y - 1), (x + 2, y + 1)
            can_move.remove(d1)
            can_move.remove(d2)
        if (x - 1, y) in coor_red:
            d1, d2 = (x - 2, y - 1), (x - 2, y + 1)
            can_move.remove(d1)
            can_move.remove(d2)
        for k in coor_red:
            if k in can_move:
                can_move.remove(k)
    elif chessman == '馬' and color == 'black':
        can_move = [(x - 1, y - 2), (x + 1, y - 2), (x - 1, y + 2), (x + 1, y + 2), (x - 2, y + 1), (x - 2, y - 1),
                    (x + 2, y + 1), (x + 2, y - 1)]
        if (x, y + 1) in coor_black:
            d1, d2 = (x - 1, y + 2), (x + 1, y + 2)
            can_move.remove(d1)
            can_move.remove(d2)
        if (x, y - 1) in coor_black:
            d1, d2 = (x - 1, y - 2), (x + 1, y - 2)
            can_move.remove(d1)
            can_move.remove(d2)
        if (x + 1, y) in coor_black:
            d1, d2 = (x + 2, y - 1), (x + 2, y + 1)
            can_move.remove(d1)
            can_move.remove(d2)
        if (x - 1, y) in coor_black:
            d1, d2 = (x - 2, y - 1), (x - 2, y + 1)
            can_move.remove(d1)
            can_move.remove(d2)
        for k in coor_black:
            if k in can_move:
                can_move.remove(k)
    elif chessman == '車' and color == 'red':
        coor_red.remove(coor)
        for i in range(10):
            if (x, y + i) in coor_red:
                break
            if y + i > 9:
                break
            can_move.append((x, y + i))
        for i in range(10):
            if (x, y - i) in coor_red:
                break
            if y - i < 0:
                break
            can_move.append((x, y - i))
        for i in range(10):
            if (x + i, y) in coor_red:
                break
            if x + i > 8:
                break
            can_move.append((x + i, y))
        for i in range(10):
            if (x - i, y) in coor_red:
                break
            if x - i < 0:
                break
            can_move.append((x - i, y))
    elif chessman == '車' and color == 'black':
        coor_black.remove(coor)
        for i in range(10):
            if (x, y + i) in coor_black:
                break
            if y + i > 9:
                break
            can_move.append((x, y + i))
        for i in range(10):
            if (x, y - i) in coor_black:
                break
            if y - i < 0:
                break
            can_move.append((x, y - i))
        for i in range(10):
            if (x + i, y) in coor_black:
                break
            if x + i > 8:
                break
            can_move.append((x + i, y))
        for i in range(10):
            if (x - i, y) in coor_black:
                break
            if x - i < 0:
                break
            can_move.append((x - i, y))
    elif chessman == '炮' and color == 'red':
        coor_red.remove(coor)
        for i in range(10):
            if (x, y + i) in coor_red:
                break
            if y + i > 9:
                break
            can_move.append((x, y + i))
        for i in range(10):
            if (x, y - i) in coor_red:
                break
            if y - i < 0:
                break
            can_move.append((x, y - i))
        for i in range(10):
            if (x + i, y) in coor_red:
                break
            if x + i > 8:
                break
            can_move.append((x + i, y))
        for i in range(10):
            if (x - i, y) in coor_red:
                break
            if x - i < 0:
                break
            can_move.append((x - i, y))
    elif chessman == '炮' and color == 'black':
        coor_black.remove(coor)
        for i in range(10):
            if (x, y + i) in coor_black:
                break
            if y + i > 9:
                break
            can_move.append((x, y + i))
        for i in range(10):
            if (x, y - i) in coor_black:
                break
            if y - i < 0:
                break
            can_move.append((x, y - i))
        for i in range(10):
            if (x + i, y) in coor_black:
                break
            if x + i > 8:
                break
            can_move.append((x + i, y))
        for i in range(10):
            if (x - i, y) in coor_black:
                break
            if x - i < 0:
                break
            can_move.append((x - i, y))

    can_move = list(set(can_move))
    temp = []
    for i in can_move:
        if 0 <= i[0] < 9 and 0 <= i[1] < 10:
            temp.append(i)
    can_move = temp

    return can_move


def is_in_rules(chessman, color, coor:tuple, coor_move):
    can_move = move_rules(chessman, color, coor)
    if coor_move in can_move:
        return True
    else:
        return False


def main():
    # 创建一个窗口
    screen = pygame.display.set_mode([850, 700])
    pygame.display.set_caption("中国象棋")
    draw_chessboard(screen)
    clock = pygame.time.Clock()
    backups1, backups2, backups3, backups4 = [], [], [], []
    running = True
    while True:
        draw_board_with_chessman(map, screen)
        pygame.display.flip()
        # 监听所有事件
        for event in pygame.event.get():
            # 点击x则关闭窗口
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                coor = coor_exchange((event.pos[0], event.pos[1]))
                # print(coor)
                if event.button == 1 and coor[0] < 9 and coor[1] < 10:
                    if running:
                        for key in red_chess.keys():
                            if coor == red_chess[key]['coor']:
                                backups1 = [key, red_chess[key]]
                                # print(move_rules(screen, key[0], red_chess[key]['color'], coor))
                        for key in black_chess.keys():
                            if coor == black_chess[key]['coor']:
                                backups2 = [key, black_chess[key]]
                                # print(move_rules(screen, key[0], black_chess[key]['color'], coor))
                        if backups1:
                            backups3 = copy.deepcopy(backups1)
                            red_chess.pop(backups1[0])
                            running = False
                        elif backups2:
                            backups4 = copy.deepcopy(backups2)
                            black_chess.pop(backups2[0])
                            running = False
                    else:
                        if 25 < event.pos[0] < 620 and 25 < event.pos[1] < 690:
                            coor_up = coor_exchange((event.pos[0], event.pos[1]))
                            # print(coor_up)
                            if backups1:
                                coor_black = []
                                for key in black_chess.keys():
                                    coor_black.append(black_chess[key]['coor'])
                                if is_in_rules(backups1[0], backups1[1]['color'], backups1[1]['coor'], coor_up):
                                    if judge_coor(coor_up):
                                        if coor_up in coor_black:
                                            for key in list(black_chess.keys()):
                                                if black_chess[key]['coor'] == coor_up:
                                                    del black_chess[key]
                                            red_chess[backups1[0]] = backups1[1]
                                            red_chess[backups1[0]]['coor'] = coor_up
                                        else:
                                            red_chess[backups3[0]] = backups3[1]
                                    else:
                                        red_chess[backups1[0]] = backups1[1]
                                        red_chess[backups1[0]]['coor'] = coor_up
                                else:
                                    red_chess[backups3[0]] = backups3[1]
                                backups1 = []
                                running = True
                            elif backups2:
                                if judge_coor(coor_up):
                                    black_chess[backups4[0]] = backups4[1]
                                else:
                                    black_chess[backups2[0]] = backups2[1]
                                    black_chess[backups2[0]]['coor'] = coor_up
                                backups2 = []
                                running = True
                        else:
                            if backups1:
                                red_chess[backups1[0]] = backups3[1]
                                backups1 = []
                                running = True
                            elif backups2:
                                red_chess[backups2[0]] = backups4[1]
                                backups2 = []
                                running = True

                pygame.display.update()


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
