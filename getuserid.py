from urllib.request import urlopen
from bs4 import BeautifulSoup

username = input('username: ')
try:
	html = urlopen('https://smashballoon.com/instagram-feed/find-instagram-user-id/?username='+username+'&address=&896914zje22267qjtl=4')
except:
	print('Could not get userID!')
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