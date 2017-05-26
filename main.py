import numpy as np
from numpy import sin, abs, max
from helpers import *
import time

# Initial params
# l - length of binary vector in generation
l = 5
# t - iteration maximum
tmax = 3
# N - individuals amount in generation.
N = 30
# P_c - crossingover likelihood
p_c = 0.3
# P_m - mutation likelihood
p_m = 0.1

# function to maximize
# also this function non-negative, so it will be used as fitnes function
f = lambda x: abs(sin(x))
fitness_function = f

start_time = time.time()

current_generation = init_first_generation(l, N)

for t in range(tmax):
    print t
    next_generation = np.empty([N, l])

    for k in range(N / 2):
        first_ancestor = selection(current_generation, fitness_function, p_s, x_f)
        second_ancestor = selection(current_generation, fitness_function, p_s, x_f)

        crossed_first_ancestor, crossed_second_ancestor = crossingover(first_ancestor, second_ancestor, p_c)

        mutated_first_ancestor = mutate(crossed_first_ancestor, p_m)
        mutated_second_ancestor = mutate(crossed_second_ancestor, p_m)

        next_generation[2*k - 1] = mutated_first_ancestor
        next_generation[2*k] = mutated_second_ancestor

    current_generation = next_generation


print "---- %s seconds " % (time.time() - start_time)
