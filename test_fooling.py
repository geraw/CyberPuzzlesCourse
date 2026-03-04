from z3 import *
import time

k = 16
x = [String(f'x_{i}') for i in range(k)]
y = [String(f'y_{i}') for i in range(k)]

a, b, c, d = Re('a'), Re('b'), Re('c'), Re('d')
Sigma = Union(a, b, c, d)

# Helper function for even parity
def even_count_re(char_re, other_chars_re):
    not_c = Star(other_chars_re)
    return Concat(not_c, Star(Concat(char_re, not_c, char_re, not_c)))

L_a = even_count_re(a, Union(b, c, d))
L_b = even_count_re(b, Union(a, c, d))
L_c = even_count_re(c, Union(a, b, d))
L_d = even_count_re(d, Union(a, b, c))

def in_L(w):
    return And(InRe(w, L_a), InRe(w, L_b), InRe(w, L_c), InRe(w, L_d))

s = Solver()

# Provide length limitations to help the solver, otherwise it might search infinite strings
max_len = 5
for i in range(k):
    s.add(Length(x[i]) <= max_len)
    s.add(Length(y[i]) <= max_len)

print("Adding constraints...")
for i in range(k):
    s.add(in_L(Concat(x[i], y[i])))
    s.add(InRe(x[i], Star(Sigma)))
    s.add(InRe(y[i], Star(Sigma)))

for i in range(k):
    for j in range(i + 1, k):
        s.add(Or(
            Not(in_L(Concat(x[i], y[j]))),
            Not(in_L(Concat(x[j], y[i])))
        ))

print(f"Solving for k={k}...")
start_time = time.time()
res = s.check()
print(f"Time taken: {time.time() - start_time:.2f}s")

if res == sat:
    m = s.model()
    print(f"Found a fooling set of size {k}:")
    for i in range(k):
        xi_val = m[x[i]].as_string().strip('"')
        yi_val = m[y[i]].as_string().strip('"')
        print(f"({xi_val or 'epsilon'}, {yi_val or 'epsilon'})")
else:
    print(f"No fooling set of size {k} exists.")
