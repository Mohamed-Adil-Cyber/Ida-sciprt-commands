def printRBX():
    print("-----------RBX,EBX,BX,BL,BH---------")
    try:
        print("BL = %x" % cpu.bl)
        print("BH = %x" % cpu.bh)
        print("BX = %x" % cpu.bx)
        print("EBX = %x" % cpu.Ebx)
        print("RBX = %x" % cpu.Rbx)
    except:
        pass
    
def printRAX():
    print("-----------RAX,EAX,AX,AL,AH---------")
    try:
        print("AH = %x" % cpu.ah)
        print("AL = %x" % cpu.al)
        print("AX = %x" % cpu.ax)
        print("EAX = %x" % cpu.Eax)
        print("RAX = %x" % cpu.Rax)
    except:
        pass

def printRCX():
    print("-----------RCX,ECX,CX,CL,CH---------")
    try:
        print("CH = %x" % cpu.ch)
        print("CL = %x" % cpu.cl)
        print("CX = %x" % cpu.cx)
        print("ECX = %x" % cpu.Ecx)
        print("RCX = %x" % cpu.Rcx)
    except:
        pass
        
def printRDX():
    print("-----------RDX,EDX,DX,DL,DH---------")
    try:
        print("DH = %x" % cpu.dh)
        print("DL = %x" % cpu.dl)
        print("DX = %x" % cpu.dx)
        print("EDX = %x" % cpu.Edx)
        print("RDX = %x" % cpu.Rdx)
    except:
        pass
        
def printRSI():
    print("-----------RSI,ESI,SI-------------")
    try:
        print("SI = %x" % cpu.si)
        print("ESI = %x" % cpu.Esi)
        print("RSI = %x" % cpu.Rsi)
    except:
        pass
        
def printRDI():
    print("-----------RDI,EDI,DI-------------")
    try:
        print("DI = %x" % cpu.di)
        print("EDI = %x" % cpu.Edi)
        print("RDI = %x" % cpu.Rdi)
    except:
        pass
        
def printRBP():
    print("-----------RBP,EBP,BP-------------")
    try:
        print("BP = %x" % cpu.bp)
        print("EBP = %x" % cpu.Ebp)
        print("RBP = %x" % cpu.Rbp)
    except:
        pass
        
def printRSP():
    print("-----------RSP,ESP,SP-------------")
    try:
        print("SP = %x" % cpu.sp)
        print("ESP = %x" % cpu.Esp)
        print("RSP = %x" % cpu.Rsp)
    except:
        pass       
              
def printRIP():
    print("-----------RIP,EIP----------------")
    try:
        print("EIP = %x" % cpu.Eip)
        print("RIP = %x" % cpu.Rip)
    except:
        pass
                                       
printRAX()
printRBX()
printRCX()
printRDX()
printRSI()
printRDI()
printRBP()
printRSP()
printRIP()
