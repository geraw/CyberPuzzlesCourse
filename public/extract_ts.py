import itertools

def extract_ts(n_inputs, initial_r, delta_func, lambda_func):
  k_regs = len(initial_r)
  states = list(itertools.product([0, 1], repeat=n_inputs + k_regs))
  
  print(f'Extraction for {n_inputs} inputs and {k_regs} registers:')
  for s in states:
    inputs = s[:n_inputs]
    regs = s[n_inputs:]
    
    next_regs = delta_func(inputs, regs)
    output = lambda_func(inputs, regs)
    
    for next_inputs in itertools.product([0, 1], repeat=n_inputs):
      next_state = next_inputs + tuple(next_regs)
      print(f'  {s} --tau--> {next_state}  [Output: {output}]')

# delta_r = x | r
# lambda_y = not (x ^ r)
initial_r = [0]
extract_ts(1, initial_r, 
  lambda x, r: [x[0] | r[0]], 
  lambda x, r: not (x[0] ^ r[0]))
