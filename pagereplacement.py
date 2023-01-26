import data_handler
import matplotlib.pyplot

class Ticker:
    def __init__(self):
        self.time_elapsed = 0

    def tick(self):
        self.time_elapsed += 1



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
        
    def create_pages(self):
        data = data_handler.read_data("page_data.json")
        for page in data["id_set"]:
            page_obj = Page(page)
            self.page_list.append(page_obj)
        return self.page_list

    def create_slots(self):
        data = data_handler.read_data("page_data.json")
        for slot in data["slot_sizes"]:
            slot_obj = Slots(slot)
            self.slots.append(slot_obj)
        return self.slots

class FIFOHandler:
    def __init__(self):
        self.page_list = PageHandler().create_pages()
        self.slots = PageHandler().create_slots()
        self.ticker = Ticker()

    def simulation(self):
        for slot in self.slots: # for each possible slot size
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
                    



                self.ticker.tick()

                # print("for " + str(page.id))
                # print([str(meme) for meme in current_slots])
                        
            # print("done: " + str(slot.size))
            print("For slot: " + str(slot.size))
            print(swap_amount)
            

class LRUHandler:
    def __init__(self):
        self.page_list = PageHandler().create_pages()
        self.slots = PageHandler().create_slots()
        self.ticker = Ticker()

    def simulation(self):
        for slot in self.slots: # for each possible slot size
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
                self.ticker.tick()



                # print("for " + str(page.id))
                # print([str(meme) for meme in current_slots])
                        
            # print("done: " + str(slot.size))
            print("For slot: " + str(slot.size))
            print(swap_amount)




def main():    
    print("FIFO")
    FIFOHandler().simulation()
    print("LRU")
    LRUHandler().simulation()
main()
# class Processor