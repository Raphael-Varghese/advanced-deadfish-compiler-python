import sys
import random

class Program:
    # Instruction set
    INSTRUCTIONS = {
        'i': 'Increment',
        'd': 'Decrement',
        's': 'Square',
        'o': 'Output',
        '*': 'OutputASCII',
        '\\': 'Clear',
        'b': 'Double',
        '!': 'Negate',
        'm': 'Modulo10',
        'r': 'Randomize',
        ':': 'Newline',
        '?': 'Input',
        '[': 'LoopStart',
        ']': 'LoopEnd'
    }

    def __init__(self, data, debug=False, overflow_limit=256):
        self.accumulator = 0
        self.data = data
        self.debug = debug
        self.pointer = 0
        self.overflow_limit = overflow_limit
        self.loop_stack = []

    def check_overflow(self):
        if self.accumulator >= self.overflow_limit or self.accumulator < 0:
            if self.debug:
                print(f"⚠️ Overflow triggered. Resetting accumulator.")
            self.accumulator = 0

    def run(self):
        while self.pointer < len(self.data):
            curr = self.data[self.pointer].lower()
            if self.debug:
                print(f"[{self.pointer}] Instruction: '{curr}' | Accumulator: {self.accumulator}")
            self.execute(curr)
            self.check_overflow()
            self.pointer += 1

    def execute(self, instr):
        if instr == 'i':
            self.accumulator += 1
        elif instr == 'd':
            self.accumulator -= 1
        elif instr == 's':
            self.accumulator **= 2
        elif instr == 'o':
            print(self.accumulator, end='')
        elif instr == '*':
            try:
                print(chr(self.accumulator), end='')
            except ValueError:
                print("�", end='')  # Invalid ASCII
        elif instr == '\\':
            self.accumulator = 0
        elif instr == 'b':
            self.accumulator *= 2
        elif instr == '!':
            self.accumulator *= -1
        elif instr == 'm':
            self.accumulator %= 10
        elif instr == 'r':
            self.accumulator = random.randint(0, self.overflow_limit - 1)
        elif instr == ':':
            print()
        elif instr == '?':
            try:
                user_input = input("🔢 Enter a number: ")
                self.accumulator = int(user_input)
            except ValueError:
                print("⚠️ Invalid input. Accumulator set to 0.")
                self.accumulator = 0
        elif instr == '[':
            loop_start = self.pointer + 1
            loop_end = self.find_loop_end(loop_start)
            loop_code = self.data[loop_start:loop_end]
            if self.debug:
                print(f"🔁 Looping {self.accumulator} times from [{loop_start} to {loop_end}]")
            for _ in range(self.accumulator):
                Program(loop_code, self.debug, self.overflow_limit).run()
            self.pointer = loop_end
        elif instr == ']':
            pass  # Handled by loop logic
        else:
            if self.debug:
                print(f"⚠️ Unknown instruction: '{instr}'")

    def find_loop_end(self, start):
        depth = 1
        for i in range(start, len(self.data)):
            if self.data[i] == '[':
                depth += 1
            elif self.data[i] == ']':
                depth -= 1
                if depth == 0:
                    return i
        raise Exception("❌ Unmatched loop brackets")

def print_help():
    print("\n🧠 Deadfish++ Compiler")
    print("Usage:")
    print("  python advanced_deadfish.py <filename> [--debug] [--limit=N]")
    print("\nOptions:")
    print("  --debug       Enable verbose debug mode")
    print("  --limit=N     Set custom overflow limit (default: 256)")
    print("  --help        Show this help message\n")

if __name__ == '__main__':
    if '--help' in sys.argv or len(sys.argv) < 2:
        print_help()
        sys.exit(0)

    filename = sys.argv[1]
    debug = '--debug' in sys.argv
    limit = 256

    for arg in sys.argv:
        if arg.startswith('--limit='):
            try:
                limit = int(arg.split('=')[1])
            except ValueError:
                print("⚠️ Invalid overflow limit. Using default (256).")

    try:
        with open(filename, 'r') as f:
            code = f.read()
        Program(code, debug, limit).run()
    except FileNotFoundError:
        print("❌ Error: File not found.")
