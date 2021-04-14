

def SWAP(circ, x, y):
    circ.swap(x, y)


def SWAPBytes(circ, x, y):
    for i in range(8):
        SWAP(circ, x[i], y[i])


def CNOTnBits(circ, x, y, n):
    for i in range(n):
        circ.cx(x[i], y[i])


def CNOTBytes(circ, x, y):
    CNOTnBits(circ, x, y, 8)


def REWIRE(circ, x, y, costing=False):
    if not costing:
        SWAP(circ, x, y)


def REWIREBytes(circ, x, y, costing=False):
    if not costing:
        SWAPBytes(circ, x, y)


def LPXOR(circ, in_1, in_2, outp):
    """
         assumes output qubit set to Zero
         linear-program xor equivalent to
         bool outp = 0
         outp = in_1 ^ in_2
    """
    circ.cx(in_1, outp)
    circ.cx(in_2, outp)


def LPXNOR(circ, in_1, in_2, outp):
    """ assumes outp = 0
    """
    LPXOR(circ, in_1, in_2, outp)
    circ.x(outp)


def LPAND(circ, in_1, in_2, outp, costing=False):
    if costing:
        # our and
        raise NotImplementedError("can we do semiclassical?")
    else:
        circ.ccx(in_1, in_2, outp)

