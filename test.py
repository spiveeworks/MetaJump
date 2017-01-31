from examples.py import opcode
from meta_jump import *


jmp_test = [opcode.CPUSH + 1, 255, opcode.JGZ, +4, opcode.PUSH + 0, opcode.POPT + 1, opcode.JMP, -6, opcode.POP + 0]



