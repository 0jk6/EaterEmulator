#eater assembler
import re
import sys

def assemble(inFilename, outFilename):
    #instruction set
    instructions = {
                "NOP" : 0x0,
                "LDA" : 0x1,
                "ADD" : 0x2,
                "SUB" : 0x3,
                "STA" : 0x4,
                "LDI" : 0x5,
                "JMP" : 0x6,
                "JC"  : 0x7,
                "JZ"  : 0x8,
                "OUT" : 0xE,
                "HLT" : 0xF
    }

    #open the asm file
    try:
        f = open(inFilename, "r")
    except:
        print(f"Error: {inFilename} file not found.")

    #copy the whole file into a buffer and close the file
    buffer = f.read()
    f.close()

    #split the buffer based on new lines, we will have a list of instructions
    tokens = buffer.split("\n")

    #output buffer
    output = []
    labels = {}
    re_label = re.compile("^\w*:$")
    re_comment = re.compile("^;.*$")
    pc = 0
    jumps = ("JMP", "JC", "JZ")

    print("Pass One: Find labels")
    for i in range(len(tokens)):
        if re_label.match(tokens[i]):
            labels[tokens[i][:-1]] = pc
        elif re_comment.match(tokens[i]):
            continue
        else:
            pc = pc + 1
    pc = 0 #set back to zero so we can show line numbers on output.

    print("Pass two: Assemble")
    #iterate through the tokens, convert them to hexadecimal
    #values based on instruction set and append it to output
    for i in range(len(tokens)):
        try:
            if re_label.match(tokens[i]) or re_comment.match(tokens[i]): #skip labels and comments altogether
                continue
            else:
                ins = tokens[i].split()
                if(ins[0] in instructions):
                    if ins[0] in jumps:
                        output.append(hex(instructions[ins[0]]<<4 | int(labels[ins[1]])))
                        print(pc, ins[0], labels[ins[1]])
                    elif(len(ins)==1):
                        output.append(hex(instructions[ins[0]]<<4 | 0 ))
                        print(pc, ins[0])
                    else:
                        if ins[1] in labels:
                            output.append(hex(instructions[ins[0]]<<4 | int(labels[ins[1]])))
                            print(pc, ins[0], labels[ins[1]])
                        else:
                            output.append(hex(instructions[ins[0]]<<4 | int(ins[1])))
                            print(pc, ins[0], ins[1])
                else:
                    if(len(ins)==1) or re_comment.match(ins[1]):
                        output.append(hex(int(ins[0])))
                        print(pc, ins[0])
                pc = pc + 1
        except Exception as e:
            #print(type(e))
            output.append(hex(0))


    #write the output buffer to a bin file by converting it into to bytes
    print("\n\nHex output")
    with open(outFilename, "wb") as f:
        for i in output:
            print(i)
            f.write(bytes((int(i,16),)))
        f.close()
    print("\n\nLabels Hashmap")
    print(labels)


if(len(sys.argv) != 4):
    print("Usage: python3 eas.py <asm filename> -o <bin filename>")
    exit()

inFilename = sys.argv[1]
outFilename = sys.argv[3]
assemble(inFilename, outFilename)
