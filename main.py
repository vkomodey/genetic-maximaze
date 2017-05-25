import numpy as np
from numpy import sin, abs, max
from helpers import *

# Initial params
# l - length of binary vector in generation
l = 10
# t - iteration maximum
tmax = 10
# N - individuals amount in generation.
N = 50
# P_c - crossingover likelihood
p_c = 0.3
# P_m - mutation likelihood
p_m = 0.1

# function to maximize
# also this function non-negative, so it will be used as fitnes function
f = lambda x: abs(sin(x))
fitness_function = f

ksi_k_prev = init_first_generation(l, N)

first_ancestor = selection(ksi_k_prev, fitness_function, p_s, x_f)
second_ancestor = selection(ksi_k_prev, fitness_function, p_s, x_f)

crossed_first_ancestor, crossed_second_ancestor = crossingover(first_ancestor, second_ancestor, p_c)

mutated_first_ancestor = mutate(crossed_first_ancestor, p_m)
mutated_second_ancestor = mutate(crossed_second_ancestor, p_m)

