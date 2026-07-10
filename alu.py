class ALU:
    def add (self, a, b):
        return a + b
    
    def sub (self, a,b):
        return a - b
    
    def mul (self,a,b):
        return a * b 
    
    def bitwise_and(self,a,b):
        return a and b
    
    def bitwise_or(self,a,b):
        return a or b
    
    def bitwise_not(self,a):
        return -a
    
    def cmp(self, a, b):
        return a - b 