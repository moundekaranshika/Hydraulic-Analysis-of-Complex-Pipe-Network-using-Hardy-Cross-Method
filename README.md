# Hydraulic Analysis of Complex Pipe Network using Hardy Cross Method

##  Project Overview

This project implements the **Hardy Cross method** to determine flow distribution in a complex interconnected pipe network.

The Hardy Cross method is an iterative technique used to analyse pipe networks containing multiple branches and closed loops. The method begins with an initial estimate of flow in each pipe and progressively applies flow corrections to satisfy the **energy/head-loss balance around each closed loop**.

In this project, a Python-based solver was developed for a **22-pipe network containing 7 interconnected loops**. The program calculates the flow rate in each pipe branch through iterative loop corrections until the solution converges.

---

##  Objectives

* Develop a computational implementation of the **Hardy Cross method**.
* Analyse flow distribution in a complex pipe network with multiple interconnected loops.
* Define initial flow rates while satisfying overall network continuity.
* Calculate head losses for individual pipe branches.
* Apply iterative loop-flow corrections.
* Determine converged flow rates in all pipe branches.
* Verify convergence of the numerical solution.

---

##  Network Configuration

The analysed network consists of:

* **22 pipe branches**
* **7 closed loops**
* Multiple input and output discharges
* Known resistance coefficients for individual pipe branches

The network was represented by defining each loop through its corresponding pipe branches and flow directions.

The project diagram shows the complete 22-pipe network and its seven interconnected loops.

---

##  Methodology

The solution follows the standard iterative Hardy Cross procedure.

### Step 1 — Define Network Inputs

The input and output discharges are specified while maintaining overall flow continuity:

[
a+b+c=d+e
]

Initial flow rates are assigned to the individual pipe branches.

### Step 2 — Define Pipe Resistance

Each pipe is assigned a resistance coefficient (K).

For the implemented network, resistance values are provided for all 22 pipe branches.

### Step 3 — Define Closed Loops

Each of the seven loops is represented by:

* Pipe numbers belonging to the loop
* Direction of each pipe relative to the loop

A direction of:

* `+1` represents flow in the same direction as the selected loop direction.
* `-1` represents flow opposite to the selected loop direction.

### Step 4 — Calculate Head Loss

For each pipe, the head-loss relationship used in the implementation is:

[
h_f = KQ^2
]

where:

* (h_f) = head loss
* (K) = pipe resistance coefficient
* (Q) = flow rate

The signed head losses are summed around each loop.

### Step 5 — Calculate Loop Correction

The Hardy Cross correction is calculated as:

[
\Delta Q =
-\frac{\sum KQ^2}
{\sum 2KQ}
]

with the appropriate flow directions applied.

### Step 6 — Update Flow Rates

The calculated correction is applied to every pipe belonging to the corresponding loop:

[
Q_{new}=Q_{old}+\Delta Q
]

with the sign determined by the pipe's direction relative to the loop.

### Step 7 — Check Convergence

The largest absolute correction in each iteration is monitored.

The solution is considered converged when:

[
|\Delta Q| < 0.0001
]

The implementation uses a maximum of 10 iterations.

---

##  Implementation

### Technology

* **Language:** Python
* **Library:** NumPy
* **Method:** Hardy Cross iterative method

### Main Components

The program contains:

```text
Input flow rates
      ↓
Initial flow estimation
      ↓
Pipe resistance definition
      ↓
Loop and flow-direction definition
      ↓
Calculate loop head losses
      ↓
Calculate Hardy Cross correction
      ↓
Update pipe flows
      ↓
Check convergence
      ↓
Final flow rates
```

---

##  Project Structure

```text
Hydraulic-Analysis-Hardy-Cross/
│
├── hardy_cross.py
├── README.md
└── network_diagram.png
```

> Rename the Python file and image above according to the actual filenames in your repository.

---

##  How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Hydraulic-Analysis-Hardy-Cross
```

### 2. Install the required dependency

```bash
pip install numpy
```

### 3. Run the program

```bash
python hardy_cross.py
```

### 4. Enter the network discharges

The program accepts the input and output discharge values in the following order:

```text
a b c d e
```

The values must satisfy:

[
a+b+c=d+e
]

---

##  Output

After convergence, the program reports the final flow rate through each pipe branch:

```text
Converged after N iterations.

Final flow rates in each pipe:
Pipe 1: ...
Pipe 2: ...
Pipe 3: ...
...
Pipe 22: ...
```

The implementation tracks the maximum correction during each iteration and stops when the specified convergence tolerance is reached.

---

##  Key Engineering Concepts

This project demonstrates practical application of:

* Fluid Mechanics
* Pipe Flow Analysis
* Hydraulic Networks
* Head Loss
* Flow Continuity
* Energy Conservation
* Iterative Numerical Methods
* Hardy Cross Method
* Computational Engineering
* Python-based Engineering Analysis

---

##  Industrial Relevance

The analysis of interconnected pipe networks is relevant to systems involving:

* Industrial water distribution
* Petroleum-product pipelines
* Refinery utility networks
* Pumping systems
* Process-fluid distribution
* Industrial cooling systems

For petroleum and refinery applications, hydraulic network analysis can help engineers understand **flow distribution, pressure/head losses and pumping requirements** across interconnected pipelines.

---

##  Possible Extensions

The current implementation can be extended by incorporating:

* Darcy-Weisbach equation
* Colebrook equation for friction-factor calculation
* Pipe diameter and length as direct inputs
* Reynolds-number-based flow-regime analysis
* Pressure distribution across nodes
* Pump characteristics
* Minor losses from valves and fittings
* Different resistance coefficients for each pipe
* Automated network visualisation
* Larger networks with additional branches and loops
* Comparison with other hydraulic-network methods

---

##  Learning Outcomes

Through this project, I developed an understanding of how the **Hardy Cross iterative method** can be translated into a computational algorithm for solving complex pipe networks.

The project provided practical experience in:

1. Formulating hydraulic network problems.
2. Establishing initial flow distributions.
3. Applying loop-based head-loss corrections.
4. Implementing iterative numerical convergence.
5. Interpreting flow distribution across interconnected pipe branches.
6. Using Python for engineering problem solving.

---

##  Author

**Anshika Moundekar**

Mechanical Engineering
Indian Institute of Technology Patna

---

##  Project Highlights

**22 Pipes | 7 Loops | Hardy Cross Method | Python | NumPy | Iterative Hydraulic Network Analysis**
