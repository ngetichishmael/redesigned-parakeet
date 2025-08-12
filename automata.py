# Automata languages

# Languages
A = ["good", "bad"]
B = ["boy", "girl"]

# Union
union = list(set(A) | set(B))
print("Union:", union)

# Concatenation (Cartesian product)
concatenation = [a + b for a in A for b in B]
print("Concatenation:", concatenation)

# Kleene Closure (example for n=0 to 2)
kleene_closure = ['']  # ε (empty string)
for n in range(1, 3):  # limit to 2 repetitions for demonstration
    for word in A:
        kleene_closure.extend([word * n])
print("Kleene Closure:", kleene_closure)

# Reverse
reverse = [word[::-1] for word in A]
print("Reverse:", reverse)

# Subset
subset = A[0:1]
print("Subset:", subset)

# Superset (here just taking A itself as example)
superset = A.copy()
print("Superset:", superset)
