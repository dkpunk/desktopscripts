from atexit import register
from re import compile
from threading import Thread 
from time import ctime
from urllib.request import urlopen as uopen 


REGEX= compile(b'#([\d,]+) in Books')
AMZN='https://www.amazon.com/dp/'

ISBNs={
	'0132269937' : 'Core Python Programming',
	'0132356139' : 'Python Web Development with Django',
	'0137143419' : 'Python Fundamentals',
}

def getRanking(isbn):
	page=uopen(AMZN+isbn)
	print("------------>"+AMZN+isbn+"<---------------")
	data=page.read()
	page.close()
	return str(REGEX.findall(data)[0],'utf-8')

def _showRanking(isbn):
	print('- %s ranked %s'%(ISBNs[isbn],getRanking(isbn)))

def _main():
	print('At',ctime(),'on Amazon..')
	for isbn in ISBNs:
		#_showRanking(isbn) #without multithreading
		Thread(target=_showRanking,args=(isbn,)).start()

@register                             # decorator which calls _atexit() when the script exits can alsoe be written "register(_atexit())""
def _atexit():
	print('all DONE at : ',ctime())

if __name__ == '__main__':
	_main()