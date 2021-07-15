import sys
import time

class CPU:
    def __init__(self):
        #Program counter
        self.pc = 0

        #Registers A, B, IR
        self.A = 0
        self.B = 0
        self.IR = 0

        #RAM or self.memory, 4 bit address bus --> 2^4 = 16 bytes of RAM
        self.memory = [0]*16

        #Output register
        self.OUT = 0;

        #Flags
        self.CF = False
        self.ZF = False
        self.HALT = False

    def loadProgram(self, filename):
        #Load your own program manually
        if filename == "default":
            #prints triangular numbers

            self.memory[0x0] = 0x1F
            self.memory[0x1] = 0x2E
            self.memory[0x2] = 0x79
            self.memory[0x3] = 0xE0
            self.memory[0x4] = 0x4F
            self.memory[0x5] = 0x1E
            self.memory[0x6] = 0x2D
            self.memory[0x7] = 0x4E
            self.memory[0x8] = 0x60
            self.memory[0x9] = 0x50
            self.memory[0xA] = 0x4F
            self.memory[0xB] = 0x1D
            self.memory[0xC] = 0x4E
            self.memory[0xD] = 1
            self.memory[0xE] = 1
            self.memory[0xF] = 0

        else:
            #if the file name was specified open it
            try:
                with open(filename, "rb") as f:
                    buffer = f.read()
                    f.close()
            except:
                print(f"Error: cannot open file: {filename}")
                exit()

            for i in range(16):
                self.memory[i] = buffer[i];

    def execute(self):
        #decode instruction from opcode by masking higher 4 bits
        opcode = (self.IR & 0xF0) >> 4;

        if(opcode == 0x0):
            #NOP
            pass;
        elif(opcode == 0x1):
            #LDA
            self.A = self.memory[self.IR & 0x0F]
        elif(opcode == 0x2):
            #ADD
            self.CF = (self.A + self.memory[self.IR & 0x0F]) > 255
            self.B = self.memory[self.IR & 0x0F]
            self.A = self.A + self.B
            self.ZF = self.A == 0
        elif(opcode == 0x3):
            #SUB
            self.CF = (self.A - self.memory[self.IR & 0x0F]) < 0
            self.B = self.memory[self.IR & 0x0F]
            self.A = self.A - self.B
            self.ZF = self.A == 0
        elif(opcode == 0x4):
            #STA
            self.memory[(self.IR & 0x0F)] = self.A
        elif(opcode == 0x5):
            #LDI
            self.A = self.IR & 0x0F
        elif(opcode == 0x6):
            #JMP - jump to address (self.IR & 0x0F) and do not increment the program counter
            self.pc = (self.IR & 0x0F) - 1
        elif(opcode == 0x7):
            #JC
            if self.CF:
                self.pc = (self.IR & 0x0F) - 1
        elif(opcode == 0x8):
            #JZ
            if self.ZF:
                self.pc = (self.IR & 0x0F) - 1
        elif(opcode == 0xE):
            #OUT
            self.OUT = self.A
            print(f"OUT : {self.OUT}")
        elif(opcode == 0xF):
            #HLT
            self.HALT = True
        else:
            print(f"Illegal opcode {hex(opcode)}")


def main(filename, speed):
    cpu = CPU()
    cpu.loadProgram(filename)

    while not cpu.HALT:
        #fetch instruction into Instruction Register
        try:
            cpu.IR = cpu.memory[cpu.pc]
            cpu.execute()
            cpu.pc += 0b0001
            time.sleep(float(speed)) #clock speed
        except Exception as e:
            print("HALTING System...")
            break;

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        speed = sys.argv[2]
    except:
        print(" ------------------------------------------- ")
        print("|Usage: python3 cpu.py <bin file> <speed>   |")
        print(" ------------------------------------------- \n")
        print(" ------------------------------------------- ")
        print("| <bin file> : compiled asm file            |\n| <speed> : (0 to 1), 0 fastest, 1 slowest  |\n")
        print("| Default program: Triangular Numbers       |\n| Run: python3 cpu.py default <speed>       |")
        print(" ------------------------------------------- \n")
        print(" ------------------------------------------- ")
        print("| Example: python3 cpu.py fib.bin 0.05      |")
        print(" ------------------------------------------- \n")
        exit()
    main(filename, speed)
