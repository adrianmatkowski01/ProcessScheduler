import matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt
import os
import sys
dir_path = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.append(parent_dir)
import data_handler

fcfs_json = data_handler.read_data("output/FCFSHandler.json")
lcfs_json = data_handler.read_data("output/LCFSHandler.json")

fcfs_total_time = [d["total_time"] for d in fcfs_json if "total_time" in d][0]
lcfs_total_time = [d["total_time"] for d in lcfs_json if "total_time" in d][0]

fcfs_average_time = [d["average_wait_time"] for d in fcfs_json if "average_wait_time" in d][0]
lcfs_average_time = [d["average_wait_time"] for d in lcfs_json if "average_wait_time" in d][0]




fig, (ax1, ax2) = plt.subplots(1,2)
ax1.bar(["FCFS", "LCFS"], [fcfs_total_time, lcfs_total_time], width=0.4)
ax1.set_ylabel("Total Time")
ax1.set_title("Total Time Comparison")

ax2.bar(["FCFS", "LCFS"], [fcfs_average_time, lcfs_average_time], width=0.4)
ax2.set_ylabel("Wait Time")
ax2.set_title("Wait Time Comparison")
# plt.show()
plt.savefig("plots/output/process.svg", format="svg")

