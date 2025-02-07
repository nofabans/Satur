class stack:
    def __init__(self):
        self.datas = [0]*1024
        self.sp =-1;self.bp = 0
        pass
    def push(self,val):
        assert self.sp<1024,OverflowError()
        self.sp+=1
        self.datas[self.sp] = val
    def pop(self):
        val = self.datas[self.sp]
        self.sp-=1
        return val
