import matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt
import os
import sys
dir_path = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.append(parent_dir)
import data_handler



lru_json = data_handler.read_data("output/LRUHandler.json")
fifo_json = data_handler.read_data("output/FIFOHandler.json")



lru_key = [int(next(iter(d))) for d in lru_json["swap_amount"]]
fifo_key = [int(next(iter(d))) for d in fifo_json["swap_amount"]]

lru_value = [d[next(iter(d))] for d in lru_json["swap_amount"]]
fifo_value = [d[next(iter(d))] for d in fifo_json["swap_amount"]]

fig, ax = plt.subplots()
ax.bar(lru_key, lru_value, label='LRU')
ax.bar(fifo_key, fifo_value, label='FIFO', width=0.4, align="edge")
ax.legend()
plt.yscale("log")
# plt.show()

plt.savefig("plots/output/pages.svg")

