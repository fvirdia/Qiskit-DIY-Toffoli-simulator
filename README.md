# Qiskit-DIY-Toffoli-simulator

DIY implementation of the Q# ToffoliSimulator functionality in Qiskit, and application to the AES S-box.

The project is inspired by https://github.com/microsoft/grover-blocks, an implementation of AES and LowMC using the Q# pogramming language.

We implement a `QuantumCircuit` class that keeps track of quantum gates applied to a state. If these consists only of `X`, `CNOT`, `CCNOT` gates and rewiring, the class allows running the circuit on classical inputs. We use this to implement the "forward" component of the AES S-box (cf. [JNRV20]), unit-test it and generate a text diagram of its circuit.

## Dependencies

- Python 3
- Qiskit 0.17.0+

The implementation of arithmetic in GF(256), of AES and of the Boyar and Peralta S-box are taken from https://github.com/microsoft/grover-blocks.

## Instructions

Run

```
python3 BoyarPeralta12.py
```

to silently test the S-box and to save the diagram to a local text file.

## References

[JNRV20] Samuel Jaques, Michael Naehrig, Martin Roetteler, and Fernando Virdia, "Implementing Grover oracles for quantum key search on AES and LowMC". Preprint available at https://eprint.iacr.org/2019/1146.