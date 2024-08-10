a1, a2 = map(int, input().split())

sequence = [a1, a2]

for i in range(2, 10):
    next_term = sequence[i-1] + 2 * sequence[i-2]
    sequence.append(next_term)

print(" ".join(map(str, sequence)))