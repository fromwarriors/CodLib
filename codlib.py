#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CodLib v1.24a
# Programmer: Michael Oselskyi & Natan L
#DISCLAIMER: NOT COMPLETE! GUI soon though.
# UPDATE 5/14/13: Added function to search through the sql file.
# Update 8/9/13: Added new-style classes, fixed the Ascii Art. Bugs: Line 33 and 48

import os
import sys


def _clear_screen():
	os.system(['clear','cls'][os.name == 'nt'])
	
def _invalid_prompt():
	print("Please try again, I did not understand your command.")
	input("PRESS ENTER")
	_clear_screen()

def search_file(filename):
	print("Enter your search terms.")
	query = input("codlib> ")
	
	with open(filename) as txt:
		for line in txt:
			if query in line:
				print(line)

	search.search()

def search():
	print("Please choose your prog lang\n(1)Python\n(2)SQL[i]")
	# I haven't tested the below. Potentially a bad idea. [CONFIRMED BROKEN]
	options = {
		'1': lambda: search_file('python'),
	'2': lambda: search_file('sql'),
	'e': sys.exit
	}
	
	valid = False
	while not valid:
		option = str(input("codlib> ")).lower()
	valid = option in options
	options.get(option, _invalid_prompt)()
	
def search_file(filename): # fix line
	print("Enter your search terms.")
	query = input("codlib> ")
	
	with open(filename) as txt:
		for line in txt:
			if query in line:
				print(line)

	search.search()


class applySnip(object):
	def appl(self):
		print("Please choose your prog language\n(1)Python\n(2)SQL[i]\n(3)Main Menu")
		
		options = {
			'1': snip.pyAppl,
			'2': snip.sqlApply,
			'3': mainMenu,
			'e': sys.exit
			}
		
		valid = False
		while not valid:
			option = str(input("codlib> ")).lower()
		valid = option in options
		options.get(option, _invalid_prompt)()  # snip.appl

def pyAppl(self):
	print("Is your snippet multilined? y/n")
	option = input('codlib> ').lower()[0]
	if option == 'y':
		# ADD MULTILINED FUNCTION HERE
		print("Please write your snippet in this format: Snippet:What it does. Type ^C when done")
		line = 0
		while line < 1000:
			line += 1
			snippet = input("codlib> ")
			with open("python.txt", "a") as f:
				f.write("\n" + snippet)
		print("Done!")
		snip.appl()
	elif option == 'n':
		print("Please write your snippet in this format: Snippet:What it does.")
		snippet = input("codlib> ")
		if snippet == '/end/':
			print("Done!")
			mainMenu()
		with open("python.txt", "a") as f:
			f.write("\n" + snippet)
def sqlAppl(self):
	print("Is your snippet multilined? y/n")
	option = input('codlib> ').lower()[0]
	if option == 'y':
		# ADD MULTILINED FUNCTION HERE
		print("Please write your snippet in this format: Snippet:What it does. Type ^C when done")
		line = 0
		while line < 1000:
			line += 1
			snippet = input("codlib> ")
			with open("sql.txt", "a") as f:
				f.write("\n" + snippet)
		print("Done!")
		snip.appl()
	elif option == 'n':
		print("Please write your snippet in this format: Snippet:What it does.")
		snippet = input("codlib> ")
		if snippet == '/end/':
			print("Done!")
			mainMenu()
		with open("sql.txt", "a") as f:
			f.write("\n" + snippet)



snip = applySnip()

def mainMenu():
	_clear_screen() #Will clear the terminal to avoid clutter.
	print("""
		   ___  _____  ____  __    ____  ____ 
		  / __)(  _  )(  _ \(  )  (_  _)(  _ \		   
		 (  (__ )(_)(  )(_) ))(__  _)(_  ) _ <	   
		  \___)(_____)(____/(____)(____)(____/
	   
		++++++++++++++++++++++++++++++++++++++++++++
		|          =  (1)Search  =                 |
		|          =  (2)Apply   =                 |
		++++++++++++++++++++++++++++++++++++++++++++""")
	
	options = {
		'1': search,
		'2': snip.appl,
		'e': sys.exit
		}
	
	valid = False
	while not valid:
		option = str(input("codlib> ")).lower()[0]
	valid = option in options
	options.get(option, _invalid_prompt)()
	
	if __name__ == '__main__':
		mainMenu()
mainMenu()

