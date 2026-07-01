class Memory:
    def __init__(self, size=256):
        self.size = size
        self.data = [0] * size
        
    def validate_adress(self, adress):
        if adress < 0 or adress >= self.size:
            raise IndexError (f"Endereço inválido: {adress}")
    
    def read(self, adress):
        self.validate_adress(adress)
        return self.data[adress]
    
    def write(self, address, value):
        self.validate_adress(address)
        self.data[address] = value 
        
    def dump(self, start=0, end=10):
        self.validate_adress(start)
        self.validate_adress(end -1)
        
        for address in range(start, end):
            print (f"{address}: {self.data[address]}")
    