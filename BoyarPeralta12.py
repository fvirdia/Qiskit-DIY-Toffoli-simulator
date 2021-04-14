# https://www.nist.gov/publications/depth-16-circuit-aes-s-box

from ciskit import QuantumCircuit
from QUtilities import *


def ForwardSBox(circ, u, s, t, m, l, costing=False):
        LPXOR(circ, u[0], u[3], t[1-1])
        LPXOR(circ, u[0], u[5], t[2-1])
        LPXOR(circ, u[0], u[6], t[3-1])
        LPXOR(circ, u[3], u[5], t[4-1])
        LPXOR(circ, u[4], u[6], t[5-1])
        LPXOR(circ, t[1-1], t[5-1], t[6-1])
        LPXOR(circ, u[1], u[2], t[7-1])
        LPXOR(circ, u[7], t[6-1], t[8-1])
        LPXOR(circ, u[7], t[7-1], t[9-1])
        LPXOR(circ, t[6-1], t[7-1], t[10-1])
        LPXOR(circ, u[1], u[5], t[11-1])
        LPXOR(circ, u[2], u[5], t[12-1])
        LPXOR(circ, t[3-1], t[4-1], t[13-1])
        LPXOR(circ, t[6-1], t[11-1], t[14-1])
        LPXOR(circ, t[5-1], t[11-1], t[15-1])
        LPXOR(circ, t[5-1], t[12-1], t[16-1])
        LPXOR(circ, t[9-1], t[16-1], t[17-1])
        LPXOR(circ, u[3], u[7], t[18-1])
        LPXOR(circ, t[7-1], t[18-1], t[19-1])
        LPXOR(circ, t[1-1], t[19-1], t[20-1])
        LPXOR(circ, u[6], u[7], t[21-1])
        LPXOR(circ, t[7-1], t[21-1], t[22-1])
        LPXOR(circ, t[2-1], t[22-1], t[23-1])
        LPXOR(circ, t[2-1], t[10-1], t[24-1])
        LPXOR(circ, t[20-1], t[17-1], t[25-1])
        LPXOR(circ, t[3-1], t[16-1], t[26-1])
        LPXOR(circ, t[1-1], t[12-1], t[27-1])

        LPAND(circ, t[13-1], t[6-1], m[1-1], costing)
        LPAND(circ, t[23-1], t[8-1], m[2-1], costing)
        LPXOR(circ, t[14-1], m[1-1], m[3-1])
        LPAND(circ, t[19-1], u[7], m[4-1], costing)
        LPXOR(circ, m[4-1], m[1-1], m[5-1])
        LPAND(circ, t[3-1], t[16-1], m[6-1], costing)
        LPAND(circ, t[22-1], t[9-1], m[7-1], costing)
        LPXOR(circ, t[26-1], m[6-1], m[8-1])
        LPAND(circ, t[20-1], t[17-1], m[9-1], costing)
        LPXOR(circ, m[9-1], m[6-1], m[10-1])
        LPAND(circ, t[1-1], t[15-1], m[11-1], costing)
        LPAND(circ, t[4-1], t[27-1], m[12-1], costing)
        LPXOR(circ, m[12-1], m[11-1], m[13-1])
        LPAND(circ, t[2-1], t[10-1], m[14-1], costing)
        LPXOR(circ, m[14-1], m[11-1], m[15-1])
        LPXOR(circ, m[3-1], m[2-1], m[16-1])
        LPXOR(circ, m[5-1], t[24-1], m[17-1])
        LPXOR(circ, m[8-1], m[7-1], m[18-1])
        LPXOR(circ, m[10-1], m[15-1], m[19-1])
        LPXOR(circ, m[16-1], m[13-1], m[20-1])
        LPXOR(circ, m[17-1], m[15-1], m[21-1])
        LPXOR(circ, m[18-1], m[13-1], m[22-1])
        LPXOR(circ, m[19-1], t[25-1], m[23-1])
        LPXOR(circ, m[22-1], m[23-1], m[24-1])
        LPAND(circ, m[22-1], m[20-1], m[25-1], costing)
        LPXOR(circ, m[21-1], m[25-1], m[26-1])
        LPXOR(circ, m[20-1], m[21-1], m[27-1])
        LPXOR(circ, m[23-1], m[25-1], m[28-1])
        LPAND(circ, m[28-1], m[27-1], m[29-1], costing)
        LPAND(circ, m[26-1], m[24-1], m[30-1], costing)
        LPAND(circ, m[20-1], m[23-1], m[31-1], costing)
        LPAND(circ, m[27-1], m[31-1], m[32-1], costing)
        LPXOR(circ, m[27-1], m[25-1], m[33-1])
        LPAND(circ, m[21-1], m[22-1], m[34-1], costing)
        LPAND(circ, m[24-1], m[34-1], m[35-1], costing)
        LPXOR(circ, m[24-1], m[25-1], m[36-1])
        LPXOR(circ, m[21-1], m[29-1], m[37-1])
        LPXOR(circ, m[32-1], m[33-1], m[38-1])
        LPXOR(circ, m[23-1], m[30-1], m[39-1])
        LPXOR(circ, m[35-1], m[36-1], m[40-1])
        LPXOR(circ, m[38-1], m[40-1], m[41-1])
        LPXOR(circ, m[37-1], m[39-1], m[42-1])
        LPXOR(circ, m[37-1], m[38-1], m[43-1])
        LPXOR(circ, m[39-1], m[40-1], m[44-1])
        LPXOR(circ, m[42-1], m[41-1], m[45-1])
        LPAND(circ, m[44-1], t[6-1], m[46-1], costing)
        LPAND(circ, m[40-1], t[8-1], m[47-1], costing)
        LPAND(circ, m[39-1], u[7], m[48-1], costing)
        LPAND(circ, m[43-1], t[16-1], m[49-1], costing)
        LPAND(circ, m[38-1], t[9-1], m[50-1], costing)
        LPAND(circ, m[37-1], t[17-1], m[51-1], costing)
        LPAND(circ, m[42-1], t[15-1], m[52-1], costing)
        LPAND(circ, m[45-1], t[27-1], m[53-1], costing)
        LPAND(circ, m[41-1], t[10-1], m[54-1], costing)
        LPAND(circ, m[44-1], t[13-1], m[55-1], costing)
        LPAND(circ, m[40-1], t[23-1], m[56-1], costing)
        LPAND(circ, m[39-1], t[19-1], m[57-1], costing)
        LPAND(circ, m[43-1], t[3-1], m[58-1], costing)
        LPAND(circ, m[38-1], t[22-1], m[59-1], costing)
        LPAND(circ, m[37-1], t[20-1], m[60-1], costing)
        LPAND(circ, m[42-1], t[1-1], m[61-1], costing)
        LPAND(circ, m[45-1], t[4-1], m[62-1], costing)
        LPAND(circ, m[41-1], t[2-1], m[63-1], costing)

        LPXOR(circ, m[61-1], m[62-1], l[0])
        LPXOR(circ, m[50-1], m[56-1], l[1])
        LPXOR(circ, m[46-1], m[48-1], l[2])
        LPXOR(circ, m[47-1], m[55-1], l[3])
        LPXOR(circ, m[54-1], m[58-1], l[4])
        LPXOR(circ, m[49-1], m[61-1], l[5])
        LPXOR(circ, m[62-1], l[5], l[6])
        LPXOR(circ, m[46-1], l[3], l[7])
        LPXOR(circ, m[51-1], m[59-1], l[8])
        LPXOR(circ, m[52-1], m[53-1], l[9])
        LPXOR(circ, m[53-1], l[4], l[10])
        LPXOR(circ, m[60-1], l[2], l[11])
        LPXOR(circ, m[48-1], m[51-1], l[12])
        LPXOR(circ, m[50-1], l[0], l[13])
        LPXOR(circ, m[52-1], m[61-1], l[14])
        LPXOR(circ, m[55-1], l[1], l[15])
        LPXOR(circ, m[56-1], l[0], l[16])
        LPXOR(circ, m[57-1], l[1], l[17])
        LPXOR(circ, m[58-1], l[8], l[18])
        LPXOR(circ, m[63-1], l[4], l[19])
        LPXOR(circ, l[0], l[1], l[20])
        LPXOR(circ, l[1], l[7], l[21])
        LPXOR(circ, l[3], l[12], l[22])
        LPXOR(circ, l[18], l[2], l[23])
        LPXOR(circ, l[15], l[9], l[24])
        LPXOR(circ, l[6], l[10], l[25])
        LPXOR(circ, l[7], l[9], l[26])
        LPXOR(circ, l[8], l[10], l[27])
        LPXOR(circ, l[11], l[14], l[28])
        LPXOR(circ, l[11], l[17], l[29])


