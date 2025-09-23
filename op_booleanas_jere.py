def AND(a,b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0
    
def OR(a,b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0
    
def NOT(a):
    if a == 0:
        return 1
    else: 
        return 0
    
def IMPL(a,b):
    if a == 1 and b == 0:
        return 0
    else:
        return 1

def NOR(a,b):
    if OR(a,b) == 1:
        return 0
    else:
        return 1

def NAND(a,b):
    if AND(a,b) == 1:
        return 0
    else:
        return 1
    
def XOR(a,b):
    if a != b:
        return 1
    else:
        return 0

def XNOR(a,b):
    if a == b:
        return 1
    else:
        return 0


print(AND(0, 1))   # 0
print(OR(0, 1))    # 1
print(NOT(0))      # 1
print(XOR(1, 1))   # 0
print(NAND(1, 1))  # 0
print(NOR(0, 0))   # 1
print(XNOR(1, 1))  # 1
print(IMPL(1, 0))  # 0