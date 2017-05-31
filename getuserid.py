from urllib.request import urlopen
from bs4 import BeautifulSoup

#-------------------------------------------------------------------
#---------------retrieve site id (antibot defence)-------------------
try:
	html = urlopen('https://smashballoon.com/instagram-feed/find-instagram-user-id/')
except:
	print('Could not get userID! Site is down')
	exit()
if html:
	bs0bj = BeautifulSoup(html,'lxml')
	namelist = bs0bj.findAll({'input','size'})
	raw = str(namelist[2])
	b = raw.split('"')
	secretid = b[1]

#--------------------------------------------------------------------
#-----------------retrieve userid from username----------------------
username = input('username: ')
try:
	html = urlopen('https://smashballoon.com/instagram-feed/find-instagram-user-id/?username='+username+'&address=&'+secretid+'=4')
except:
	print('Could not get userID! Site is down')
	exit()
if html:
	bs0bj = BeautifulSoup(html,'lxml')
	namelist = bs0bj.findAll('div','user match')
	try:
		string = (namelist[0].get_text())
		a, userid = string.split(': ')
		print (userid)
	except IndexError:
		print('Error! Non existent user.')
