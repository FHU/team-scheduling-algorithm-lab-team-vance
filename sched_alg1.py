#Abbie Vance and Evan Vance
#MLRR

from lib.Queue import Queue
from lib.Processes import MLRRProcess
import random


class MLRRScheduler:

    def __init__(self, layer_count=5, time_quantum=2):
        self.layers: list[Queue] = [Queue() for _ in range(layer_count)]
        self.time_quantum = time_quantum

    def schedule(self, proccess: MLRRProcess):
        if proccess.priority > len(self.layers):
            raise RuntimeError("Proccess Priority too large to handle")

        self.layers[proccess.priority].put(proccess)

    def consume(self):
        for i,queue in enumerate(self.layers):
            print(f"Queue layer: {i}")
            while not queue.is_empty():
                proccess = queue.get()
                print(proccess)

                #This is representative of doing the work of the process.
                proccess.burst_time -= self.time_quantum

                if proccess.burst_time > 0:
                    queue.put(proccess)


if __name__ == '__main__':

    schedule = MLRRScheduler()

    for i in range(30):
        schedule.schedule(MLRRProcess(pid=i, burst_time=random.randint(0,30), priority=random.randint(0,4)))
    
    schedule.consume()