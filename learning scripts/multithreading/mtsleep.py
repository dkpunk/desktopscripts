import threading
from time import sleep,ctime
loops=[4,2]
def loop(nloop,nsec):
	print('start loop'+str(nloop)+' at: '+ctime())
	sleep(nsec)
	print('loop'+str(nloop)+' done at:'+ctime())
def main():
	print('starting at :'+ctime())
	threads=[]
	nloops=range(len(loops))
	for i in nloops:
		t=threading.Thread(target=loop,args=(i,loops[i])) # create a thread with index of the array and the content in it
		threads.append(t) #append the threads to the python threads by using append
	for i in nloops:
		threads[i].start() #initialized the threads 
	for i in nloops:
		threads[i].join() #waits for all the intialized threads to finish execution
	print('all DONE at :'+ctime())
if __name__ == '__main__':
	main()