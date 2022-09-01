# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: mouse_run_bianxing.py
# author: ScCcWe
# time: 2022/8/31 19:47
import random
import pyautogui

middle_x = 900
middle_y = 500


# --------------------------------------- x
# |point(0, 0)
# |
# |
# |
# |             (900, 500)        (1000, 500)
# |
# |
# |                       (1200, 900)
# y
#
def mouse_and_click_go_like_a_rect():
    """
    往右移动，x值变大即可
    往下移动，y值变大即可
    :return:
    """
    while True:
        jibianxing = random.randint(4, 6) - 2

        # ------------------------step1 初始移动 - 把鼠标个移动到正确的位置(右上角)---------------------------------
        start_x = middle_x + random.randint(200, 400)
        start_y = middle_y - random.randint(100, 230)
        pyautogui.moveTo(start_x, start_y, get_random_from_half_to_one())
        pyautogui.click(clicks=1, button='left', duration=get_random_from_half_to_one())  # 点击进入单据

        if jibianxing == 2:
            # step3 x小增，y大增
            pyautogui.moveTo(middle_x + random.randint(300, 500), middle_y + random.randint(300, 500), get_random_from_half_to_one())
            pyautogui.click(clicks=1, button='left', duration=get_random_from_half_to_one())  # 点击进入单据

            # step4 x大减，y小变
            pyautogui.moveTo(middle_x - random.randint(300, 500), middle_y + random.randint(50, 100), get_random_from_half_to_one())
            pyautogui.click(clicks=1, button='left', duration=get_random_from_half_to_one())  # 点击进入单据

        if jibianxing == 3:
            # step3 x小增，y大增
            pyautogui.moveTo(middle_x + random.randint(300, 500), middle_y + random.randint(300, 500), get_random_from_half_to_one())
            pyautogui.click(clicks=1, button='left', duration=get_random_from_half_to_one())  # 点击进入单据

            # 少减少一点就可以了
            pyautogui.moveTo(middle_x - random.randint(100, 200), middle_y + random.randint(100, 200), get_random_from_half_to_one())
            pyautogui.click(clicks=1, button='left', duration=get_random_from_half_to_one())  # 点击进入单据

            # step4 x大减，y小变
            pyautogui.moveTo(middle_x - random.randint(300, 500), middle_y + random.randint(50, 100), get_random_from_half_to_one())
            pyautogui.click(clicks=1, button='left', duration=get_random_from_half_to_one())  # 点击进入单据

        if jibianxing == 4:
            # step2 x值大于上下，y值在之间
            pyautogui.moveTo(middle_x + random.randint(500, 550), start_y + random.randint(100, 230), get_random_from_half_to_one())
            pyautogui.click(clicks=1, button='left', duration=get_random_from_half_to_one())  # 点击进入单据

            # step3 x小增，y大增
            pyautogui.moveTo(middle_x + random.randint(300, 500), middle_y + random.randint(300, 500), get_random_from_half_to_one())
            pyautogui.click(clicks=1, button='left', duration=get_random_from_half_to_one())  # 点击进入单据

            # 少减少一点就可以了
            pyautogui.moveTo(middle_x - random.randint(100, 200), middle_y + random.randint(100, 200), get_random_from_half_to_one())
            pyautogui.click(clicks=1, button='left', duration=get_random_from_half_to_one())  # 点击进入单据

            # step4 x大减，y小变
            pyautogui.moveTo(middle_x - random.randint(300, 500), middle_y + random.randint(50, 100), get_random_from_half_to_one())
            pyautogui.click(clicks=1, button='left', duration=get_random_from_half_to_one())  # 点击进入单据

        # step5 --------------------------结尾移动到初始点-----------------------------------------------------
        pyautogui.moveTo(start_x, start_y, get_random_from_half_to_one())
        pyautogui.click(clicks=1, button='left', duration=get_random_from_half_to_one())  # 点击进入单据


def get_a_suitable_middle_point(x, y):
    pyautogui.moveTo(x, y, get_random_from_half_to_one())


def get_random_from_half_to_one():
    return round(random.uniform(0.5, 1), 1)


if __name__ == '__main__':
    # get_a_suitable_middle_point(900, 500)
    mouse_and_click_go_like_a_rect()
