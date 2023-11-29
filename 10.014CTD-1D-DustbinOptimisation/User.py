class User():
    #to decide what user options there are
    def __init__(self):
        print('User created')
        self.rubbish_in_cart = 0
        self.job_completed = False
        self.current_vertex = ''
    
    #estimate a cart realistic max volume
    def check_cart_fullness(self):
        pass
    
    #force a nearest path to dump rubbish in cart
    def action_emptycart(self):
        pass

    def __del__(self):
        print('Job completed, deleting user')
        
    def printtest(self):
        print('printtest')

class Collector(User):
    def __init__(self, ID):
        super().__init__()
        self.collector_ID=ID
        
    def __del__(self):
        print('Job completed, clocking off')
        