import threading
import time
import nmap3
exitFlag = 0


class myThread (threading.Thread):

    def __init__(self, threadID, name, target):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.target = target

    def run(self):

        print("Starting " + self.name)
        print_time(self.target)
        print("Exiting " + self.name)

def print_time(target):
        
        map = nmap3.Nmap()

        sonuc = map.nmap_os_detection(target)

        print(sonuc)


# Create new threads
target ="10.0.0.50"
sayac = 0
liste = {"10.0.0.50","10.0.0.25","10.0.0.19","10.0.0.21"}
for i in liste:
    #print(i)
    sayac+=1
    thread + str(sayac) = myThread(str(sayac), "Thread-1",i)
    
   
    


    
#thread1 = myThread(1, "Thread-1",target)
#thread2 = myThread(2, "Thread-2",target)
#thread3 = myThread(3, "Thread-2",target)
#thread4 = myThread(4, "Thread-2",target)





print("Exiting Main Thread")
