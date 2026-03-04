from z3 import *
import time

s = Solver()
MAX_WORD_LEN = 4
MAX_CONCAT_LEN = MAX_WORD_LEN * 2

def count_char(w, c):
    # Sum occurrences up to MAX_CONCAT_LEN
    return Sum([If(SubString(w, i, 1) == StringVal(c), 1, 0) for i in range(MAX_CONCAT_LEN)])

def in_L(w):
    ca = count_char(w, 'a')
    cb = count_char(w, 'b')
    cc = count_char(w, 'c')
    cd = count_char(w, 'd')
    return And(
        ca % 2 == 0,
        cb % 2 == 0,
        cc % 2 == 0,
        cd % 2 == 0,
        Length(w) == ca + cb + cc + cd # Ensures w only contains a,b,c,d
    )

k = 5
x = [String(f'x_{i}') for i in range(k)]
y = [String(f'y_{i}') for i in range(k)]

for i in range(k):
    s.add(Length(x[i]) <= MAX_WORD_LEN)
    s.add(Length(y[i]) <= MAX_WORD_LEN)
    s.add(in_L(Concat(x[i], y[i])))

for i in range(k):
    for j in range(i + 1, k):
        s.add(Or(
            Not(in_L(Concat(x[i], y[j]))),
            Not(in_L(Concat(x[j], y[i])))
        ))

print('Solving for k=5 without RE...')
start_time = time.time()
res = s.check()
print(f'Time taken: {time.time() - start_time:.2f}s')

if res == sat:
    m = s.model()
    for i in range(k):
        xi_val = m[x[i]].as_string().strip('"')
        yi_val = m[y[i]].as_string().strip('"')
        print(f'({xi_val or "epsilon"}, {yi_val or "epsilon"})')
else:
    print('unsat')
