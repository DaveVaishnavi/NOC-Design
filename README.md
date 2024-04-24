# Network on Chip Design

This repository contains the implementation of a Network on Chip design solution for optimizing communication within a System on Chip. The solution focuses on minimizing latency, maximizing bandwidth, optimizing buffer occupancy, and minimizing throttling occurrences while meeting power constraints.

## Overview

The NOC design solution consists of several components, including scripts for measuring latency and bandwidth, utility functions for controlling buffer sizes and arbiter weights, and potentially a reinforcement learning framework for optimization. The solution aims to address the challenges of designing an efficient NOC architecture for various workloads running on the CPU and IO peripherals.

## Project Structure

- `src/`: Contains the source code for the solution.
- `tests/`: Contains test cases to ensure the correctness of the solution.
- `docs/`: Contains documentation related to the solution.
- `README.md`: Overview of the project and instructions for running the code.

## Usage

1. **Clone the repository:**
   bash
   git clone <repository-url>

2. **Install dependencies:**
  bash
  pip install -r requirements.txt

3. **Run the main script to measure latency and bandwidth:**
   bash
   python src/latency_bandwidth.py

4. **Run tests:**
   bash
   python -m unittest discover tests
