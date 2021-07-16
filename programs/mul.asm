; perform a multiplication function by looping through the range
; defined by one of the factors (defined at address 13)
; and adding the second factor onto the product in each loop.
; the loop ends when the subtraction of the first factor by the 
; loop counter value reaches -1
start:
    LDA factor1
    SUB 15  ; decrement by value at address 15
    NOP
    JC  end
    STA factor1
    LDA product
    ADD factor2
    STA product
    JMP 0
end:
    LDA 12
    OUT
    HLT
; these are in effect data labels.
product:
    0
factor1:
    7
factor2:
    6
decrement:
    1       ; loop counter value