# EaterEmulator - Ben Eater's 8 Bit Breadboard CPU Emulator in Python

TinyE8 emulates [Ben Eater's](https://www.youtube.com/channel/UCS0N5baNlQWJCUrhCEo8WlA) 8 bit breadboard CPU. Implemented all the Instructions.

## Instruction set
```
 -------------------------------------------------------------------------------------------------------------------------------
| 0000 - NOP --> No Operation
| 0001 - LDA --> Load contents of a memory address XXXX into A register
| 0010 - ADD --> Load contents of a memory address XXXX into B register, then performs A+B and stores the result in A register
| 0011 - SUB --> Load contents of a memory address XXXX into B register, then performs A-B and stores the result in A register
| 0100 - STA --> Store contents of A register at memory address XXXX
| 0101 - LDI --> Load 4 bit immediate value into A register
| 0110 - JMP --> Unconditional jump: sets program counter to XXXX and executes from there
| 0111 - JC  --> Jump if carry: sets program counter to XXXX when carry flag is set and executes from there
| 1000 - JZ  --> Jump if zero: sets program counter to XXXX when zero flag is set and executes from there
| 1110 - OUT --> Output contents of A register to 7 segment display, in our case, we'll print it on console
| 1111 - HLT --> Halts the execution
 -------------------------------------------------------------------------------------------------------------------------------
```

#### Implemented Instructions:
- [x] NOP
- [x] LDA
- [x] ADD
- [x] SUB
- [x] STA
- [x] LDI
- [x] JMP
- [x] JC
- [x] JZ
- [x] OUT
- [x] HLT

## Loading your own program
Go to `cpu.py` file in `loadProgram()` function, add your own program after line 24

For example:

Loading a program that adds 7 and 3 would be as follows
```
LDA 1000
ADD 1001
OUT 0000

;at address 1000, we'll store 7
;and at address 1001, we'll store 3
```
In `cpu.py` file, you should write the code as follows
```
self.memory[0b0000] = 0b00011000; //LDA 1000 or load 7 into A register from memory[0b1000] or memory[8]
self.memory[0b0001] = 0b00101001; //ADD 1001 or load 3 into B register, then ADD and store it in A
self.memory[0b0010] = 0b11100000; //OUT 0000 or OUTPUT A register contents

//store data in the memory
self.memory[0b1000] = 7; //store 7 at memory[8], so that we can access it using LDA instruction
self.memory[0b1001] = 3; //store 3 at memory[9], so that we can access it using ADD instruction
```
You can write numbers in binary format or hexadecimal format

Here's a program that prints Triangular numbers upto 255,
```
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
```

I hope you understand it.

## Running th code
Installation of `Python 3.x` version is required.
Clone this repo `git clone https://github.com/jaychandra6/EaterEmulator` and run `python3 cpu.py` on Linux. 
If you are on Windows make sure that Python is added to your `PATH` and run `python cpu.py`.
