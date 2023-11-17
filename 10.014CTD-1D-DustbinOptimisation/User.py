


class User():
    #to decide what user options there are
    def __init__(self):
        print('User created')
        self.rubbish_in_cart = 0
        self.job_completed = False
        self.current_vertex = ''
        
    def check_cart_fullness(self):
        pass
    
    def action_emptycart(self):
        pass

    def __del__(self):
        print('Job completed, deleting user')
        

    def printtest(self):
        print('printtest')

class Collector(User):
    def __init__(self):
        super().__init__()
        
    def __del__(self):
        print('Job completed, clocking off')
        