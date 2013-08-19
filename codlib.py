#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CodLib v1.28a
# Programmer: Michael Oselskyi & Natan L
#DISCLAIMER: NOT COMPLETE! GUI soon though.
# UPDATE 5/14/13: Added function to search through the sql file.
# Update 8/9/13: Added new-style classes, fixed the Ascii Art.
# Update 8/11/13: Fixed Menus(MAJOR BUG FIX). Fine Tuning.
# Update 8/18/13: Added the logo into a seperate file for space managment. Started work on the csv stuff.

import os
import sys
import functools
import csv


def _print_logo():
    with open('logo.txt', 'r') as logo:
        print(logo.read())


def _clear_screen():
    os.system(['clear','cls'][os.name == 'nt'])

def _invalid_prompt():
    print("Please try again, I did not understand your command.")
    input("PRESS ENTER")
    _clear_screen()

def exit():
    sys.exit()

def search_file(filename):
    try:
        print("Enter search term:")
        query = input('CodLib> ').lower()
    except EOFError:
        print('\nExiting...\n')
        sys.exit()
    with open(filename) as file:
        for line in file:
            if query in line:
                print(line)

    search()

def search(): # [RESOLVED]
    print("Please choose your prog lang\n(1)Python\n(2)SQL[i]\n")
    options = {'1': functools.partial(search_file, 'python.txt'),
               '2': functools.partial(search_file, 'sql.txt'),'e': sys.exit}
    while 1:
        choice = str(input("CodLib> ")).lower()
        try:
            options[choice]()
        except KeyError:
            print("'{0}': invalid option. Try Again." .format(choice))
    options.get(options, _invalid_prompt)()

class applySnip(object):
    def appl(self):
        print("Please Choose Your Programming\
 Language\n(1)Python\n(2)SQL[i]\n(3)Main Menu")

        options = {
            '1': snip.pyAppl,
            '2': snip.sqlAppl,
            '3': mainMenu,
            'e': sys.exit
            }

        while 1:
            choice = str(input("CodLib> ")).lower()
            try:
                 options[choice]()
            except KeyError:
                print("'{0}': invalid option. Try Again." .format(choice))
        options.get(options, _invalid_prompt)()
    def pyAppl(self):
        print("Is your snippet multilined? y/n")
        option = input('codlib> ').lower()[0]
        if option == 'y':
            # ADD MULTILINED FUNCTION HERE
            print("Please write your snippet in this format: \
                                Snippet:What it does. Type ^C when done")
            line = 0
            while line < 1000:
                line += 1
                snippet = input("CodLib> ")
                with open('python.txt','a') as f:
                    f.write("\n"+ snippet)
            print("Done!")
            snip.appl()
        elif option == 'n':
            print("Please write your snippet in this format:\
 Snippet:What it does.")
            snippet = input("codlib> ")
            print("Done!")
            snip.appl()
            with open("python.txt", "a") as f:
                f.write("\n" + snippet)
    def sqlAppl(self):
        print("Is your snippet multilined? y/n")
        option = input('codlib> ').lower()[0]
        if option == 'y':
            # ADD MULTILINED FUNCTION HERE
            print("Please write your snippet in this format: \
                                Snippet:What it does. Type ^C when done")
            line = 0
            while line < 1000:
                line += 1
                snippet = input("codlib> ")
                with open("sql.txt", "a") as f:
                    f.write("\n" + snippet)
            print("Done!")
            snip.appl()
        elif option == 'n':
            print("Please write your snippet in this format: \
 Snippet:What it does.")
            snippet = input("codlib> ")
            print("Done!")
            snip.appl()
            with open("sql.txt", "a") as f:
                f.write("\n" + snippet)



snip = applySnip()

def mainMenu():
    _clear_screen() #Will clear the terminal to avoid clutter.
    _print_logo()
    callbacks = [search,snip.appl,exit]
    choice = int(input('Enter Your Choice: '))
    try:
        callbacks[choice]() # call cooresponding options
    except IndexError:
        print('"%s":invalid option. Try Again.'% (choice))

if __name__ == '__main__':
    mainMenu()
