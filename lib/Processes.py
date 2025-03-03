class Process:

    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time


class MLRRProcess(Process):

    def __init__(self,pid, burst_time, priority=0):
        super().__init__(pid, burst_time)
        self.priority = priority

    def __str__(self):
        return f"PID:{self.pid:>{8}} | Time Remaining: {self.burst_time:>{8}} | Priority:{self.priority:>{8}}"


class SJFProcess(Process):

    def __lt__(self, compared: Process):
        return self.burst_time < compared.burst_time

    def __str__(self):
        return f"PID:{self.pid:>{8}} | Time Remaining: {self.burst_time:>{8}}"