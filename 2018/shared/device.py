class Device:
    """Object representing the Wrist Device."""

    def __init__(self, registers=[0 for _ in range(6)], instruction_register=0):
        super(Device, self).__init__()
        self.registers = registers
        self.instruction_pointer = 0
        self.instruction_register = instruction_register
        self.opcodes = {x: None for x in range(16)}
        self.opcode_names = {
            "addr": self.addr,
            "addi": self.addi,
            "mulr": self.mulr,
            "muli": self.muli,
            "banr": self.banr,
            "bani": self.bani,
            "borr": self.borr,
            "bori": self.bori,
            "setr": self.setr,
            "seti": self.seti,
            "gtir": self.gtir,
            "gtri": self.gtri,
            "gtrr": self.gtrr,
            "eqir": self.eqir,
            "eqri": self.eqri,
            "eqrr": self.eqrr,
        }

    def addr(self, reg_a, reg_b, reg_c):
        """stores into reg C the result of adding reg A and reg B"""
        self.registers[reg_c] = self.registers[reg_a] + self.registers[reg_b]

    def addi(self, reg_a, val_b, reg_c):
        """stores into reg C the result of adding reg A and value B"""
        self.registers[reg_c] = self.registers[reg_a] + val_b

    def mulr(self, reg_a, reg_b, reg_c):
        """stores into reg C the result of multiplying reg A and reg B"""
        self.registers[reg_c] = self.registers[reg_a] * self.registers[reg_b]

    def muli(self, reg_a, val_b, reg_c):
        """stores into reg C the result of multiplying reg A and value B"""
        self.registers[reg_c] = self.registers[reg_a] * val_b

    def banr(self, reg_a, reg_b, reg_c):
        """stores into reg C the result of bitwise AND of reg A and reg B"""
        self.registers[reg_c] = self.registers[reg_a] & self.registers[reg_b]

    def bani(self, reg_a, val_b, reg_c):
        """stores into reg C the result of bitwise AND of reg A and value B"""
        self.registers[reg_c] = self.registers[reg_a] & val_b

    def borr(self, reg_a, reg_b, reg_c):
        """stores into reg C the result of bitwise OR of reg A and reg B"""
        self.registers[reg_c] = self.registers[reg_a] | self.registers[reg_b]

    def bori(self, reg_a, val_b, reg_c):
        """stores into reg C the result of bitwise OR of reg A and value B"""
        self.registers[reg_c] = self.registers[reg_a] | val_b

    def setr(self, reg_a, _, reg_c):
        """copies the contents of reg A into reg C. B is ignored."""
        self.registers[reg_c] = self.registers[reg_a]

    def seti(self, val_a, _, reg_c):
        """copies the contents of reg A into reg C. B is ignored."""
        self.registers[reg_c] = val_a

    def gtir(self, val_a, reg_b, reg_c):
        """Sets reg C to 1 if value A is > than reg B. Otherwise, reg C is set to 0."""
        if val_a > self.registers[reg_b]:
            self.registers[reg_c] = 1
        else:
            self.registers[reg_c] = 0

    def gtri(self, reg_a, val_b, reg_c):
        """Sets reg C to 1 if reg A is > than value B. Otherwise, reg C is set to 0."""
        if self.registers[reg_a] > val_b:
            self.registers[reg_c] = 1
        else:
            self.registers[reg_c] = 0

    def gtrr(self, reg_a, reg_b, reg_c):
        """Sets reg C to 1 if reg A is > than reg B. Otherwise, reg C is set to 0."""
        if self.registers[reg_a] > self.registers[reg_b]:
            self.registers[reg_c] = 1
        else:
            self.registers[reg_c] = 0

    def eqir(self, val_a, reg_b, reg_c):
        """Sets reg C to 1 if value A is = to reg B. Otherwise, reg C is set to 0."""
        if val_a == self.registers[reg_b]:
            self.registers[reg_c] = 1
        else:
            self.registers[reg_c] = 0

    def eqri(self, reg_a, val_b, reg_c):
        """Sets reg C to 1 if reg A is = to value B. Otherwise, reg C is set to 0."""
        if self.registers[reg_a] == val_b:
            self.registers[reg_c] = 1
        else:
            self.registers[reg_c] = 0

    def eqrr(self, reg_a, reg_b, reg_c):
        """Sets reg C to 1 if reg A is = to reg B. Otherwise, reg C is set to 0."""
        if self.registers[reg_a] == self.registers[reg_b]:
            self.registers[reg_c] = 1
        else:
            self.registers[reg_c] = 0

    def run_program(self, program):
        """Run the program with the current opcodes."""
        for line in program:
            self.opcodes[int(line[0])](int(line[1]), int(line[2]), int(line[3]))

    def run_program_with_flow_control(self, program):
        """Run the program with the current opcodes."""
        while 0 <= self.instruction_pointer < len(program):
            self.registers[self.instruction_register] = self.instruction_pointer
            line = program[self.instruction_pointer]
            self.opcode_names[line[0]](int(line[1]), int(line[2]), int(line[3]))
            self.instruction_pointer = self.registers[self.instruction_register] + 1

    def __str__(self):
        return f"IP: {self.instruction_pointer} Registers: {self.registers}"
