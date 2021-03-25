genius, notGenius, t = 0, 0, int(input())
for _ in range(t):
    m, p = map(int, input().split())
    if m < 3 or p < 3 or (not (m == 10 or p == 10)) or ((m+p)/2 < 7.5):
        notGenius += 1
    else:
        genius += 1
    print(genius, notGenius)
if genius / t * 100 >= 50:
    print("Genius")
else:
    print("Not Genius Yet")

    