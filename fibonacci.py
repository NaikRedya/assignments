n1 = 0
n2 = 1
for n in range(0, 50):
    if n <= 1:
        print(n)
    else:
        first_terms= n1 + n2
        n1 = n2
        n2 = first_terms
        print(first_terms)
