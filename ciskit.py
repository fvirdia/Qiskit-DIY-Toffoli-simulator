"""
Run tests by calling: python3 -m doctest -v -o ELLIPSIS ciskit.py
"""


import qiskit


class QuantumCircuit:

    def __init__(self, q_registers, c_registers=0):

        self.q_registers, self.c_registers = q_registers, c_registers

        if self.c_registers > 0:
            self.circ = qiskit.QuantumCircuit(self.q_registers, self.c_registers)
        else:
            self.circ = qiskit.QuantumCircuit(self.q_registers)

        self.listing = []

    def x(self, y, quantum=True, register=[]):
        """
        TEST:
            >>> c = QuantumCircuit(1)
            >>> c.x(0)
            <qiskit.circuit.instructionset.InstructionSet ...
            >>> c.classical_run([False])
            ([True], [])
            >>> c.classical_run([True])
            ([False], [])
        """
        if quantum:
            self.listing.append(('x', (y,)))
            return self.circ.x(y)
        else:
            return (not register[y],)

    def h(self, x, quantum=True, register=[]):
        if quantum:
            self.listing.append(('h', (x,)))
            return self.circ.h(x)
        else:
            raise ValueError("Can't simulate H classically")

    def cx(self, x, y, quantum=True, register=[]):
        """
        TEST:
            >>> c = QuantumCircuit(2)
            >>> c.cx(0, 1)
            <qiskit.circuit.instructionset.InstructionSet ...
            >>> c.classical_run([False, False])
            ([False, False], [])
            >>> c.classical_run([False, True])
            ([False, True], [])
            >>> c.classical_run([True, False])
            ([True, True], [])
            >>> c.classical_run([True, True])
            ([True, False], [])
        """
        if quantum:
            self.listing.append(('cx', (x, y)))
            return self.circ.cx(x, y)
        else:
            return (register[x], register[x] ^ register[y])

    def ccx(self, x, y, z, quantum=True, register=[]):
        """
        TEST:
            >>> c = QuantumCircuit(3)
            >>> c.ccx(0, 1, 2)
            <qiskit.circuit.instructionset.InstructionSet ...
            >>> c.classical_run([False, False, False])
            ([False, False, False], [])
            >>> c.classical_run([False, False, True])
            ([False, False, True], [])
            >>> c.classical_run([False, True, False])
            ([False, True, False], [])
            >>> c.classical_run([False, True, True])
            ([False, True, True], [])
            >>> c.classical_run([True, False, False])
            ([True, False, False], [])
            >>> c.classical_run([True, False, True])
            ([True, False, True], [])
            >>> c.classical_run([True, True, False])
            ([True, True, True], [])
            >>> c.classical_run([True, True, True])
            ([True, True, False], [])
        """
        if quantum:
            self.listing.append(('ccx', (x, y, z)))
            return self.circ.ccx(x, y, z)
        else:
            return (register[x], register[y], (register[x] & register[y]) ^ register[z])

    def swap(self, x, y, quantum=True, register=[]):
        """
        TEST:
            >>> c = QuantumCircuit(2)
            >>> c.swap(0, 1)
            <qiskit.circuit.instructionset.InstructionSet ...
            >>> c.classical_run([False, False])
            ([False, False], [])
            >>> c.classical_run([False, True])
            ([True, False], [])
            >>> c.classical_run([True, False])
            ([False, True], [])
            >>> c.classical_run([True, True])
            ([True, True], [])
        """
        if quantum:
            self.listing.append(('swap', (x, y)))
            return self.circ.swap(x, y)
        else:
            return (register[y], register[x])

    def draw(self, **kwargs):
        return self.circ.draw(**kwargs)

    def classical_run(self, q_input, c_input=[], verbose=False):
        if len(q_input) != self.q_registers:
            raise ValueError("Not enough input qubits provided")
        if len(c_input) != self.c_registers:
            raise ValueError("Not enough input bits provided")

        q_regs = q_input[::]
        c_regs = c_input[::]

        if verbose:
            print(f"intput: {q_regs}, {c_regs}")

        for instruction in self.listing:
            op, regs = instruction
            if verbose:
                print(f"status: {q_regs}, {c_regs}")
                print(f"{op}: {regs}", end="")
            out = getattr(self, op)(*regs, quantum=False, register=q_regs)
            if verbose:
                print(f" -> {out}")
            for _ in range(len(regs)):
                q_regs[regs[_]] = out[_]
        return q_regs, c_regs
