def zadanie(n):
    s = [0] * (n + 1)
    s[0], s[1] = 1, 1
    for i in range(2, n+1):
        s[i] = 2*s[i-1] - s[i-2]
    return s[n]


print(zadanie(6))