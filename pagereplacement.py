import data_handler



class Tick:
    def __init__(self):
        self.time_elapsed = 0

    def tick(self):
        self.time_elapsed += 1



class Page:
    def __init__(self, name):
        self.name = name

class Window:
    def __init__(self, size):
        self.size = size

class PageHandler:
    def __init__(self):
        self.page_list = []    
        self.window_sizes = []
        
    def create_pages(self):
        data = data_handler.read_data("page_data.json")
    
