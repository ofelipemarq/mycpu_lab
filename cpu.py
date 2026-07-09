class CPU:
    def __init__(self):
        self.registers = {
            "R0": 0,
            "R1": 0,
            "R2": 0,
            "R3": 0,
        }
        
        self.pc = 0
        self.ir = None
        
        self.flags = {
            "Z": False,
            "N": False,
            "C": False,
            "V": False,
        }
        
    def dumb_state(self):
        print ("==== ESTADO DA CPU ==== ")
        
        print("\n REGISTRADORES: ")
        for register_name, value in self.registers.items():
            print (f"{register_name}: {value}")
            
        print ("\n CONTROLE: ")
        print (f"Pc: {self.pc}")
        print (f"IR: {self.ir}")
        
        print("\n FLAGS: ")
        for flags_name, value in self.flags.items():
            print (f"{flags_name}: {value}")

            
