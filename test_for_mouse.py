# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_for_mouse.py
# author: ScCcWe
# time: 2022/8/31 19:47
import random
import pyautogui

while True:
    pyautogui.moveTo(random.randint(700, 800), random.randint(400, 500), duration=0.5)
    pyautogui.click(clicks=1, button='left', duration=1)  # 点击进入单据

    pyautogui.moveTo(random.randint(600, 700), random.randint(400, 500), duration=0.5)
    pyautogui.click(clicks=1, button='left', duration=1)  # 点击进入单据
