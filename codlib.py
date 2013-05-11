# CodLib v1.1a
# Programmer: Michael Oselskyi
#DISCLAIMER: Not in anyway this is complete. It actually has errors. Cuz it's in alpha still. Yea. GUI coming soon.


#! usr/bin/env python

import os 
import sys
import re 

# Classes:
  
class searchProg:
	def search(self):
		print "Please choose your prog lang\n(1)Python\n(2)SQL[i]"
		op = raw_input("codlib> ")
		if op == '1':
			search.pySearch()
		elif op == '2':
			search.sqlSearch()
		elif op == 'exit' or op == 'EXIT':
			sys.exit()
		else:
			print "Try your query again."
			raw_input("PRESS ENTER")
			search.search()
	def pySearch(self):
		print "Enter your search terms."
		query = raw_input("codlib> ")
		
		for line in open("python.txt"):
			if query in line:
				print line
		search.search()
		
		
	def sqlSearch(self):
		print "NULL"

search = searchProg()


class applySnip:
	def appl(self):
		print "Please choose your prog language\n(1)Python\n(2)SQL[i]\n(3)Main Menu"
		op = raw_input("codlib> ")
		if op == '1':
			snip.pyAppl()
		elif op == '2':
			snip.sqlAppl()
		elif op == 'exit' or op == 'EXIT':
			sys.exit()
		elif op == '3':
			mainMenu()
		else:
			print "Try your query again."
			raw_input("PRESS ENTER")
			snip.appl()
	def pyAppl(self):
		print "Is your snippet multilined? y/n"
		option = raw_input('codlib> ')
		if option == 'y' or option == 'Y':
			# ADD MULTILINED FUNCTION HERE
			print "Please write your snippet in this format: Snippet:What it does. Type /end/ when done"
			line = 0
			while line < 2000:
				line += 1
				print "Line: ", line
				snippet = raw_input("codlib> ")
				with open("python.txt", "a") as f:
					f.write("\n" + snippet)
			print("Done!")
			snip.appl()
		elif option == 'n'or option == 'N':
			print "Please write your snippet in this format: Snippet:What it does."
			snippet = raw_input("codlib> ")
			if snippet == '/end/':
				print("Done!")
				mainMenu()
			with open("python.csv", "a") as f:
				f.write("\n" + snippet)
	def sqlAppl(self):
		print "Please write your snippet in this format: Snippet:What it does."
		snippet = raw_input("codlib> ")
		with open("sql.csv", "a") as f:
			f.write("\n" + snippet)
		print("Done!")
		snip.appl()
		
					

snip = applySnip()

def mainMenu():	
	os.system("clear")
	print(""" 
_______  _______  ______   _       _________ ______  
(  ____ \(  ___  )(  __  \ ( \      \__   __/(  ___ \ 
| (    \/| (   ) || (  \  )| (         ) (   | (   ) )
| |      | |   | || |   ) || |         | |   | (__/ / 
| |      | |   | || |   | || |         | |   |  __ (  
| |      | |   | || |   ) || |         | |   | (  \ \ 
| (____/\| (___) || (__/  )| (____/\___) (___| )___) )
(_______/(_______)(______/ (_______/\_______/|/ \___/ 
                                                      
	
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|                      =  (1)Search  =                             |
|                      =  (2)Apply   =                             |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
	
	op = raw_input("codlib> ")
	
	if op == '1':
		search.search()
	elif op == '2':
		snip.appl()
	elif op == 'exit' or op == 'EXIT':
			sys.exit()
	else: 
		print "Please try again, I did not understand your command."
		raw_input("PRESS ENTER")
		mainMenu()


	

mainMenu()
