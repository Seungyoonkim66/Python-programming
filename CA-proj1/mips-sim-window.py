def trans(a):
    if a == "0":
        a = "0000"
    if a == "1":
        a = "0001"
    if a == "2":
        a = "0010"
    if a == "3":
        a = "0011"
    if a == "4":
        a = "0100"
    if a == "5":
        a = "0101"
    if a == "6":
        a = "0110"
    if a == "7":
        a = "0111"
    if a == "8":
        a = "1000"
    if a == "9":
        a = "1001"
    if a == "a":
        a = "1010"
    if a == "b":
        a = "1011"
    if a == "c":
        a = "1100"
    if a == "d":
        a = "1101"
    if a == "e":
        a = "1110"
    if a == "f":
        a = "1111"

    return a

def Rtype(i):
    funct = i[26:]
    rs = int(i[6:11], 2)
    rt = int(i[11:16], 2)
    rd = int(i[16:21], 2)
    shamt = int(i[21:26], 2)
    if funct == "100000":
        print("add $%d, $%d, $%d" %(rd, rs, rt))
    elif funct == "100001":
        print("addu $%d, $%d, $%d" %(rd, rs, rt))
    elif funct == "100010":
        print("sub $%d, $%d, $%d" %(rd, rs, rt))
    elif funct == "100011":
        print("subu $%d, $%d, $%d" %(rd, rs, rt))
    elif funct == "100100":
        print("and $%d, $%d, $%d" %(rd, rs, rt))
    elif funct == "100101":
        print("or $%d, $%d, $%d" %(rd, rs, rt))
    elif funct == "100101":
        print("nor $%d, $%d, $%d" %(rd, rs, rt))
    elif funct == "100101":
        print("xor $%d, $%d, $%d" %(rd, rs, rt))
    elif funct == "101010":
        print("slt $%d, $%d, $%d" %(rd, rs, rt))
    elif funct == "101001":
        print("sltu $%d, $%d, $%d" %(rd, rs, rt))
    elif funct == "000000":
        print("sll $%d, $%d, %d" %(rd, rt, shamt))
    elif funct == "000010":
        print("srl $%d, $%d, %d" %(rd, rt, shamt))
    elif funct == "000011":
        print("sra $%d, $%d, %d" %(rd, rt, shamt))
    elif funct == "000110":
        print("srlv $%d, $%d, $%d" %(rd, rs, rt))
    elif funct == "000111":
        print("srav $%d, $%d, $%d" %(rd, rs, rt))
    elif funct == "001000":
        print("jr $%d" %(rs))
    elif funct == "001000":
        print("jalr $%d $%d" %(rd, rs))   
    elif funct == "011000":
        print("mult $%d, $%d" %(rs, rt))
    elif funct == "011001":
        print("multu $%d, $%d" %(rs, rt))
    elif funct == "011010":
        print("div $%d, $%d" %(rs, rt))
    elif funct == "011011":
        print("divu $%d, $%d" %(rs, rt))
    elif funct == "010000":
        print("mfhi $%d" %(rd))
    elif funct == "010001":
        print("mthi $%d" %(rs))
    elif funct == "010010":
        print("mflo $%d" %(rd))
    elif funct == "010011":
        print("mtlo $%d" %(rs))
    elif funct == "001100":
        print("systemcall")
    else:
        return 1
    
def Jtype(i):
    opcode = i[:6]
    addr = int(i[6:],2)
    if opcode == "000010":
        print("j %d" %(addr))
    elif opcode == "000011":
        print("jal %d" %(addr))
    else:
        return 2

def Itype(i):
    rs = int(i[6:11],2)
    rt = int(i[11:16],2)
    imm = int(i[16:],2)

    if opcode == "000100":
        print("beq $%d, $%d, %d" %(rs, rt, imm))
    elif opcode == "000101":
        print("bne $%d, $%d, %d" %(rs, rt, imm))
    elif opcode == "001000":
        print("addi $%d, $%d, %d" %(rt, rs, imm))
    elif opcode == "001001":
        print("addiu $%d, $%d, %d" %(rt, rs, imm)) 
    elif opcode == "001100":
        print("andi $%d, $%d, %d" %(rt, rs, imm)) 
    elif opcode == "001101":
        print("ori $%d, $%d, %d" %(rt, rs, imm)) 
    elif opcode == "001110":
        print("xori $%d, %d($%d)" %(rt, rs, imm)) 
    elif opcode == "001010":
        print("slti $%d, $%d, %d" %(rt, rs, imm)) 
    elif opcode == "001011":
        print("sltiu $%d, $%d, %d" %(rt, rs, imm)) 
    elif opcode == "001111":
        print("lui $%d, %d" %(rt, imm)) 
    elif opcode == "100011":
        print("lw $%d, %d($%d)" %(rt, imm, rs)) 
    elif opcode == "101011":
        print("sw $%d, %d($%d)" %(rt, imm, rs)) 
    elif opcode == "100000":
        print("lb $%d, %d($%d)" %(rt, imm, rs))
    elif opcode == "100100":
        print("lbu $%d, %d($%d)" %(rt, imm, rs))  
    elif opcode == "100001":
        print("lh $%d, %d($%d)" %(rt, imm, rs))  
    elif opcode == "100101":
        print("lhu $%d, %d($%d)" %(rt, imm, rs)) 
    elif opcode == "101000":
        print("sb $%d, %d($%d)" %(rt, imm, rs)) 
    elif opcode == "101001":
        print("sh $%d, %d($%d)" %(rt, imm, rs)) 
    else:
        return 3

with open('test2.bin') as data:
    inst_line=data.readlines()
data.close()

inst = []
for i in inst_line:
    i = i.replace(" ", "")
    inst.append(i[9:17])
    inst.append(i[17:25])
    inst.append(i[25:33])
    inst.append(i[33:41]) 

# instruction 이진수로 변환하기 
b_inst = []
for i in inst:
    if i == "":
        break
    else:
        for j in i:
            b_inst.append(trans(j))

#b_inst 32비트씩 나눠서 b32_inst 리스트에 저장
b32_inst = []
start = 0; end = 8
for i in b_inst:
    if b_inst == "":
        break
    else: 
        b = ''.join(b_inst[start:end])
        b32_inst.append(b)
        start += 8
        end += 8
while '' in b32_inst:
    b32_inst.remove('')

# assembly code로 변환
inst_num = 0
for i in b32_inst:
    
    print("inst %d: %s " %(inst_num, inst[inst_num]), end="")
    opcode = i[0:6]
    if opcode == "000000":
        ch = Rtype(i)
        if ch == 1:
            print("unkwnon instruction")
    elif opcode == "000010" or opcode =="000011":
        ch = Jtype(i)
        if ch == 2:
            print("unkwnon instruction")
    elif opcode == "000100" or opcode == "000101" or opcode == "001000" or opcode == "001001" or opcode == "001100" or opcode == "001101" or opcode == "001010" or opcode == "001011" or opcode == "001111" or opcode == "100011" or opcode == "101011" or opcode == "001110" or opcode == "100000" or opcode == "100100" or opcode == "100001" or opcode == "100101" or opcode == "101000" or opcode == "101001":
        ch = Itype(i)
        if ch == 3:
            print("unkwnon instruction")
    else:
        print("unknown instruction")
    inst_num += 1

