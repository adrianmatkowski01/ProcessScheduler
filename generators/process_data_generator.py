import os
import sys
dir_path = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.append(parent_dir)
import data_handler
import random


seed = 260120230002
random.seed(seed)

data = []

output_name = input("What should the filename be: ")

process_size = int(input("How many processes: "))

process_range = int(input("What should the process range be: "))

max_arrival = int(input("What should the max arrival time be: "))

max_length = int(input("How big should the max process length be: "))

for x in range(process_size):
    name = "process" + str(random.randint(1,process_range))
    arrival = random.randint(1,max_arrival)
    length = random.randint(1,max_length)
    data.append({"process_id": name, "arrival_time": arrival, "burst_time": length})


data_handler.generator_data(data, output_name)


# data_handler.generator_data(data, output_name)

