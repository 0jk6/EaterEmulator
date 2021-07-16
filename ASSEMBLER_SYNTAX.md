# Using the assembler

This project includes an Assembler for the BenEater CPU.  It support some of the standard capabilities you would expect to find in a standard assember.

The Ben Eater 8bit CPU has only 16 bytes of RAM.  Your program must fit into 16 bytes and this includes any data you need to initialise the program with.

The computer only has a 3 char 7 Segment LED Display allowing for output of numbers from 0-255.

## Table of contents

* [Table of contents](#table-of-contents)
* [Usage](#usage)
* [Syntax](#syntax)
  * [Comments](#comments)
  * [Labels](#labels)
  * [Whitespace](#whitespace)
  * [Addressing Modes](#addressing-modes)
* [List of Supported Instructions](#list-of-supported-instructions)

## Usage

Executing the assembler without any arguments will issue this help message.

``` text
~ python3 eas.py
Usage: python3 eas.py <asm filename> -o <bin filename>
```

A more complete example:

``` text
~ python3 eas.py programs/fib.asm -o programs/fib.bin
Pass One: Find labels
Pass two: Assemble
0 LDI 1
1 STA 14
2 LDI 0
3 STA 15
4 OUT
5 LDA 14
6 ADD 15
7 STA 14
8 OUT
9 LDA 15
10 ADD 14
11 JC 13
12 JMP 3
13 HLT
14 0
15 1


Hex output
0x51
0x4e
0x50
0x4f
0xe0
0x1e
0x2f
0x4e
0xe0
0x1f
0x2e
0x7d
0x63
0xf0
0x0
0x1


Labels Hashmap
{'start': 0, 'loop': 3, 'end': 13}


Binary Code for programming with Dip Switches

Addr : Inst : Data
==== : ==== : ====
0000 : 0101 : 0001
0001 : 0100 : 1110
0010 : 0101 : 0000
0011 : 0100 : 1111
0100 : 1110 : 0000
0101 : 0001 : 1110
0110 : 0010 : 1111
0111 : 0100 : 1110
1000 : 1110 : 0000
1001 : 0001 : 1111
1010 : 0010 : 1110
1011 : 0111 : 1101
1100 : 0110 : 0011
1101 : 1111 : 0000
1110 : 0000 : 0000
1111 : 0000 : 0001
```

## Syntax

### Comments

Comments are ignored by the assembler and are always prefixed by a simicolon. (`;`)

``` asm
; This is a comment on a line by itself.
    LDA 15  ; This is an inline comment and must be at the end of a line.
```

### Labels

* Labels must be on a line on their own.
* No whitespace before the label.
* The assembler will match a label based on this regular expression: `"^\w*:$"`  IE: Start of line, any number of alphanumeric and underscores but no whitespace and a colon (`:`) at the end.
* When you use a label in an instruction, DO NOT include the colon at the end.

``` asm
; simple program to count up from zero
start:
    LDA counter
    ADD increment
    OUT
    JMP start
counter:
    0
increment:
    1
```

In this example, the labels: `start`, `counter`, and `increment` all act as pointeres to memory addresses.  The assembler will pass through the code first to find all the labels and record their memory addresses.  Then on the second pass it will substitue the labels for the actual addresses.  The intermediate assembly is printed to the console showing these substitutions.

### Whitespace

At least one whitespace character is required between menmonics that require arguments and their arguments.  You can use more than one whitespace character - the assembler treats all continuou whitespace a single separator for tokenizing terms.

### Addressing Modes

This assembler expects all address locations to be expressed in decimal or a label reference.  IE: For address location `0b1111` (`0xF`) you need to enter `15`.

In the example below, the LDA and ADD statements refer to addresses by their labels.  The JMP statement explicitly declares the first address (`0b000`) by its decimal representation.

``` asm
start:
  LDI 0             ; 0 in this case is the value to load into A
  ADD increment     ; Add the value stored at address labeled, "increment"
  OUT               ; display the result to the 7segment LCD display
  JMP 0             ; Set the program counter (jump) to address 0
increment:
  2
```

## List of Supported Instructions

This is the table of instructions that are available.

| Menmonic | Argument         | Description
|----------|------------------|-------
| NOP      | None             | No Operation
| LDA      | Address or Label | Load contents of a memory address XXXX into A register
| ADD      | Address or Label | Load contents of a memory address XXXX into B register, then performs A+B and stores the result in A register
| SUB      | Address or Label | Load contents of a memory address XXXX into B register, then performs A-B and stores the result in A register
| STA      | Address or Label | Store contents of A register at memory address XXXX
| LDI      | Value            | Load 4 bit immediate value into A register
| JMP      | Address or Label | Unconditional jump: sets program counter to XXXX and executes from there
| JC       | Address or Label | Jump if carry: sets program counter to XXXX when carry flag is set and executes from there
| JZ       | Address or Label | Jump if zero: sets program counter to XXXX when zero flag is set and executes from there
| OUT      | None             | Output contents of A register to 7 segment display, in our case, we'll print it on console
| HLT      | None             | Halts the execution
