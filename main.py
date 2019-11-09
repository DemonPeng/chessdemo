import pygame
import sys
import traceback
import copy

from chessboard import Draw

pygame.font.init()
pygame.init()


def main():
    # 定义两个存储棋子现在的状态
    backups1 = []
    backups2 = []

    # 创建一个窗口
    screen = pygame.display.set_mode([1200, 900])
    # 设置窗口标题
    pygame.display.set_caption("中国象棋")
    # 在窗口画出棋盘以及按钮
    Draw.draw_a_chessboard(screen)
    clock = pygame.time.Clock()

    while True:
        Draw.draw_a_chessboard_with_chessman(map, screen)
        pygame.display.flip()
        # 监听所有事件
        for event in pygame.event.get():
            # 点击x则关闭窗口
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    # 鼠标第一次按下选择棋子
                    if running:
                        x, y = event.pos[0], event.pos[1]
                        for key in hongqi.keys():
                            if sqrt((hongqi[key]['now_weizhi'][0] - x) ** 2 + (
                                    hongqi[key]['now_weizhi'][1] - y) ** 2) < r:
                                backups1 = [key, hongqi[key]]
                        for key in heiqi.keys():
                            if sqrt((heiqi[key]['now_weizhi'][0] - x) ** 2 + (
                                    heiqi[key]['now_weizhi'][1] - y) ** 2) < r:
                                backups2 = [key, heiqi[key]]
                        if backups1:
                            # 用于暂存棋子状态
                            backups3 = copy.deepcopy(backups1)
                            hongqi.pop(backups1[0])
                            running = not running
                        elif backups2:
                            # 用于暂存棋子状态
                            backups4 = copy.deepcopy(backups2)
                            heiqi.pop(backups2[0])
                            running = not running
                    # 鼠标再次按下，落下棋子
                    else:
                        if r < event.pos[0] < 900 + r and r < event.pos[1] < 810 + r:
                            x = (event.pos[0] + r) // 90 * 90
                            y = (event.pos[1] + r) // 90 * 90

                            if backups1:  # 红棋
                                # 判断所走位置是否有棋子
                                if weizhi_panduan(x, y):
                                    hongqi[backups3[0]] = backups3[1]
                                else:
                                    hongqi[backups1[0]] = backups1[1]
                                    hongqi[backups1[0]]['now_weizhi'] = [x, y]

                                backups1 = []
                                running = not running
                            elif backups2:  # 黑棋
                                if weizhi_panduan(x, y):
                                    heiqi[backups4[0]] = backups4[1]
                                else:
                                    heiqi[backups2[0]] = backups2[1]
                                    heiqi[backups2[0]]['now_weizhi'] = [x, y]
                                backups2 = []
                                running = not running
                        else:
                            if backups1:
                                hongqi[backups1[0]] = backups3[1]
                                backups1 = []
                                running = not running
                            elif backups2:
                                heiqi[backups2[0]] = backups4[1]
                                backups2 = []
                                running = not running


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
