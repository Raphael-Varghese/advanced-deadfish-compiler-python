import sys
import random

class Program:
    # Instructions
    I_INC = 'i'
    I_DEC = 'd'
    I_SQR = 's'
    I_OUT = 'o'
    I_OCH = '*'
    I_SDE = '\\'
    I_DBL = 'b'
    I_NEG = '!'
    I_MOD = 'm'
    I_RND = 'r'
    I_NL  = ':'
    I_LOOP_START = '['
    I_LOOP_END = ']'

    def __init__(self, data, debug=False):
        self.accumulator = 0
        self.data = data
        self.debug = debug
        self.pointer = 0

    def CheckOverflow(self):
        if self.accumulator == 256 or self.accumulator == -1:
            self.accumulator = 0

    def Run(self):
        while self.pointer < len(self.data):
            curr = self.data[self.pointer].lower()
            if self.debug:
                print(f"[{self.pointer}] Instruction: {curr}, Accumulator: {self.accumulator}")
            if curr == Program.I_INC:
                self.accumulator += 1
            elif curr == Program.I_DEC:
                self.accumulator -= 1
            elif curr == Program.I_SQR:
                self.accumulator **= 2
            elif curr == Program.I_OUT:
                print(self.accumulator, end='')
            elif curr == Program.I_OCH:
                print(chr(self.accumulator), end='')
            elif curr == Program.I_SDE:
                self.accumulator = 0
            elif curr == Program.I_DBL:
                self.accumulator *= 2
            elif curr == Program.I_NEG:
                self.accumulator *= -1
            elif curr == Program.I_MOD:
                self.accumulator %= 10
            elif curr == Program.I_RND:
                self.accumulator = random.randint(0, 255)
            elif curr == Program.I_NL:
                print()
            elif curr == Program.I_LOOP_START:
                loop_start = self.pointer + 1
                loop_end = self.find_loop_end(loop_start)
                loop_code = self.data[loop_start:loop_end]
                for _ in range(self.accumulator):
                    Program(loop_code, self.debug).Run()
                self.pointer = loop_end
            else:
                if self.debug:
                    print(f"Unknown instruction: {curr}")
            self.CheckOverflow()
            self.pointer += 1

    def find_loop_end(self, start):
        depth = 1
        for i in range(start, len(self.data)):
            if self.data[i] == Program.I_LOOP_START:
                depth += 1
            elif self.data[i] == Program.I_LOOP_END:
                depth -= 1
                if depth == 0:
                    return i
        raise Exception("Unmatched loop brackets")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python advanced_deadfish.py <filename> [--debug]")
        sys.exit(1)

    filename = sys.argv[1]
    debug = '--debug' in sys.argv

    try:
        with open(filename, 'r') as f:
            code = f.read()
        Program(code, debug).Run()
    except FileNotFoundError:
        print("Error: File not found.")
