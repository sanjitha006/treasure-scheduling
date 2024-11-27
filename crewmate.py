'''
    Python file to implement the class CrewMate
'''
from heap import *
class CrewMate:

    def __init__(self):
        self.treasureheap=Heap(comp_1,[])
        self.priority_heap=Heap(comp_2,[])
        self.updated_time=0
        self.rem_load=0
        self.completed_list=[]
        
        