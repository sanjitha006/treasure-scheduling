def comp_1(x,y):
    return (x.arrival_time < y.arrival_time)
def comp_2(x,y):
    return(x[0]<y[0] or (x[0]==y[0] and x[1].id<y[1].id))
def comp_3(x,y):
    return((x.rem_load-y.updated_time)<(y.rem_load-x.updated_time))

class Heap:
    def __init__(self,comparison_function, init_array=[]):
        self.comp = comparison_function
        self.heaplist = init_array
        if self.heaplist:
            self.buildHeap()

    def heapify(self, arr, n, i):
        lt = 2*i + 1
        rt = 2*i + 2
        small = i

        if (lt<n and self.comp(arr[lt],arr[i])):
            small = lt

        if (rt<n and self.comp(arr[rt], arr[small])):
            small= rt

        if (small!= i):
            arr[i],arr[small] = arr[small],arr[i]
            self.heapify(arr, n, small)

    def buildHeap(self):
        #print(self.heaplist)
        n = len(self.heaplist)
        for i in range((n-1)//2,-1,-1):
            self.heapify(self.heaplist, n, i)

    def insert(self, value):
        self.heaplist.append(value)
        i = len(self.heaplist) - 1

        while(i>=0 and (((i-1)//2)>=0)):
            if(not(self.comp(self.heaplist[(i-1)//2],self.heaplist[i]))):
                self.heaplist[(i-1)//2],self.heaplist[i]=self.heaplist[i],self.heaplist[(i-1)//2]
                i=(i-1)//2
            else:
                break

    def extract(self):
        if (len(self.heaplist)==0):
            return None

        self.heaplist[0], self.heaplist[-1] = self.heaplist[-1], self.heaplist[0]
        res= self.heaplist.pop()

        if (len(self.heaplist)!=0):
            self.heapify(self.heaplist, len(self.heaplist), 0)

        return res

    def top(self):
        if self.is_empty():
            return None
        return self.heaplist[0]

    def sort(self):
        n=len(self.heaplist)
        for i in range(n-1,0,-1):
            self.heaplist[i],self.heaplist[0]=self.heaplist[0],self.heaplist[i]
            self.heapify(self.heaplist,i,0)
        self.heaplist=self.heaplist[::-1]

    def is_empty(self):
        if(len(self.heaplist)==0):
            return True
        else:
            return False


