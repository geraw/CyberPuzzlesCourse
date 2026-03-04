from z3 import *
import time
from functools import reduce
import operator

def xor_sum(bools):
    # If list is empty, parity is False
    if not bools: return False
    return reduce(operator.xor, bools)

k = 16
N = 4 # MAX_LEN = 4 is enough to create all 16 subsets
chars = ['a', 'b', 'c', 'd']

s = Solver()

# X[i][p][c] = True if character c is at position p in string X_i
X_vars = [[[Bool(f'X_{i}_{p}_{c}') for c in chars] for p in range(N)] for i in range(k)]
Y_vars = [[[Bool(f'Y_{i}_{p}_{c}') for c in chars] for p in range(N)] for i in range(k)]

print("Adding at most one char per position constraints...")
for i in range(k):
    for p in range(N):
        # At most one character can be True at any position
        # (If all False, it represents epsilon)
        # For small number of variables (4), we can just do pairwise mutually exclusive
        for ci in range(len(chars)):
            for cj in range(ci + 1, len(chars)):
                s.add(Not(And(X_vars[i][p][chars[ci]], X_vars[i][p][chars[cj]])))
                s.add(Not(And(Y_vars[i][p][chars[ci]], Y_vars[i][p][chars[cj]])))

def in_L(X_i, Y_j):
    # Returns a Boolean expression representing X_i Y_j in L
    # i.e., the parity of each character over X_i and Y_j is False (even)
    conds = []
    for c_idx, c in enumerate(chars):
        x_bools = [X_i[p][c_idx] for p in range(N)]
        y_bools = [Y_j[p][c_idx] for p in range(N)]
        parity = xor_sum(x_bools + y_bools)
        # Needs to be even (False)
        conds.append(Not(parity))
    return And(*conds)

print("Adding fooling set constraints...")
for i in range(k):
    s.add(in_L(X_vars[i], Y_vars[i]))

for i in range(k):
    for j in range(i + 1, k):
        s.add(Or(
            Not(in_L(X_vars[i], Y_vars[j])),
            Not(in_L(X_vars[j], Y_vars[i]))
        ))

print(f"Solving for k={k}...")
start_time = time.time()
res = s.check()
print(f"Time taken: {time.time() - start_time:.2f}s")

if res == sat:
    m = s.model()
    print("Found a pooling set!")
    
    def decode_word(var_matrix):
        word = ""
        for p in range(N):
            found = False
            for c_idx, c in enumerate(chars):
                if is_true(m[var_matrix[p][c_idx]]):
                    word += c
                    found = True
            # if not found, it's epsilon, we just don't add anything
        return word if word else "epsilon"
        
    for i in range(k):
        xi_val = decode_word(X_vars[i])
        yi_val = decode_word(Y_vars[i])
        print(f"({xi_val}, {yi_val})")
else:
    print("unsat")
