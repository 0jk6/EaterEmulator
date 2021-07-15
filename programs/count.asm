start:
    LDI 0
printup:
    OUT
up:
    ADD 15
    JC down
    JMP printup
down:
    SUB 15
printdown:
    OUT
    JZ up
    JMP down
    NOP
    NOP
    NOP
    NOP
    NOP
    NOP
    3