from memory import Memory

def main():
    
    memory = Memory()
    
    memory.write(10, 37)
    
    value = memory.read(10)
    
    print (value)
    
    memory.dump(8,13)
    
main()