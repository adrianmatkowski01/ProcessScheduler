import data_handler
import random


seed = 260120230002
random.seed(seed)

output_name = input("What should the filename be: ")
data = {"slot_sizes":[0], "id_set":[0]}
data["slot_sizes"] = [int(x) for x in input("Slot sizes (separated by spaces): ").split()]

sample_size = int(input("How many samples: "))

sample_range = int(input("What should the sample range be: "))


for x in range(1, int(sample_size)+1):
    data["id_set"].extend([random.randint(1, sample_range)])

data_handler.write_data(data, output_name)

