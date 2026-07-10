from memory import Memory
from cpu import CPU

def main():
   cpu = CPU()
   
   cpu.registers["R1"] = 8
   cpu.registers["R2"] = 13
   
   result = cpu.alu.add(cpu.registers["R1"], cpu.registers["R2"])
   
   cpu.registers ["R1"] = result
   cpu.uptade_flags(result)
   
   cpu.dumb_state() 
   
    
main()