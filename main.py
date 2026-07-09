from memory import Memory
from cpu import CPU

def main():
    
    memory = Memory()
    
    memory.write(10, 37)
    
    value = memory.read(10)
    
    print (value)
    
    memory.dump(8,13)
    
    
    cpu = CPU()
    
    cpu.dumb_state()
    
    
main()