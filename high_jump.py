

class high_jump_machine:
    def __init__(self, main):
        self.top = main;
        self.fptr = 0;
        self.stack = [];
        self.call = [];
        self.code = [];
        
    def __iter__(self):
        hi_ops = [
            self.jump,      # 0 change fptr
            
            self.cpush,     # 1 add constants to the stack (note LIFO)
            self.push,      # 2 copy an element to the top of the stack
            self.pop,       # 3 delete an element from the stack
            self.pull,      # 4 move an element to the top of the stack and push the rest back
            self.bury,      # 5 push the top element down the stack, pulling the rest back
            
            self.math       # 6 arithmetic
            
            self.code       # 7 add 
            self.icode      # 8
            self.ccode      # 9
            self.iccode     # A
            self.pcode      # B
            self.ipcode     # C
            self.call       # D
            self.functional # E
            
        ]
        while self.call or self.fptr < len(self.top):
            while self.fptr < len(self.top):
                byte = self.code[self.fptr]
                hi = byte >> 4
                lo = byte & 0x0F
                
            self.top, self.fptr = self.call.pop()
            self.fptr += 1
        


