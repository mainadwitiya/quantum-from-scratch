# Phase 3: Quantum Computing Fundamentals

**Duration:** 4-6 weeks
**Prerequisites:** Phase 2 (quantum mechanics)
**Capstone:** circuit-engine — Quantum circuit simulator from scratch (numpy only)

## Objectives

By the end of this phase, you will:
- Represent qubits on the Bloch sphere and manipulate them with gates
- Build quantum circuits from universal gate sets
- Implement quantum teleportation and superdense coding
- Use Qiskit for circuit construction and simulation
- Build a circuit simulator from scratch using only numpy

## Weekly Plan

### Week 1: Qubits & Single-Qubit Gates
- Qubit as unit vector in C^2
- Bloch sphere representation
- Pauli gates (X, Y, Z), Hadamard, phase gates (S, T)
- Rotation gates (Rx, Ry, Rz)
- Exercises: visualize gate actions on Bloch sphere

### Week 2: Multi-Qubit Gates & Circuits
- Tensor product for multi-qubit states
- CNOT, Toffoli, SWAP gates
- Controlled-U gates
- Universal gate sets
- Circuit model of computation
- Exercises: build circuits, compute output states by hand and code

### Week 3: Quantum Protocols
- Quantum teleportation (implement step by step)
- Superdense coding
- BB84 quantum key distribution
- Bell inequality and CHSH game
- Exercises: full protocol implementations

### Week 4: Qiskit Introduction
- Circuit construction and visualization
- Statevector and Qasm simulators
- Measurement and shot statistics
- Exercises: recreate hand-built circuits in Qiskit

### Weeks 5-6: Capstone Project
- Build circuit-engine from scratch (numpy only)
- Support: arbitrary single-qubit gates, CNOT, measurement
- Statevector simulation
- Test against Qiskit results

## Resources

- *Quantum Computation and Quantum Information* — Nielsen & Chuang (Ch. 1, 4)
- Qiskit Textbook (online)
- *Programming Quantum Computers* — Johnston, Harrigan, Gimeno-Segovia
