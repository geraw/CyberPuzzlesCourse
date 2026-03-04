from z3 import *
import time
from functools import reduce
import operator

# Modeled purely as a SAT problem using Booleans instead of Strings
# Generates a fooling set S = { (x_i, y_i) } 

def xor_sum(bools):
    if not bools: return False
    return reduce(operator.xor, bools)

k = 17
N = 4 
chars = ['a', 'b', 'c', 'd']

s = Solver()

X_vars = [[[Bool(f'X_{i}_{p}_{c}') for c in chars] for p in range(N)] for i in range(k)]
Y_vars = [[[Bool(f'Y_{i}_{p}_{c}') for c in chars] for p in range(N)] for i in range(k)]

print("Adding structural constraints (at most one char per position)...")
for i in range(k):
    for p in range(N):
        # At most one character per position
        for ci in range(len(chars)):
            for cj in range(ci + 1, len(chars)):
                s.add(Not(And(X_vars[i][p][ci], X_vars[i][p][cj])))
                s.add(Not(And(Y_vars[i][p][ci], Y_vars[i][p][cj])))               

def in_L(X_i, Y_j):
    conds = []
    for c_idx, c in enumerate(chars):
        x_bools = [X_i[p][c_idx] for p in range(N)]
        y_bools = [Y_j[p][c_idx] for p in range(N)]
        parity = xor_sum(x_bools + y_bools)
        conds.append(Not(parity))
    return And(*conds)

print("Adding fooling set constraints...")
# 1. x_i y_i must be in L
for i in range(k):
    s.add(in_L(X_vars[i], Y_vars[i]))

# 2. Cross pairs must be rejected
for i in range(k):
    for j in range(i + 1, k):
        s.add(Or(
            Not(in_L(X_vars[i], Y_vars[j])),
            Not(in_L(X_vars[j], Y_vars[i]))
        ))

# Ensure all 16 subset partitions are distinct!
for i in range(k):
    for j in range(i + 1, k):
        s.add(Or([X_vars[i][p][c] != X_vars[j][p][c] for p in range(N) for c in range(len(chars))]))

print(f"Solving for k={k}...")
start_time = time.time()
res = s.check()
print(f"Time taken: {time.time() - start_time:.2f}s")

if res == sat:
    m = s.model()
    print(f"Found a fooling set of size {k}:")
    
    def decode_word(var_matrix):
        word = ""
        for p in range(N):
            for c_idx, c in enumerate(chars):
                if is_true(m[var_matrix[p][c_idx]]):
                    word += chars[c_idx]
        return word if word else "epsilon"
        
    for i in range(k):
        xi_val = decode_word(X_vars[i])
        yi_val = decode_word(Y_vars[i])
        print(f"({xi_val}, {yi_val})")
else:
    print(f"No fooling set of size {k} exists.")