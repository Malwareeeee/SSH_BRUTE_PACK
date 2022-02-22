import time 
import shodan
from colorama import Fore 
import threading

def select():
	print(Fore.LIGHTBLACK_EX + 'Program By Malware')
	print(Fore.RED + "Select 1-4, 1 = 100 | 2 = 200 | 3 = 300 | 4 = 400 |")
	dinp = input(Fore.RED + 'Enter Generated Amount: ')
	if dinp == '1':
		threading.Thread(target=search_for_ssh(),daemon=True).start()
		c = '100'
		threading.Thread(target=count_t(c)).start()
		select()
	elif dinp == '2':
		for i in range(1,3):
			threading.Thread(target=search_for_ssh(),daemon=True).start()
		c = '200'
		threading.Thread(target=count_t(c)).start()
		select()
	elif dinp == '3':
		for i in range(1,4):
			threading.Thread(target=search_for_ssh(),daemon=True).start()
		c = '300'
		threading.Thread(target=count_t(c)).start()
		select()
	elif dinp == '4':
		for i in range(1,5):
			threading.Thread(target=search_for_ssh(),daemon=True).start()
		c = '400'
		threading.Thread(target=count_t(c)).start()
		select()
	elif dinp == 'e':
		print(Fore.RED + 'Closing Process..')
		time.sleep(1)
		exit()
	else:
		print(Fore.RED + 'Sorry, That Format Isnt Recognized..')
		exit()

def count_t(process):
	print(Fore.GREEN + 'All Proccesses Have Been Completed | ST:200 | Total Ips Grabbed: %s' %(d))
	with open('SSHFILESAVE.txt','rb') as f:
		r = f.readlines()
	print(Fore.GREEN + 'Total Ips In Save: %s' %(len(r)))
	print(Fore.GREEN + 'Total Ips Written: %s' %(process))
	f.close()
	
def launch_api():
	SHODAN_KEY = '' # < - - Put Your Api  Key Here
	global api
	api = shodan.Shodan(SHODAN_KEY)

def write_to_files():
	time.sleep(1)
	for i in ssh_success_list:
		with open('SSHFILESAVE.txt','a') as f:
			f.write("%s"%(i))
	time.sleep(1)
	f.close()

def search_for_ssh():
	global ssh_success_list
	ssh_success_list = []
	try:
		results = api.search('ssh')
		for result in results['matches']:
			ssh_success_list.append(result['ip_str'] + '\n')
	except shodan.APIError as e:
			print(Fore.RED + 'Error: {}'.format(e))
	time.sleep(1)
	global d 
	d = results['total']
	write_to_files()

if __name__ == '__main__':
	launch_api()
	select()
