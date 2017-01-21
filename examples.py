
class opcode:
    NOP = 0x00
    JPOP = 0x08  # the best kind of pop
    JEZ = 0x01
    JGZ = 0x02
    JLZ = 0x04
    JMP = 0x07

    CPUSH = 0x10
    PUSH = 0x20
    POP = 0x30
    PULL = 0x40
    BURY = 0x50

    MATH = 0x60
    ADD = 0x60
    SUB = 0x61
    MUL = 0x62
    DIV = 0x63
    MOD = 0x64
    DIVMOD = 0x65
    OR = 0x66
    AND = 0x67
    XOR = 0x68
    RSHIFT = 0x69
    LSHIFT = 0x6A
    INC = 0x6B
    DEC = 0x6C
    COMP = 0x6D
    NEG = 0x6E
    NOT = 0x6F


    CALL = 0x70
    CCODE = 0x80
    RCCODE = 0x90
    CODE = 0xA0
    RCODE = 0xB0

    LO = 0xC0
    RET = 0xC0
    PCALL = 0xC1
    CCALL = 0xC2
    FLUSH = 0xC3
    RFLUSH = 0xC4
    THIS = 0xC5
    TCALL = 0xC6
    OTCALL = 0xC57

    IPT = 0xD0
    COPT = 0xE0
    POPT = 0xF0

HELLO_WORLD = [opcode.COPT + len("Hello, World!")] + [ord(x) for x in "Hello, World!"]

GEN = [opcode.THIS, opcode.CPUSH + 1, 0]  # def gen(): return (gen, 0)

POP_TO_RREG = [opcode.RCODE, opcode.RCCODE + 1, opcode.CPUSH + 1]
def tuple(n): return [opcode.CCODE + 2, opcode.CPUSH, n, opcode.RCODE, n, opcode.FLUSH]
  # def n-tuple(a1, a2, a3... an):
  #     def inner():
  #         return (a1, a2, a3... an)
  #     return inner


