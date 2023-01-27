import data_handler
import sys
import os

class Page:
    def __init__(self, id):
        self.id = id

class Slots:
    def __init__(self, size):
        self.size = size

class PageHandler:
    def __init__(self):
        self.page_list = []    
        self.slots = []

        if len(sys.argv) > 1:
            if sys.argv[1].endswith(".json"):
                if os.path.exists("input/" + sys.argv[1]):
                    self.data = data_handler.read_data("input/" + sys.argv[1])
                else:
                    print("That file doesn't exist in the input/ folder.")
                    exit(-1)
            else:
                print("Please provide a file path ending in '.json'.")
                exit(-1)
        else:
            print("No input file given.")
            exit(-1)

    def create_pages(self):
        for page in self.data["id_set"]:
            page_obj = Page(page)
            self.page_list.append(page_obj)
        return self.page_list

    def create_slots(self):
        
        for slot in self.data["slot_sizes"]:
            slot_obj = Slots(slot)
            self.slots.append(slot_obj)
        return self.slots

class FIFOHandler:
    def __init__(self):
        self.handler = PageHandler()
        self.page_list = self.handler.create_pages()
        self.slots = self.handler.create_slots()
        self.data = []

    def simulation(self):
        for slot in self.slots: 
            current_slots = []
            swap_amount = 0
            for page in self.page_list:
                if slot.size > len(current_slots):
                    if page.id not in current_slots:
                        current_slots.append(page.id)
                    
                else:
                    if page.id not in current_slots:
                        current_slots.pop(0)
                        swap_amount += 1
                        current_slots.append(page.id)
            self.data.append({slot.size: swap_amount})
        Data(self.handler.data).export_data(self.data, __class__.__name__)
            

class LRUHandler:
    def __init__(self):
        self.handler = PageHandler()
        self.page_list = self.handler.create_pages()
        self.slots = self.handler.create_slots()
        self.data = []

    def simulation(self):
        for slot in self.slots: 
            current_slots = []
            swap_amount = 0
            for page in self.page_list: 
                if not slot.size > len(current_slots):
                    if page.id in current_slots:
                        current_slots.remove(page.id)
                        current_slots.append(page.id)
                    
                    else:
                        current_slots.pop(0)
                        current_slots.append(page.id)
                        swap_amount += 1
                else:
                    if page.id not in current_slots:
                        current_slots.append(page.id)
            self.data.append({slot.size: swap_amount})
        Data(self.handler.data).export_data(self.data, __class__.__name__)
        

class Data:
    def __init__(self, data):
        self.data = data

    def export_data(self, output_data, file_name):
        self.data["swap_amount"] = output_data
        data_handler.write_data(self.data, file_name)
        

def main():    
    FIFOHandler().simulation()
    LRUHandler().simulation()
main()