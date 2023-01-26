import data_handler


class Ticker: # Thread?
    def __init__(self):
        self.time_elapsed = 0
    
    def time(self):
        return self.time_elapsed

    def tick(self):
        self.time_elapsed += 1


class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time

    def process_arrival(self):
        return self.arrival_time

    def process_length(self):
        return self.burst_time

    def name(self):
        return self.process_id

class ProcessHandler:
    def __init__(self):
        self.processes = []

    def create_processes(self):
        data = data_handler.read_data("process_data.json")
        for process in data:
            process_id = process['process_id']
            arrival_time = process['arrival_time']
            burst_time = process['burst_time']
            process_obj = Process(process_id, arrival_time, burst_time)
            self.processes.append(process_obj)
        return self.processes

 
class FCFSHandler:
    def __init__(self):
        self.processes = ProcessHandler().create_processes()

    def sort_processes(self):
        self.processes.sort(key=lambda process: process.process_arrival())
        return self.processes


class LCFSHandler:
    def __init__(self):
        self.processes = ProcessHandler().create_processes()

    def sort_processes(self):
        self.processes.sort(key=lambda process: process.process_arrival(), reverse=True)
        return self.processes


class Processor:
    def __init__(self):
        self.ticker = Ticker()
        self.time = 0

    def chooser(self, mode):
        if mode == "fcfs":
            self.process_algorythm(FCFSHandler())
        elif mode == "lcfs":
            self.process_algorythm(LCFSHandler())

    def process_algorythm(self, algorythm_obj):
        algorythm = algorythm_obj.sort_processes()
        algorythm_data = Data(algorythm, algorythm_obj.__class__.__name__)
        for process in algorythm:
            timer = 0
            while self.ticker.time() < process.process_arrival():
                self.ticker.tick()
            algorythm_data.wait_time_parser(process, self.ticker)
            while timer < process.process_length():
                self.ticker.tick()
                timer += 1
            self.time += timer
        algorythm_data.total_time_export(self.time)
        algorythm_data.average_wait_time()
            


class Data:
    def __init__(self, processes, class_name):
        self.class_name = class_name
        self.json_processes = [p.__dict__ for p in processes]
    
    def wait_time_parser(self, process: Process, exec_time: Ticker):
        wait_time = exec_time.time() - process.process_arrival()
        for x in self.json_processes:
            if x['process_id'] == process.name():
                x['wait_time'] = wait_time

    def total_time_export(self, total_time):
        self.json_processes.append({"total_time": total_time})
        self.to_json()

    def average_wait_time(self):
        sum = 0
        counter = 0
        for x in self.json_processes:
            if "wait_time" in x: 
                sum += x['wait_time']
                counter += 1
        time = sum/counter
        self.json_processes.append({"average_wait_time": time})
        self.to_json()

    def to_json(self):
        data_handler.write_data(self.json_processes, self.class_name)



    # def set_length(self, length):
    #     self.length = length


def test():
    Processor().chooser("lcfs")
    Processor().chooser("fcfs")
    # Data.to_json()

test()