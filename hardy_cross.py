#a,b,c are input flow rates and d,e are output flow rates #always ensure that a+b+c=d+e
a,b,c,d,e=map(float,input().split())
q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22=a/2,(a+b)/2,a/ 4,a/2,a/4,a/4,c+(a/4),(3*a/8)+(b/4),(3*a/8)+(b/4),(b/2),b/2,(3*a/8)+(3*b/4),(3*a/16)+(3*b/8),(3*a/1
6)+(3*b/8),(a+b+c)/4,(7*a/15)+(5*b/8)+(c/4),(a+b+c)/8,(a+b+c)/4,(a+b+c)/8,(5*a/16)+(b/8)+(c/2),(5* a/16)+(b/8)+(c/2),(5*a/8)+(b/4)+c


import numpy as np


# Define the initial flow guesses (m³/s) for each pipe initial_flows = {
1: q1, 2: q2, 3: q3, 4: q4, 5: q5,
6: q6, 7: q7, 8: q8, 9: q9, 10: q10,
11: q11, 12: q12, 13: q13, 14: q14, 15: q15,
16: q16, 17: q17, 18: q18, 19: q19, 20: q20,
21: q21, 22: q22
}


# Resistance constants (k-values) for each pipe k_values = {
1: 1, 2: 1, 3: 1, 4: 1, 5: 1,
6: 1, 7: 1, 8: 1, 9: 1, 10: 1,
11: 1, 12: 1, 13: 1, 14: 1, 15: 1,
16: 1, 17: 1, 18: 1, 19: 1, 20: 1,
21: 1, 22: 1
}


# Define loops, each with a list of pipes and their directions
# Directions: +1 for flow in the same direction as the loop, -1 in other cases loops = [
{'pipes': [1, 2, 3, 4], 'directions': [1, 1, -1, -1]},

{'pipes': [2, 10, 11, 9], 'directions': [-1, -1, 1, -1]},
{'pipes': [5, 3, 8, 7, 6], 'directions': [-1, 1, 1, -1, -1]},
{'pipes': [8, 9, 12, 14, 21, 22], 'directions': [-1, 1, 1, 1, -1, -1]},
{'pipes': [14, 13, 15], 'directions': [-1, 1, -1]},
{'pipes': [20, 21, 18, 19], 'directions': [-1, 1, 1, 1]},
{'pipes': [18, 15, 16, 17], 'directions': [-1, 1, 1, -1]}
]


# Set the tolerance for convergence and maximum number of iterations t = 0.0001
maxi= 10


# Initialize the flows
flows = initial_flows.copy()


# Hardy Cross iterative process for i in range(maxi):
max_correction = 0 # Track the largest correction in this iteration


for loop in loops:
# Extract pipes and directions for the current loop pipes = loop['pipes']
directions = loop['directions']


# Calculate sum of head losses and sum of derivatives for the loop sum_head_loss = 0
sum_derivative = 0


for pipe, direction in zip(pipes, directions): flow = flows[pipe]
k = k_values[pipe]

head_loss = k * flow**2 * direction derivative = 2 * k * flow * direction

sum_head_loss += head_loss sum_derivative += derivative

# Calculate correction for the loop
correction = -sum_head_loss / sum_derivative if sum_derivative != 0 else 0 max_correction = max(max_correction, abs(correction))

# Apply correction to each pipe in the loop for pipe, direction in zip(pipes, directions):
flows[pipe] += correction * direction


# Check for convergence if max_correction < t:
print(f"Converged after {i + 1} iterations.") break

# Output the final flow rates in each pipe print("Final flow rates in each pipe:")
for pipe, flow in flows.items():
print(f"Pipe {pipe}: {flow:.4f} m³/s")
