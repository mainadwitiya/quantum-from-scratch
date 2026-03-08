# Quantum From Scratch

Learning quantum computing from zero — building everything by hand before reaching for frameworks.

This is a living repository. I'm a data scientist documenting my journey from linear algebra basics to frontier quantum research. Everything is implemented in Python, tested, and explained as I go.

## The Idea

Most quantum computing tutorials jump straight to Qiskit circuits. This repo takes the long way:

1. **Build the math first** — implement matrix operations, Dirac notation, eigensolvers with numpy
2. **Understand the physics** — simulate quantum mechanics before touching quantum computing
3. **Code before frameworks** — write a circuit simulator from scratch, then use Qiskit knowing what's underneath
4. **Run on real hardware** — go from simulator to IBM quantum computers
5. **Contribute back** — ultimately contribute to open-source quantum projects

## Structure

```
phases/          6 learning phases, each with notes, exercises, and tests
projects/        Capstone project for each phase
research/        Paper summaries and reproductions
notebooks/       Jupyter scratch space
requirements/    Chained pip requirements per phase
```

## Phases

| # | Phase | What I Build |
|---|-------|-------------|
| 1 | Math & Physics Foundations | Linear algebra toolkit |
| 2 | Quantum Mechanics Core | QM simulation sandbox |
| 3 | QC Fundamentals | Circuit simulator (numpy only) |
| 4 | Quantum Algorithms | Algorithm suite + IBM hardware runs |
| 5 | Advanced + Open Source | QEC toolkit + open-source PR |
| 6 | Frontier Research | Paper reproduction + original work |

## Getting Started

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements/phase1.txt
```

Exercises are TDD-style — function stubs that raise `NotImplementedError` with tests ready to run:

```bash
cd phases/01-foundations/exercises
pytest test_complex_numbers.py -v   # all fail initially
# implement the functions, watch them go green
```

## Following Along

- **ROADMAP.md** — master checklist of every topic across all phases
- **SESSION_LOG.md** — what I learned each session, what's still unclear
- **Phase READMEs** — weekly plans and resources for each phase

If you're on a similar journey, fork it and make it yours.

## Tools

- Python 3.12, numpy, scipy, matplotlib, sympy, jupyter
- Later phases add: qutip, qiskit, pennylane, cirq
- Claude Code as AI tutor and code reviewer

## License

MIT
