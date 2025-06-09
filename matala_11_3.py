import networkx as nx

def find_decomposition(budget, preferences):
    """
    Check if the given budget is fractional decomposable with respect to the citizens' preferences.
    If decomposable, return a decomposition matrix d[i][j] = amount citizen i contributes to issue j.
    Otherwise, return None.
    """
    m = len(budget)
    n = len(preferences)
    total_budget = sum(budget)
    share = total_budget / n

    # Build directed flow network
    G = nx.DiGraph()
    source, sink = 's', 't'

    # Source -> citizens with capacity = share
    for i in range(n):
        G.add_edge(source, f'c{i}', capacity=share)

    # Citizens -> issues if supported, capacity = share
    for i, prefs in enumerate(preferences):
        for j in prefs:
            if 0 <= j < m:
                G.add_edge(f'c{i}', f't{j}', capacity=share)

    # Issues -> sink with capacity = budget[j]
    for j, amount in enumerate(budget):
        G.add_edge(f't{j}', sink, capacity=amount)

    # Compute maximum flow
    flow_value, flow_dict = nx.maximum_flow(G, source, sink)

    # If flow covers total_budget, decomposition exists
    if abs(flow_value - total_budget) > 1e-6:
        return None

    # Build decomposition matrix
    decomposition = [[0.0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            decomposition[i][j] = flow_dict.get(f'c{i}', {}).get(f't{j}', 0.0)

    return decomposition

# Define test cases
test_cases = [
    ("Trivial single issue", [100], [{0}]),
    ("All zero budget", [0, 0, 0], [set(), set(), set()]),
    ("Simple decomposable", [10, 10], [{0, 1}, {0, 1}]),
    ("Non-decomposable", [5, 5], [{0}, {1}]),
    ("Unequal preferences", [30, 20, 10], [{0, 1}, {1, 2}, {0, 2}]),
    ("Zero-preference citizen", [20, 20], [{0}, set()]),
    ("Question 3 example", [400, 50, 50, 0], [
        {0, 1},  # Citizen 0 supports issues 0 and 1
        {0, 2},  # Citizen 1 supports issues 0 and 2
        {0, 3},  # Citizen 2 supports issues 0 and 3
        {1, 2},  # Citizen 3 supports issues 1 and 2
        {0}      # Citizen 4 supports issue 0 only
    ]),
]

# Execute and display test results
for name, budget, prefs in test_cases:
    print(f"Test: {name}")
    result = find_decomposition(budget, prefs)
    if result is None:
        print("  Result: Not decomposable\n")
    else:
        print("  Result: Decomposable. Matrix:")
        for i, row in enumerate(result):
            formatted = ', '.join(f"{val:.2f}" for val in row)
            print(f"    Citizen {i}: [{formatted}]")
        print()
