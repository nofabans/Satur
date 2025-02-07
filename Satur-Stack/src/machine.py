import inc.stackBuild as s
class machine:
    def __init__(self,prog:list[int]):
        self.variable_stack = s.stack()
        self.constant_stack = s.stack()
        self.program  = prog
        self.code     = [0]*3
        self.argtab:list[int] = []
        self.pc:int   = 0
        self.cmp: bool = True
    def get(self):
        for i in range(3):
            self.code[i] = self.program[self.pc+i]
        self.pc+=3
    def decode(self):
        ins = self.code[0]
        match ins:
            case 0:
                pass
            case 1:
                self.argtab.append(self.constant_stack.datas[self.code[1]])
            case 2:
                self.argtab.append(self.variable_stack.datas[self.code[1]])
            case 3:
                self.constant_stack.push(self.argtab[self.code[1]])
            case 4:
                self.variable_stack.push(self.argtab[self.code[1]])
            case 5:
                a,b = self.argtab[0:2]
                self.argtab[0] = a+b
            case 6:
                a,b = self.argtab[0:2]
                self.argtab[0] = a-b
            case 7:
                a,b = self.argtab[0:2]
                self.argtab[0] = a*b
            case 8:
                a,b = self.argtab[0:2]
                self.argtab[0] = a//b
            case 9:
                a,b = self.argtab[0:2]
                self.cmp = (a>b)
            case 10:
                a,b = self.argtab[0:2]
                self.cmp = (a<b)
            case 11:
                a,b = self.argtab[0:2]
                self.cmp = (a==b)
            case 12:
                a = self.argtab[0]
                self.cmp = (a==0)
            case 13:
                a = self.argtab[0]
                self.cmp = (a==self.code[1])
            case 14:
                if self.cmp:
                    self.pc = self.code[1]
            case 15:
                if not self.cmp:
                    self.pc = self.code[1]
            case 16:
                self.pc = self.code[1]
            case 17:
                self.variable_stack.push(self.variable_stack.bp)
                self.variable_stack.bp = self.variable_stack.sp+1
            case 18:
                self.variable_stack.sp = self.variable_stack.bp-1
                self.variable_stack.bp = self.variable_stack.pop()
            case 19:
                self.argtab.append(self.variable_stack.pop())
                self.variable_stack.push(self.argtab[-1])
            case 20:
                a,b = self.argtab[self.code[1]],self.argtab[self.code[2]]
            case 21:
                self.variable_stack.datas[self.variable_stack.bp+self.code[1]] = self.code[2]
            case 22:
                self.constant_stack.datas[self.code[1]] = self.code[2]
            case 23:
                print("OUT:",self.argtab[0])
            case 24:
                self.argtab = []
def test():
    '''
    GIVE_CONSTANT_NUM 0,1
    GIVE_CONSTANT_NUM 1,2
    LOAD_CONSTANT
    LOAD_CONSTANT
    ADD
    OUT
    '''
    test_vec = [0x16,0,1, 0x16,1,2, 1,0,0, 1,1,0, 5,0,0, 0x17,0,0, 0x18,0,0, 0,0,0]
    m = machine(prog=test_vec)
    while m.pc<len(test_vec):
        m.get()
        print(m.pc,m.code,m.argtab)
        m.decode()
test()
