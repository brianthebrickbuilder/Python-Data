'''
Name:           main.py
Author:         Brian Richardson
Version:        1.0
Date:           June 20, 2021
Description:    This is the main file for Lab 05
'''
import functions

MENU_EXIT = False

while MENU_EXIT is False:
    MENU_EXIT = functions.menu()

functions.menu_exit()
