from crewmate import CrewMate
from heap import *
from treasure import Treasure

class StrawHatTreasury:
  
    def __init__(self, m):
        r=[]
        self.crewheap=Heap(comp_3,[])
        for i in range(m):
            self.crewheap.insert(CrewMate())
        self.active_crewlist=set()
            

    def add_treasure(self, treasure):
        x = self.crewheap.extract()
        x.treasureheap.insert(treasure)
        x.rem_load = max(0, x.rem_load - treasure.arrival_time + x.updated_time) + treasure.size

        x.updated_time = treasure.arrival_time
        self.crewheap.insert(x)
        self.active_crewlist.add(x)
        
            


    def get_completion_time(self):
        
        res=[]
        #for i in self.crewheap.heaplist:
        for i in self.active_crewlist:
            
            if(i.treasureheap.is_empty()):
               
                for j in i.priority_heap.heaplist:
                    res.append(j[1])
                 
                for k in i.completed_list:
                
                    res.append(k)
                continue
               
            while(not(i.treasureheap.is_empty())):
              
                present_treasure=i.treasureheap.extract()
               
                if(i.priority_heap.is_empty()):
                    i.priority_heap.insert([present_treasure.ret_rem(),present_treasure])
                    
                else:
                    peeked_treasure=(i.priority_heap.top())[1]
                  
                    wait_time=present_treasure.arrival_time-peeked_treasure.arrival_time
          
                    last_process_time=present_treasure.arrival_time-peeked_treasure.ret_time()
           
                    j=False
                    while((peeked_treasure.ret_rem()-(last_process_time))<=0):
                       
                         
                        kk=peeked_treasure.ret_time()
                        pp=peeked_treasure.ret_rem()
                    
                        peeked_treasure.completion_time=peeked_treasure.ret_time()+peeked_treasure.ret_rem()
                        peeked_treasure.set_rem(0)
                        
                        i.completed_list.append(peeked_treasure)
                        
                        i.priority_heap.extract()
        
                        if(i.priority_heap.is_empty()):
                        
                                   
                            i.priority_heap.insert([present_treasure.ret_rem(),present_treasure])
                            
                            j=True
                            break
                        else:
                           
                                  
                            peeked_treasure=(i.priority_heap.top())[1]
                            peeked_treasure.set_time(kk+pp)
                            
                            
                
                            wait_time=present_treasure.arrival_time-peeked_treasure.arrival_time
                            last_process_time=present_treasure.arrival_time-peeked_treasure.ret_time()
                     
                        

                    if(j==False):
                        if not i.priority_heap.is_empty():
                            
                            
                               
                            peeked_treasure.set_rem(peeked_treasure.ret_rem() - last_process_time)
                     
                            peeked_treasure.set_time(present_treasure.arrival_time)
                            
             
                        new_priority=-wait_time+peeked_treasure.ret_rem()
              
                        i.priority_heap.top()[0]=new_priority
                        i.priority_heap.insert([present_treasure.size,present_treasure])
                        
            last_arrival_time=present_treasure.arrival_time
            
            if(not(i.priority_heap.is_empty())):
                for t in i.priority_heap.heaplist:
                    t[0] = (-(last_arrival_time-t[1].arrival_time) + t[1].ret_rem())
                m=i.priority_heap.heaplist
                i.priority_heap=Heap(comp_2,m)

            i.priority_heap.sort()
     
            cumulative_time = last_arrival_time
           
            
            for tr in i.priority_heap.heaplist:
              
                cumulative_time += tr[1].ret_rem()
                
           
                tr[1].completion_time=cumulative_time
                res.append(tr[1])
            for jj in i.completed_list:
                           
                res.append(jj)
        
        return sorted(res,key=lambda c:c.id)

   
