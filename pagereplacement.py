import data_handler

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

            for page in self.page_list:
                
                if not slot.size > len(current_slots):

                    if page.id not in current_slots:
                        current_slots.pop(0)

                current_slots.append(page.id)

                print("for " + str(page.id))
                print([str(meme) for meme in current_slots])
                        
            print("done: " + str(slot.size))
            

class LRUHandler:
    def __init__(self):
        self.page_list = PageHandler().create_pages()
        self.slots = PageHandler().create_slots()
        self.ticker = Ticker()

    def simulation(self):
        for slot in self.slots: # for each possible slot size
            current_slots = []

            for page in self.page_list: 
                if not slot.size > len(current_slots):
                    if page.id in current_slots:
                        current_slots.remove(page.id)
                    
                    else:
                        current_slots.pop(0)
                        
                current_slots.append(page.id)



                print("for " + str(page.id))
                print([str(meme) for meme in current_slots])
                        
            print("done: " + str(slot.size))




def main():    
    FIFOHandler().simulation()
    LRUHandler().simulation()
main()
# class Processor