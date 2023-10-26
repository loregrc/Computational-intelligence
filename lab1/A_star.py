#Imports
from random import random
from math import ceil
from functools import reduce
from collections import namedtuple
from queue import PriorityQueue

import numpy as np

#Problem Constraints
PROBLEM_SIZE = 10
NUM_SETS = 20

#Inizialization
SETS = tuple(np.array([random() < 0.3 for _ in range(PROBLEM_SIZE)]) for _ in range(NUM_SETS))

State = namedtuple('State', ['taken', 'not_taken'])

#Printing SETS to have a visual idea of the problem
for s in SETS:
    print(s)

#Goal checking
def covered(state):
    return reduce(np.logical_or, [SETS[i] for i in state.taken], np.array([False for _ in range(PROBLEM_SIZE)]))

def goal_check(state):
    return np.all(covered(state))

#Verify if problem is solvable
assert goal_check(State(set(range(NUM_SETS)), set())), "Problem not solvable"
print("Problem is solvable")

#h functions
def h_remaining_coverage(state):
    return PROBLEM_SIZE - sum(covered(state))

def f(state):
    return len(state.taken) + h_remaining_coverage(state)

#A* Algorithm
frontier = PriorityQueue()
state = State(set(), set(range(NUM_SETS)))
steps = 0
frontier.put((f(state), state))

_, current_state = frontier.get()
while not goal_check(current_state):
    steps += 1
    for action in current_state.not_taken:
        new_state = State(
            current_state.taken ^ {action},
            current_state.not_taken ^ {action},
        )
        frontier.put((f(new_state), new_state))
    _, current_state = frontier.get()

print(
    f"Solved in {steps:,} steps ({len(current_state.taken)} tiles)"
)