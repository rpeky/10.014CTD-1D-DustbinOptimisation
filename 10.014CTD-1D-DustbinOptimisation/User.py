class User():
    #to decide what user options there are
    def __init__(self):
        print('User created')
        self.CART_MAX_VAL =1000 
        self.rubbish_in_cart = 0
        self.job_completed = False
        self.current_vertex = ''
        self.distance_covered = 0
    
    #estimate a cart realistic max volume
    def check_cart_fullness(self):
        pass
    
    #force a nearest path to dump rubbish in cart
    def action_emptycart(self):
        # Another path-finding algorithm
        self.rubbish_in_cart = 0
        
    def validate_carthasspace(self, amount):
        return self.CART_MAX_VAL - self.rubbish_in_cart - amount > 0
        
    def action_rmeovetrash_addtocart(self, rubbish_amt):
        if self.validate_carthasspace(rubbish_amt):
            self.rubbish_in_cart += rubbish_amt
        else:
            pass
        #path find to nearest lift to empty cart, make new decision after

    def __del__(self):
        print('Job completed, deleting user')
        
    def printtest(self):
        print('printtest')

class Collector(User):
    def __init__(self, ID):
        super().__init__()
        self.collector_ID = ID
        
    def test_printname(self):
        print(self.collector_ID)
        
    def __del__(self):
        print('Job completed, clocking off')
        