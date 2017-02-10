import sys
import sched
import urllib
import time
import webbrowser
s = sched.scheduler(time.time, time.sleep)
def task():
	for i in range(num):
            testfile.retrieve(name[i],filename[i])
            print "Download Complete"+str(i+1)
	
def bhago():
	sys.exit()

print time.time()
testfile = urllib.URLopener()
num=input("enter no. of download files for the special time")
name=[]
filename=[]
for j in range(num):
        name+=[raw_input("Enter url of website")]
        filename+=[raw_input("enter filename")]
curr_time = time.time()
time2 = 1486672189.76 
time5 = 1486682995.09
data = time2-curr_time
diff = time5 -time2 
s.enter(data, 1, task, ())
s.enter(data+diff,3,bhago, ())
s.run()
print time.time()
	
