class Shape:
 
    def set_edge(self,the_edge):
        
        self.my_edge=the_edge
    
    def get_edge(self):
        
        return self.my_edge
    
    def display(self):
        i = 1
        while i <= self.get_edge():        
            j = 1
            while j <=self.get_edge()+1-i:     
                print("*",end="")
                j +=1
            print("")                  
            i +=1
        return""

x=Shape()
x.set_edge(5)
print(x.display())
        