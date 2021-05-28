import threading, queue
import nmap3

q = queue.Queue()

liste = []
nmap = nmap3.Nmap()
result =nmap.nmap_version_detection("192.168.1.113")
print(result)
result.append(liste)


def islem(threadName,q):
    global liste
    while not q.empty():
        item = q.get()
		
        print(f"{threadName} Çıkarılacak eleman: {item}")        
        q.task_done()

for i in liste:
    q.put(i)

for i in range(2):
    worker = threading.Thread(target=islem, args=(f"Thread-{i}",q), daemon=True)
    worker.start()

q.join()