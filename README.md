# Prime Number Generator

A Python project to generate prime numbers of a specified bit length using the **Miller-Rabin Primality Test**. This script provides a simple implementation of probabilistic prime generation suitable for cryptographic purposes.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Limitations](#limitations)
- [License](#license)

## Overview
This project generates prime numbers of a given bit size by repeatedly testing randomly generated numbers using the Miller-Rabin Primality Test. It ensures a high probability of correctness by running multiple tests for each candidate.

## Features
- Generates prime numbers of arbitrary bit lengths.
- Uses the Miller-Rabin test to ensure probable primality.
- Efficiently computes large prime numbers with a high degree of certainty.

## Requirements
- Python 3.x

No additional libraries are required, only standard Python modules are used.

## Usage
1. Clone this repository.
2. Run the script with Python:
```bash
python generatore_primi.py
```
3. Enter the desired bit length for the prime number when prompted.

## How It Works
- **Fast Exponentiation**: An optimized method for calculating `(a^e) % n`.
- **Miller-Rabin Test**: A probabilistic algorithm to check if a number is prime by repeatedly testing it against random bases.
- **Prime Generation**: Repeatedly generates random numbers of the specified bit size and tests them until a prime is found.


