'''
    Python file to implement the Treasure class
'''

class Treasure:
   
    def __init__(self, id, size, arrival_time):
       
        
        # DO NOT EDIT THE __init__ method
        self.id = id
        self.size = size
        self.arrival_time = arrival_time
        self.completion_time = None

    def set_rem(self,k):
        self.rem_size=k
    def ret_rem(self):
        return getattr(self,'rem_size', self.size)
    def set_time(self,x):
        self.upd_time=x
    def ret_time(self):
        return getattr(self,'upd_time', self.arrival_time)

