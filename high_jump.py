


class high_jump_machine:
    
    @staticmethod
    def repeat_lo(base):
        def decorated(self, lo):
            if lo == 0:
                lo = self.func[self.fptr]
                self.fptr += 1
            base(self, lo)
        return decorated
            
    @staticmethod
    def get_literals(base):
        def decorated(self, lo):
            literals = self.func[self.fptr:self.fptr + lo]
            self.fptr += lo
            base(self, literals)
        return decorated
    
    def __init__(self, main):
        self.func = main;
        self.fptr = 0;
        self.stack = [];
        self.call = [];
        self.reg = [];
        
    def get(self, lo):
        return self.stack[len(self.stack) - lo]
        
    def pop(self, lo):
        return self.stack.pop(len(self.stack) - lo)
        
    def jump(self, lo):
        byte = self.stack[-1]
        if lo & 8:
            self.stack.pop()
        if lo & 7 == 7:
            jump = True
        elif byte == 0:
            jump = lo & 1
        elif byte  > 0:
            jump = lo & 2
        elif byte <  0:
            jump = lo & 4
        if jump:
            self.fptr += self.stack[self.fptr]
    
    @repeat_lo
    @get_literals
    def cpush(self, literals):
        for byte in literals:
            self.stack.append(byte)
    
    def push(self, lo):
        self.stack.append(self.get(lo))
    
    def pull(self, lo):
        if lo:
            self.stack.append(self.pop(lo))
        else:
            lo = self.func[self.fptr]
            self.func += 1
            self.push(lo)  # special case to turn a no-op into lpush
    
    def bury(self, lo):
        lo = lo or 16  # turn no-op into useful special tool for accessing 16th element
        el = self.stack.pop()
        self.stack.insert(len(self.stack) - lo, el)
        
    def __iter__(self):
        hi_ops = [
            self.jump,      # 0 change fptr
            
            self.cpush,     # 1 add constants to the stack (note LIFO)
            self.push,      # 2 copy an element to the top of the stack
            self.pop,       # 3 delete an element from the stack
            self.pull,      # 4 move an element to the top of the stack and push the rest back
            self.bury,      # 5 push the top element down the stack, pulling the rest back
            
            self.math       # 6 arithmetic
            
            self.call       # 7 call a function, after which resume execution
            self.ccode      # A add bytes to the code register
            self.iccode     # B insert bytes after the last normal code or ccode execution
            self.code       # 8 add a byte from the stack to the code register
            self.icode      # 9 insert a byte from the stack after the last normal code or ccode execution
            self.functional # C
            
            self.input      # D
            self.output     # E
        ]
        while self.call or self.fptr < len(self.func):
            while self.fptr < len(self.func):
                byte = self.func[self.fptr]
                hi = byte >> 4
                lo = byte & 0x0F
                self.fptr += 1
                hi_ops[hi](lo)
                
                
            self.func, self.fptr = self.call.pop()
            self.fptr += 1
        


