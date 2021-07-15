start:
    LDA 13
    SUB 15
    OUT
    JC  end
    STA 13
    LDA 12 
    ADD 14
    STA 12 
    JMP start
end:
    LDA 12
    OUT
    HLT
data:
    0
    7
    6
    1