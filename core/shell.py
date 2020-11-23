# Coded by OneParsec

import pytube
from sys import exit, platform
from os import system
from time import sleep

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white



def check_res(resolution):
	if resolution == "720p" or resolution == "1080p" or resolution == "480p":
		pass
	else:
		print("Program support downloading on 1080p, 720p or 480p resolution")
		print("Program doesn't support this resolution! ")
		shell()


def help():
	print("clear	 	Clear the screen")
	print("quit		Exit the program")
	print("show		Show selected parameters")
	print("help		Show this message")
	print("run 		Start downloading")
	print("set 		Set parameters")
	print("Avalible parameters: link, resolution")
	print("Example: set link https://www.youtube.com/watch?v=uTOEiQSsCRk")



def startup_message():
		print("Welcome to " + R + "YouTube " + W + "Downloader Interactive Shell (YDIS)!\nType help!")

def shell():
	link = "Nothing"
	resolution = "Nothing"
	while True:
		try:
			an = input(R + "YDIS shell>> " + W)
			prompt = an.split()
			if not prompt:
				continue
			elif prompt[0] == "help":
				help()
			elif prompt[0] == "run":
				if link == "Nothing":
					print("Please, set link first!")
					shell()
				elif resolution == "Nothing":
					yt = pytube.YouTube(link)
					defaultres = "720p"
					filename = yt.streams.filter(res=defaultres).first().download()
					print("File successfuly saved to", filename)
				else:
					yt = pytube.YouTube(link)
					filename = yt.streams.filter(res=resolution).first().download()
					print("File successfuly saved to", filename)

			elif prompt[0] == "clear":
				print("\033[H\033[J")
			elif prompt[0] == "quit" or prompt[0] == "exit":
				print(C + "Exit!")
				exit(0)
			elif prompt[0] == "show":
				print("Download Link :", link)
				print("Resolution :", resolution)
			elif prompt[0] == "set":
				if prompt[1] == "link":
					try:
						link = prompt[2]
					except IndexError:
						print("Avalible parameters: link, resolution")
						print("You need to add one parameter: YouTube video link")
				if prompt[1] == "resolution":
					try:
						resolution = prompt[2]
					except IndexError:
						print("Avalible parameters: link, resolution")
						print("You need to add one parameter: Resolution")
					else:
						check_res(resolution)
			else:
				print("Command not found!")
		except KeyboardInterrupt:
			print(C + "\nExit!")
			exit(1)

startup_message()
shell()