def SBox(circ, q_input, q_output, costing=False):

    u = q_input[::-1]
    s = q_output[::-1]
    t = range(16, 16+27)
    m = range(16+27, 16+27+63)
    l = range(16+27+63, 16+27+63+30)

    ForwardSBox(circ, u, s, t, m, l, costing)

    # get out result
    LPXOR(circ, l[6], l[24], s[0])
    LPXNOR(circ, l[16], l[26], s[1])
    LPXNOR(circ, l[19], l[28], s[2])
    LPXOR(circ, l[6], l[21], s[3])
    LPXOR(circ, l[20], l[22], s[4])
    LPXOR(circ, l[25], l[29], s[5])
    LPXNOR(circ, l[13], l[27], s[6])
    LPXNOR(circ, l[6], l[23], s[7])

    # uncompute -- need to implement feature similar to "Adjoint" in Q#
    # (Adjoint ForwardSBox)(u, s, t, m, l, costing);


def main():
    c = QuantumCircuit(16+27+63+30)
    SBox(c, range(8), range(8, 16))

    import aes
    from gf256 import GF256Element
    for _x in range(256):
        # using aes from the Q# paper
        x = GF256Element(_x)
        sbox = GF256Element(aes.SBox(x))
        # print(list(x), " -> ", list(sbox))

        # using partial qiskit Sbox
        input_byte = list(map(bool, list(x)))
        output_register = c.classical_run(input_byte + [False] * (16+27+63+30-8))
        output_byte = list(map(int, output_register[0][8:16]))
        # print(list(x), " -> ", output_byte)
        # print()
        # print(output_register)
        # print(output_byte)
        assert(list(sbox) == output_byte)

    c.draw(filename="sbox.txt")

    print(":)")

    return c

main()