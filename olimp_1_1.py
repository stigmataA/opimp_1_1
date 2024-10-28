import math

K_str, M_str, T_str, X_str = input(f"Введите K, M, T, X:").split()
K = int(K_str)
M = int(M_str)
T = int(T_str)
X = int(X_str)

sevenK_minus_T = 7 * K - T

found = False
N = -1

if sevenK_minus_T > 0:
    q_min = max(0, (M - X - 7 * K + sevenK_minus_T - 1) // sevenK_minus_T)
    for q in range(q_min, q_min + 100):  # Limit the range to prevent infinite loop
        A_max = X + q * (7 * K - T) + 7 * K
        if A_max < M:
            continue
        RHS = M - X - q * (7 * K - T)
        for r in range(0, 7):
            if (r + 1) * K >= RHS:
                N = 7 * q + r + 1
                found = True
                break
        if found:
            break
    if not found:
        N = -1
elif sevenK_minus_T == 0:
    RHS = M - X
    if RHS <= 7 * K:
        r_min = (RHS + K - 1) // K - 1
        if 0 <= r_min < 7:
            N = r_min + 1
        else:
            N = -1
    else:
        N = -1
else:  # sevenK_minus_T < 0
    A_max = X + 7 * K
    if A_max < M:
        N = -1
    else:
        RHS = M - X
        for r in range(0, 7):
            if (r + 1) * K >= RHS:
                N = r + 1
                found = True
                break
        if not found:
            N = -1

print(N)