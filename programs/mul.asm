; perform a multiplication function by looping through the range
; defined by one of the factors (defined at address 13)
; and adding the second factor onto the product in each loop.
; the loop ends when the subtraction of the first factor by the 
; loop counter value reaches -1
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
    0       ; product
    7       ; factor
    6       ; factor
    1       ; loop counter value