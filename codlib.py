#! usr/bin/env python

# CodLib v1.2a
# Programmer: Michael Oselskyi
#DISCLAIMER: NOT COMPLETE! GUI soon though.



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
		option = raw_input('codlib> ').lower()[0]
		if option == 'y':
			# ADD MULTILINED FUNCTION HERE
			print "Please write your snippet in this format: Snippet:What it does. Type ^C when done"
			line = 0
			while line < 1000:
				line += 1
				snippet = raw_input("codlib> ")
				with open("python.txt", "a") as f:
					f.write("\n" + snippet)
			print("Done!")
			snip.appl()
		elif option == 'n':
			print "Please write your snippet in this format: Snippet:What it does."
			snippet = raw_input("codlib> ")
			if snippet == '/end/':
				print("Done!")
				mainMenu()
			with open("python.txt", "a") as f:
				f.write("\n" + snippet)
	def sqlAppl(self):
		print "Is your snippet multilined? y/n"
		option = raw_input('codlib> ').lower()[0]
		if option == 'y':
			# ADD MULTILINED FUNCTION HERE
			print "Please write your snippet in this format: Snippet:What it does. Type ^C when done"
			line = 0
			while line < 1000:
				line += 1
				snippet = raw_input("codlib> ")
				with open("sql.txt", "a") as f:
					f.write("\n" + snippet)
			print("Done!")
			snip.appl()
		elif option == 'n':
			print "Please write your snippet in this format: Snippet:What it does."
			snippet = raw_input("codlib> ")
			if snippet == '/end/':
				print("Done!")
				mainMenu()
			with open("sql.txt", "a") as f:
				f.write("\n" + snippet)
		
					

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
