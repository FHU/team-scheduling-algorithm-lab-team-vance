#Abbie Vance and Evan Vance
#SJF
from lib.Queue import Queue
from lib.Processes import SJFProcess
import random

#CLASSES GO HERE
class SFJScheduler:
    def __init__(self, queue):
        self.queue = queue
    def schedule(self):
        current = self.queue.head;  
        index = None;  
        if(self.queue.is_empty()):
            print('Queue is empty')
        elif(self.queue.head == None):  
            return;  
        else:  
            while(current != None):  
                index = current.next;  
                  
                while(index != None):  
                    if(current.item < index.item):  
                        temp = current.item;  
                        current.item = index.item;  
                        index.item = temp;  
                    index = index.next;  
                current = current.next; 

if __name__ == '__main__':
#REMOVE PASS AND DEMONSTRATE THE SCHEDULER IN ACTION HERE
#CREATE ANY QUEUES, PROCESSES, CALL APPROPRIATE METHODS
    queue = Queue()
    for i in range(30):
        queue.put(SJFProcess(pid=random.randint(1,50), burst_time=random.randint(1,50)))
    scedule = SFJScheduler(queue)
    scedule.schedule()
    for i in range(queue.count):
        print(queue.get())