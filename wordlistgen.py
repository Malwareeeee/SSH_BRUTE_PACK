from colorama import Fore 
import time 
import os
import threading

def search(ti):
	with open(ti,'r') as f:
		r1 = f.readlines()
	for i in r1:
		sp = i.split(':')											
		with open('newuser.txt','a') as f2:
			f2.write(sp[0] + '\n')
		with open('newpass.txt','a') as f3:
			f3.write(sp[1])
		with open('newuser.txt','r') as f4:
			rl12 = f4.readlines()
		with open('newpass.txt','r') as f5:
			rl13 = f5.readlines()
	print("Process Finished | %s Usernames | %s Passwords"%(len(rl12),len(rl13)))

def banner():
	time.sleep(1)
	print(Fore.LIGHTBLACK_EX + 'Wordlist Creater | By: Malware | ')
	launch()

def invalid():
	print(Fore.RED + 'Sorry That File Hasnt Appeared, Try Placing It Into CWD')
	launch()

def continue_(ti):
	time.sleep(1)
	print(Fore.GREEN + 'Sorting Through %s In %s | ST:200 |' %(ti,os.getcwd()))
	print(Fore.GREEN + 'This May Take A Minute, Please Wait...')
	threading.Thread(target=search(ti),daemon=True).start()

def launch():
	time.sleep(1)
	print(Fore.RED + 'Select Your File Containing Initial Wordlist Format | EX: root:root |')
	ti = input(Fore.RED + 'wordlist@wordlist:~$ ')
	success_f = []
	skip = False
	for i in os.listdir(os.getcwd()):
		if not i == ti:
			skip = True
			continue 
		if skip:
			skip = False 
		success_f.append(i)
	if len(success_f) < 1:
		print("Sorry, That File Hasn't Appeared. Try Moving This File To The CWD")
	else:
		continue_(ti)

if __name__ == '__main__':
	banner()
