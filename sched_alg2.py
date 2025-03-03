#Abbie Vance and Evan Vance
#SJF
from lib.Queue import Queue
from lib.Processes import SJFProcess
import random

#CLASSES GO HERE
class SFJScheduler:

    def __init__(self):
        self.ready_queue = Queue()


    def schedule(self, processes: list):
        processes.sort()
        for process in processes:
            self.ready_queue.put(process)


    def consume(self):
        for i in range(self.ready_queue.count):
            print(self.ready_queue.get())


if __name__ == '__main__':
#REMOVE PASS AND DEMONSTRATE THE SCHEDULER IN ACTION HERE
#CREATE ANY QUEUES, PROCESSES, CALL APPROPRIATE METHODS
    schedule = SFJScheduler()
    process_list = []
    for i in range(30):
        process_list.append((SJFProcess(pid=i,  burst_time=random.randint(1,30))))
    
    schedule.schedule(process_list)
    schedule.consume()
