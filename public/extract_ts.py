import itertools

def extract_ts(n_inputs, initial_r, delta, lam):
  k = len(initial_r)
  states = list(itertools.product([0, 1], repeat=n_inputs + k))
  transitions = []
  labels = {}

  for s in states:
    x, r = s[:n_inputs], s[n_inputs:]
    out = lam(x, r)
    # Build label: active propositions
    ap = []
    for i, v in enumerate(x):
      if v: ap.append(f'x{i+1}' if n_inputs > 1 else 'x')
    for i, v in enumerate(r):
      if v: ap.append(f'r{i+1}' if k > 1 else 'r')
    if out: ap.append('y')
    labels[s] = '{' + ','.join(ap) + '}'

    next_r = tuple(delta(x, r))
    for nx in itertools.product([0, 1], repeat=n_inputs):
      transitions.append((s, nx + next_r))

  init = [s for s in states if s[n_inputs:] == tuple(initial_r)]
  return states, transitions, init, labels

def show_ts(states, transitions, init, labels):
  print("States:")
  for s in states:
    marker = " (initial)" if s in init else ""
    print(f"  {s}  L={labels[s]}{marker}")
  print(f"\nTransitions ({len(transitions)}):")
  seen = set()
  for src, tgt in transitions:
    edge = (src, tgt)
    if edge not in seen:
      seen.add(edge)
      print(f"  {src} --> {tgt}")

# Example: delta_r = x|r, lambda_y = not(x^r)
S, T, I, L = extract_ts(1, [0],
  lambda x, r: [x[0] | r[0]],
  lambda x, r: not (x[0] ^ r[0]))
show_ts(S, T, I, L)
