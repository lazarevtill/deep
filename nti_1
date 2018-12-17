def save(name='test', fmt='png'):
    plt.savefig('{}.{}'.format(name, fmt), fmt=fmt)


def set_ticks(mv):
    plt.figure()
    plt.plot(np.asarray(range(len(mv))), mv)
    plt.grid()
    plt.xlabel('n, номер отсчёта')
    plt.ylabel('v, электрический потенциал')
    plt.title('ЭКГ')


def main():
    set_ticks(g)
    plt.show()
    # save()

f = []
s = []
x = input().split(' ')
for i in range(len(x)):
    nnnn, b = map(int, x[i].split(','))
    f.append(a)
    s.append(nnnn)
# print(f, s)
x=f
for m in range(2):
    
    N = 40
    # Первый алгоритм (Выделение QRS)
    g1 = []
    for n in range(len(x)):
    a = []
    for i in range(1, N + 1):
        if n - i >= 0:
            an = ((x[n - i + 1] - x[n - i]) ** 2) * (N - i + 1)
            a.append(an)
    g1.append(sum(a))
    # Второй алгоритм (фильтрация, нз зачем)
    # g = []
    # for n in range(len(x)):
    #     a = []
    #     for i in range(1, N):
    #         if n - i >= 0:
    #             an = g1[n - i]
    #             a.append(an)
    #     g.append(sum(a)/N)
    # Поиск пиков среди g
    g = g1[:]
    p = []
    th = 0.5 * max(g)
    for n in range(len(g)):
    if g[n] <= th:
        continue
    flag = False
    for i in range(1, N + 1):
        if n - i >= 0:
            if g[n] <= g[n - i]:
                flag = True
                break
        if n + i < len(g):
            if g[n] < g[n + i]:
                flag = True
                break
    if flag:
        continue
    p.append(n)

    i = 0
    while i != len(p):
    if abs(p[i] - p[i - 1]) * 2 <= 400:
        del p[i]
    else:
        i += 1

# ЗАДАЧА 1
print(len(p))

    # ЗАДАЧА 2 (фэйлится на 2-ом тесте)
    # intervals = []
    # for i in range(len(p)):
    #     if i != 0:
    #         intervals.append((p[i] - p[i - 1]) * 2)
    # print(*intervals)


if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    main()

